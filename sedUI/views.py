from django.shortcuts import render, render_to_response, redirect, HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User, Group
from .models import Course, Scout, Workshop, Session, Instructor, AboutPage, HomePage, Checkout, MailPayment, Location, Register
from django.views import generic
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password
from django.views.generic import View
from random import randint, shuffle
from .forms import RegistrationForm1, RegistrationForm2, RegistrationScoutForm1, RegistrationScoutForm2, RegistrationVolunteerForm1, RegistrationVolunteerForm2, RegistrationPaymentForm, ContactEmailForm, BadgeForm
from formtools.wizard.views import WizardView, SessionWizardView, CookieWizardView
import os, datetime, re, pytz, stripe, urlparse
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.core.management.utils import get_random_secret_key
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
import json
from django.core.files.storage import FileSystemStorage
# import django_tables2 as tables
# from django_tables2 import SingleTableView

# Create your views here.
class IndexView(generic.TemplateView):
    template_name='sedUI/pages/index.html'
    def get(self, request, *args, **kwargs):
        HomePage_object=getHomePageLatest()
        aboutPage = getAboutPageLatest()
        isOpen=checkOpenDate()
        img_fileNames = []
        #Add first image
        img_fileNames.append(os.path.join('img/images/', '00001.jpg'))
        # for filename in os.listdir("sed/sedUI/static/img/homeImages"):    # Use if running on AWS Server
        for filename in os.listdir("sedUI/static/img/homeImages"):          # Use if running on Local Machine
            img_fileNames.append(os.path.join('img/homeImages/', filename))
        return render(request, 'sedUI/pages/index.html', {"fileNames" : img_fileNames, "HomePage": HomePage_object,'aboutPage' : aboutPage, 'isOpen' : isOpen})

class ContactConfirmationView(generic.TemplateView):
    template_name = 'sedUI/pages/contactConfirmation.html'

class ContactConfirmationViewMember(generic.ListView):
    template_name = 'sedUI/pages/contactConfirmation.html'
    context_object_name='register'
    def get_queryset(self):
        return Register.objects.get(registration_id=self.kwargs['registration_id'], register_sui=self.kwargs['register_sui'])
    def get_context_data(self, **kwargs):
        ctx=super(ContactConfirmationViewMember, self).get_context_data(**kwargs)
        ctx["register"]=Register.objects.get(registration_id=self.kwargs['registration_id'], register_sui=self.kwargs['register_sui'])
        return ctx

class ContactView(SessionWizardView):
    form_list=[ContactEmailForm]
    template_name = 'sedUI/pages/contact.html'

    def done(self, form_list, **kwargs):
        form_data=self.get_cleaned_data_for_step('0')
        contact_send_email(form_list)
        return redirect(reverse('contactConfirmation'))

def contact_send_email(form_list):
    form_data = [form.cleaned_data for form in form_list]
    message1 = str(form_data[0]["contact_first_name"]) + " " + str(form_data[0]["contact_last_name"]) + " (" + str(form_data[0]["email_address"]) + ") sent the message: \n\n" + str(form_data[0]["message"])
    message2 = "Hello " + str(form_data[0]["contact_first_name"]) + " " + str(form_data[0]["contact_last_name"]) + ",\n\n" + "Your Message was sent to the SED Team and they will be responding shortly any additional information or inquiries can be sent to support@sedteam.org. \n\n" + " Your Message: " + str(form_data[0]["message"])
    email1 = EmailMessage(
        str(form_data[0]["message_subject"]),
        message1,
        settings.EMAIL_DEFAULT_USER,
        ["support@sedteam.org"],
    )
    email2 = EmailMessage(
        str(form_data[0]["message_subject"]),
        message2,
        settings.EMAIL_DEFAULT_USER,
        [form_data[0]["email_address"]],
    )

    email1.send(fail_silently=False)
    email2.send(fail_silently=False)

    return form_data

# def login(request):
#     return render(request, 'sedUI/pages/basic.html')

# def loginOrRegister(request):
#     return render(request, 'sedUI/pages/loginOrRegister.html')

class CourseView(generic.ListView):
    template_name = 'sedUI/pages/courses.html'
    context_object_name = 'all_courses'
    def get_queryset(self):
        return Course.objects.all().order_by('course_name')

class CourseDetailView(generic.ListView):
    template_name = 'sedUI/pages/course_detail.html'
    context_object_name = 'course'
    def get_queryset(self):
        return Course.objects.get(course_id=self.kwargs['course_id'])

    def get_context_data(self, **kwargs):
        ctx=super(CourseDetailView, self).get_context_data(**kwargs)
        try:
            ctx['instructorAM']=getInstructorbyCourse(self.get_queryset().course_id, "AM")
        except:
            ctx['instructorAM']=None
        try:
            ctx['instructorPM']=getInstructorbyCourse(self.get_queryset().course_id, "PM")
        except:
            ctx['instructorPM']=None
        try:
            ctx['instructorFULL']=getInstructorbyCourse(self.get_queryset().course_id, "FULL")
        except:
            ctx['instructorFULL']=None
        return ctx

class ScoutView(generic.ListView):
    template_name = 'sedUI/pages/scouts.html'
    context_object_name = 'all_scouts'

    def get_queryset(self):
        return Scout.objects.all()

class ScoutDetailView(generic.ListView):
    template_name = 'sedUI/pages/scout_detail.html'
    context_object_name='scout'
    def get_queryset(self):
        return Scout.objects.get(scout_id=self.kwargs['scout_id'])

    def get_context_data(self, **kwargs):
        ctx=super(ScoutDetailView, self).get_context_data(**kwargs)
        session_data=getSessionByUniqueSession(self.get_queryset().scout_id, self.get_queryset().scout_year)
        ctx['session']=session_data
        #check if workshop are done
        ctx['workshop1']=getCourseBySession(session_data.workshop1_id)
        ctx['workshop2']=getCourseBySession(session_data.workshop2_id)
        return ctx

def event_checkin(request, scout_id):
    try:
        scout=getScoutByUniqueScout(scout_id, datetime.datetime.now().year)
        session=getSessionByUniqueSession(scout_id, scout.scout_year)
        if(session.workshop2_status=="COMPLETE" or session.workshop2_status=='INCOMPLETE'):
            scout.scout_status='WORKSHOP2_CHECKOUT'
            scout.save()
            session.workshop2_checkout=datetime.datetime.now()
            session.save()
            return HttpResponseRedirect(reverse('scout_detail/', args=(scout_id,)))
        elif(session.workshop1_status=="COMPLETE" or session.workshop1_status=='INCOMPLETE'):
            scout.scout_status='WORKSHOP1_CHECKOUT'
            scout.save()
            session.workshop1_checkout=datetime.datetime.now()
            session.save()
            return HttpResponseRedirect(reverse('scout_detail/', args=(scout_id,)))
        elif(getCourseBySession(session.workshop1_id).course_name=='None'):
            scout.scout_status='WORKSHOP1_CHECKOUT'
            scout.save()
            session.workshop1_checkout=datetime.datetime.now()
            session.save()
            return HttpResponseRedirect(reverse('scout_detail/', args=(scout_id,)))
        elif(scout.scout_status=="UNDERWAY" or scout.scout_status=='EVENT_CHECKOUT'):
            scout.scout_status='EVENT_CHECKIN'
            scout.save()
            session.event_checkin=datetime.datetime.now()
            session.save()
            return HttpResponseRedirect(reverse('scout_detail/', args=(scout_id,)))
        else:
            return render_to_response('sedUI/pages/errorPage.html', status=404)
    except:
        return render_to_response('sedUI/pages/errorPage.html', status=404)

def event_checkout(request, scout_id):
    try:
        scout=getScoutByUniqueScout(scout_id, datetime.datetime.now().year)
        if(scout.scout_status=='EVENT_CHECKIN' or scout.scout_status=='WORKSHOP1_CHECKOUT' or scout.scout_status=='WORKSHOP2_CHECKOUT'):
            scout.scout_status='EVENT_CHECKOUT'
            scout.save()
            session=getSessionByUniqueSession(scout_id, scout.scout_year)
            session.event_checkout=datetime.datetime.now()
            session.save()
            return HttpResponseRedirect(reverse('scout_detail/', args=(scout_id,)))
        else:
            return render_to_response('sedUI/pages/errorPage.html', status=404)
    except:
        return render_to_response('sedUI/pages/errorPage.html', status=404)

def workshop_checkin(request, scout_id):
    workshop_checkinI(scout_id)
    return HttpResponseRedirect(reverse('scout_detail/', args=(scout_id,)))

def workshop_checkinI(scout_id):
    try:
        scout=getScoutByUniqueScout(scout_id, datetime.datetime.now().year)
        session=getSessionByUniqueSession(scout_id, scout.scout_year)
        if(scout.scout_status=='EVENT_CHECKIN'):
            scout.scout_status='WORKSHOP1_CHECKIN'
            scout.save()
            session.workshop1_status='IN PROGRESS'
            session.workshop1_checkin=datetime.datetime.now()
            session.save()
        elif(scout.scout_status=='WORKSHOP1_CHECKOUT' and session.workshop2_id != '0'):
            scout.scout_status='WORKSHOP2_CHECKIN'
            scout.save()
            session.workshop2_status='IN PROGRESS'
            session.workshop2_checkin=datetime.datetime.now()
            session.save()
        else:
            return render_to_response('sedUI/pages/errorPage.html', status=404)
    except:
        return render_to_response('sedUI/pages/errorPage.html', status=404)

def workshop_checkinW(scout_id, workshop_id):
    try:
        scout=getScoutByUniqueScout(scout_id, datetime.datetime.now().year)
        session=getSessionByUniqueSession(scout_id, scout.scout_year)
        workshop=Workshop.objects.get(workshop_id=workshop_id)
        if(workshop.workshop_time=='AM' or workshop.workshop_time=='FULL'):
            if(scout.scout_status=='EVENT_CHECKIN'):
                scout.scout_status='WORKSHOP1_CHECKIN'
                scout.save()
                session.workshop1_status='IN PROGRESS'
                session.workshop1_checkin=datetime.datetime.now()
                session.save()
        elif(workshop.workshop_time=='PM'):
            scout.scout_status='WORKSHOP2_CHECKIN'
            scout.save()
            session.workshop2_status='IN PROGRESS'
            session.workshop2_checkin=datetime.datetime.now()
            session.save()
        else:
            return render_to_response('sedUI/pages/errorPage.html', status=404)
    except:
        return render_to_response('sedUI/pages/errorPage.html', status=404)

def workshop_completed(request, scout_id):
    workshop_completedI(scout_id)
    return HttpResponseRedirect(reverse('scout_detail/', args=(scout_id,)))

def workshop_completedI(scout_id):
    try:
        scout=getScoutByUniqueScout(scout_id, datetime.datetime.now().year)
        session=getSessionByUniqueSession(scout_id, scout.scout_year)
        if(scout.scout_status=='WORKSHOP1_CHECKIN'):
            scout.scout_status='WORKSHOP1_CHECKOUT'
            scout.save()
            session.workshop1_status="COMPLETE"
            session.workshop1_checkout=datetime.datetime.now()
            session.save()
        elif(scout.scout_status=='WORKSHOP2_CHECKIN'):
            scout.scout_status='WORKSHOP2_CHECKOUT'
            scout.save()
            session.workshop2_status="COMPLETE"
            session.workshop2_checkout=datetime.datetime.now()
            session.save()
        else:
            return render_to_response('sedUI/pages/errorPage.html', status=404)
    except:
        return render_to_response('sedUI/pages/errorPage.html', status=404)

def workshop_completedW(scout_id, workshop_id):
    try:
        scout=getScoutByUniqueScout(scout_id, datetime.datetime.now().year)
        session=getSessionByUniqueSession(scout_id, scout.scout_year)
        workshop=Workshop.objects.get(workshop_id=workshop_id)
        if(workshop.workshop_time=='AM' or workshop.workshop_time=='FULL'):
            scout.scout_status='WORKSHOP1_CHECKOUT'
            scout.save()
            session.workshop1_status="COMPLETE"
            session.workshop1_checkout=datetime.datetime.now()
            session.save()
        elif(workshop.workshop_time=='PM'):
            scout.scout_status='WORKSHOP2_CHECKOUT'
            scout.save()
            session.workshop2_status="COMPLETE"
            session.workshop2_checkout=datetime.datetime.now()
            session.save()
        else:
            return render_to_response('sedUI/pages/errorPage.html', status=404)
    except:
        return render_to_response('sedUI/pages/errorPage.html', status=404)

def workshop_checkout(request, scout_id):
    workshop_checkoutI(scout_id)
    return HttpResponseRedirect(reverse('scout_detail/', args=(scout_id,)))

def workshop_checkoutI(scout_id):
    try:
        scout=getScoutByUniqueScout(scout_id, datetime.datetime.now().year)
        session=getSessionByUniqueSession(scout_id, scout.scout_year)
        if(scout.scout_status=='WORKSHOP1_CHECKIN'):
            scout.scout_status='WORKSHOP1_CHECKOUT'
            scout.save()
            session.workshop1_status="INCOMPLETE"
            session.workshop1_checkout=datetime.datetime.now()
            session.save()
        elif(scout.scout_status=='WORKSHOP2_CHECKIN'):
            scout.scout_status='WORKSHOP2_CHECKOUT'
            scout.save()
            session.workshop2_status="INCOMPLETE"
            session.workshop2_checkout=datetime.datetime.now()
            session.save()
        else:
            return render_to_response('sedUI/pages/errorPage.html', status=404)
    except:
        return render_to_response('sedUI/pages/errorPage.html', status=404)

def workshop_checkoutW(scout_id, workshop_id):
    try:
        scout=getScoutByUniqueScout(scout_id, datetime.datetime.now().year)
        session=getSessionByUniqueSession(scout_id, scout.scout_year)
        workshop=Workshop.objects.get(workshop_id=workshop_id)
        if(workshop.workshop_time=='AM' or workshop.workshop_time=='FULL'):
            scout.scout_status='WORKSHOP1_CHECKOUT'
            scout.save()
            session.workshop1_status="INCOMPLETE"
            session.workshop1_checkout=datetime.datetime.now()
            session.save()
        elif(workshop.workshop_time=='PM'):
            scout.scout_status='WORKSHOP2_CHECKOUT'
            scout.save()
            session.workshop2_status="INCOMPLETE"
            session.workshop2_checkout=datetime.datetime.now()
            session.save()
        else:
            return render_to_response('sedUI/pages/errorPage.html', status=404)
    except:
        return render_to_response('sedUI/pages/errorPage.html', status=404)

class WorkshopView(generic.ListView):
    template_name = 'sedUI/pages/workshop.html'
    context_object_name = 'all_workshop'

    def get_queryset(self):
        return Workshop.objects.all().filter(workshop_year=datetime.datetime.now().year)


    def get_context_data(self, **kwargs):
        ctx=super(WorkshopView, self).get_context_data(**kwargs)
        ctx['all_workshop_custom']=getWorkshopCustom()
        ctx['current_date']=datetime.datetime.now().year
        return ctx

class WorkshopDetailView(generic.ListView):
    template_name = 'sedUI/pages/workshop_detail.html'
    context_object_name='workshop'


    def get_queryset(self):
        return Workshop.objects.get(workshop_id=self.kwargs['workshop_id'])

    def get_context_data(self, **kwargs):
        ctx=super(WorkshopDetailView, self).get_context_data(**kwargs)
        ctx['instructor']=getInstructorByID(self.get_queryset().instructor_id)
        ctx['location']=getLocationByID(self.get_queryset().location_id)
        ctx['course']=getCourseByID(self.get_queryset().course_id)
        ctx['scouts']=getScoutSessionsByWorkshop(self.get_queryset().workshop_id, self.get_queryset().workshop_time)
        return ctx

class ReportView(generic.TemplateView):
    template_name = 'sedUI/pages/reportAnalysis.html'
    def get(self, request, *args, **kwargs):
        context = {
            'all_courses' : Course.objects.all(),
            'all_scouts' : Scout.objects.all(),
            'all_session' : Session.objects.all(),
            'all_workshop' : Workshop.objects.all(),
            'all_instructor' : Instructor.objects.all()
        }
    	return render(request, 'sedUI/pages/reportAnalysis.html', context)

    def get_context_data(self, **kwargs):
        return context

class ProfileView(generic.TemplateView):
    template_name = 'sedUI/pages/profile.html'

class AboutView(generic.TemplateView):
    template_name='sedUI/pages/about.html'
    # context_object_name = 'all_courses'
    def get(self, request, *args, **kwargs):
    	aboutPage = getAboutPageLatest()
        # all_courses = []
        # for course in Course.objects.all():
        #     if re.search("\w* - [b-zB-Z]", course, re.IGNORECASE) != True:
        #         all_courses.append(course)
        all_courses = Course.objects.all().exclude(course_name='None')
        left_items = all_courses[:(len(all_courses)+1)/2]
        right_items = all_courses[(len(all_courses)+1)/2:]
        current_datetime = datetime.datetime.now()
        isOpen=checkOpenDate()
        # if (current_datetime>aboutPage.registrationOpenDate) and (current_datetime<aboutPage.saveDate):
        #     isOpen=True
        # else:
        #     isOpen=False
        context = {
            'all_courses' : all_courses,
            'left_items' : left_items,
            'right_items' : right_items,
            'aboutPage' : aboutPage,
            'isOpen' : isOpen
        }
    	return render(request, 'sedUI/pages/about.html', context)

class BadgeView(SessionWizardView):
    form_list=[BadgeForm]
    template_name = 'sedUI/pages/getBadge.html'

    def done(self, form_list, **kwargs):
        form_data=self.get_cleaned_data_for_step('0')
        confirmation_id=form_data["confirmation_id"]
        scout_id=form_data["scout_id"]
        scout_data=None
        if(confirmation_id):
            scout_data=getScoutByConfirmation_id(confirmation_id)
        elif(scout_id):
            scout_year=str(datetime.datetime.now().year)
            scout_data=getScoutByUniqueScout(scout_id, scout_year)
        else:
            return render_to_response('sedUI/pages/errorPage.html', status=404)
        try:
            session_data=getSessionByUniqueSession(scout_data.scout_id, scout_data.scout_year)
            course_1=getCourseBySession(session_data.workshop1_id)
            location_1=getLocationByWorkshop(session_data.workshop1_id)
            if(session_data.workshop2_id!='0' or session_data.workshop2_id!=None):
                course_2=getCourseBySession(session_data.workshop2_id)
                location_2=getLocationByWorkshop(session_data.workshop2_id)
            else:
                course_2=None
                location_2=None
            return render_to_response('sedUI/pages/showBadge.html',
            {'form_data': [form.cleaned_data for form in form_list],
                'scout': scout_data,
                'session': session_data,
                'workshop_1': course_1,
                'workshop_2': course_2,
                'location_1': location_1,
                'location_2': location_2
            })
        except:
        	return render_to_response('sedUI/pages/errorPage.html', status=404)

class AllBadgesView(generic.ListView):
    template_name = 'sedUI/pages/getAllBadges.html'
    context_object_name = 'all_scouts'

    def get_queryset(self):
        return Scout.objects.all()

    def get_context_data(self, **kwargs):
    	ctx=super(AllBadgesView, self).get_context_data(**kwargs)

    	ctx['data']={}
        for scout in Scout.objects.all():
            session_data=getSessionByUniqueSession(scout.scout_id, scout.scout_year)
            location_1=getLocationByWorkshop(session_data.workshop1_id)
            location_2=getLocationByWorkshop(session_data.workshop2_id)
            workshop_1=getCourseBySession(session_data.workshop1_id)
            workshop_2=getCourseBySession(session_data.workshop2_id)
            try:
                workshop_1_data=str(workshop_1.course_name)+" - "+str(location_1.location_room)
            except:
                workshop_1_data=" "
            try:
                workshop_2_data=str(workshop_2.course_name)+" - "+str(location_2.location_room)
            except:
                workshop_2_data=" "
            scout_information={'scout': scout,
            'workshop_1': workshop_1_data,
            'workshop_2': workshop_2_data,
            'session': session_data,
            }
            scoutstring=str(scout.scout_id)
            ctx['data'].update({scoutstring:scout_information})
        sorted(ctx['data'].iteritems())
        return ctx

## Registration Process
class RegistrationIssueView(generic.TemplateView):
    template_name = 'sedUI/pages/registrationIssue.html'

class RegistrationVolunteerWizard(SessionWizardView):
    template_name = 'sedUI/pages/registration_form.html'
    form_list = [RegistrationForm1, RegistrationForm2, RegistrationVolunteerForm1, RegistrationVolunteerForm2]
    def render_next_step(self, form, **kwargs):
        """
        This method gets called when the next step/form should be rendered.
        `form` contains the last/current form.
        """
        # get the form instance based on the data from the storage backend
        # (if available).

        # check citizen status
        if(self.steps.current=='0'):
            data=self.get_cleaned_data_for_step('0')
            if(data["citizenship"]=='No'):
                return redirect(reverse('registrationIssue'))


        # run default render_next_step
        next_step = self.steps.next
        new_form = self.get_form(
            next_step,
            data=self.storage.get_step_data(next_step),
            files=self.storage.get_step_files(next_step),
        )

        # change the stored current step
        self.storage.current_step = next_step
        return self.render(new_form, **kwargs)

    def get_form_initial(self, step):
        initial = {}
        if(step=='2'):
            data=self.get_cleaned_data_for_step('1')
            if(data['register_is_volunteer']==True):
                initial["volunteer_first_name"] = data['register_first_name']
                initial["volunteer_last_name"] = data['register_last_name']
                initial["volunteer_email"] = data['register_email']
                initial["volunteer_email_confirm"] = data['register_email']
                initial["volunteer_phone"] = data['register_phone']
        return self.initial_dict.get(step, initial)
    # def get_context_data(self, **kwargs):
    #     ctx = super(RegistrationVolunteerWizard, self).get_context_data(**kwargs)
    #     try:
    #         ctx['volunteerList']

    def done(self, form_list, **kwargs):
        register_data = self.get_cleaned_data_for_step('1')
        volunteer_data=self.get_cleaned_data_for_step('2')
        task_data=self.get_cleaned_data_for_step('3')
        username=generateUsername(register_data["register_first_name"], register_data["register_last_name"])
        password=generatePassword()
        register = Register(
            register_first_name = form_data["contact_first_name"],
            register_last_name = form_data["contact_last_name"],
            register_email = form_data["email_address"],
            register_sui = username,
            register_code = passcode,
            register_type = register_type,
            registration_year = str(datetime.datetime.now().year),
            volunteer = True
        )
        user = User.objects.create(
            username=register.register_sui,
            first_name =register.register_first_name,
            last_name = register.register_last_name,
            email=register.register_email,
            password=make_password(register.register_code)
        )
        s
        if(register_data["mitre_employee"]):
            my_group=Group.objects.get("mitre")
            my_group.user_set.add(user)

        if(register_data["volunteer"]):
            my_group=Group.objects.get("volunteer")
            my_group.user_set.add(user)

        register.save()
        return render_to_response('sedUI/pages/registrationConfirmation.html', {'form_data': [form.cleaned_data for form in form_list]})

class RegistrationScoutWizard(SessionWizardView):
    form_list = [RegistrationForm1, RegistrationForm2, RegistrationScoutForm1, RegistrationScoutForm2, RegistrationPaymentForm]
    template_name = 'sedUI/pages/registration_form.html'

    def get_context_data(self, **kwargs):
        ctx = super(RegistrationScoutWizard, self).get_context_data(**kwargs)
        try:
            ctx['isOpen']=checkOpenDate()
            ctx['payment']=getMailPaymentLatest()
            ctx['checkout']=getCheckoutLatest()
        except:
            ctx['isOpen']=checkOpenDate()
            ctx['payment']=None
            ctx['checkout']=None
        # try:
        #     register_data = self.get_cleaned_data_for_step('1')
        #     ctx['scoutList']=getScoutList(register_data['register_id'])
        # except:
        #     ctx['scoutList']=None
        return ctx

    def render(self, form=None, **kwargs):
        form = form or self.get_form()
        if self.steps.current=='4':
            context = self.get_context_data(form=form, **kwargs)
            return self.render_to_response(context)
        context = self.get_context_data(form=form, **kwargs)
        return self.render_to_response(context)

    def render_next_step(self, form, **kwargs):
        """
        This method gets called when the next step/form should be rendered.
        `form` contains the last/current form.
        """
        # get the form instance based on the data from the storage backend
        # (if available).

        # check citizen status
        if(self.steps.current == '0'):
            data = self.get_cleaned_data_for_step('0')
            if(data["citizenship"] == 'No'):
                return redirect(reverse('registrationIssue'))

        # if(self.steps.current == '1'):
        #     data = self.get_cleaned_data_for_step('1')
        #     register.save()

        # run default render_next_step
        next_step = self.steps.next
        new_form = self.get_form(
            next_step,
            data=self.storage.get_step_data(next_step),
            files=self.storage.get_step_files(next_step),
        )

        # change the stored current step
        self.storage.current_step = next_step
        return self.render(new_form, **kwargs)

    def done(self, form_list, **kwargs):
        course_1=None
        course_2=None
        register_data = self.get_cleaned_data_for_step('1')
        scout_data=self.get_cleaned_data_for_step('2')
        workshop_data=self.get_cleaned_data_for_step('3')
        session_data=self.get_cleaned_data_for_step('4')

        if(session_data["payment_method"]=="Pay_Online"):
        	stripeCall(self.request)

        # store into database scout table
        scout_size=Scout.objects.all().count()
        RegistrationClosedTrigger()
        scout_size=scout_size+1
        RegistrationClosedTrigger()
        scout = Scout(scout_first_name=scout_data["first_name"],
            scout_last_name=scout_data["last_name"],
            unit_number=scout_data["unit_number"],
            scout_phone=scout_data["phone"],
            scout_email=scout_data["email"],
            emergency_first_name=scout_data["emergency_first_name"],
            emergency_last_name=scout_data["emergency_last_name"],
            emergency_phone=scout_data["emergency_phone"],
            emergency_email=scout_data["emergency_email"],
            scout_type=scout_data["affiliation"],
            scout_photo=scout_data["photo"],
            scout_medical=scout_data["medical_notes"],
            scout_allergy=scout_data["allergy_notes"],
            scout_status="UNDERWAY",
            scout_year=str(datetime.datetime.now().year)
            )
        scout.save()
        # # store into database session table
        #filter courses
        workshop1_data=str(workshop_data["morning_subject"]).split('-')
        payment_status_info="PAID"
        if(session_data["payment_method"]=="Waived"):
            payment_status_info="PAID"
        elif(session_data["payment_method"]=="Pay_Online"):
            payment_status_info="PAID"
        else:
            payment_status_info="NOT PAID"

        if(workshop1_data[1]=="FULL"):
            WorkshopClosedTrigger(getWorkshopbyCourse(workshop1_data[0], workshop1_data[1]), workshop1_data[1])
            session = Session(
                scout_id=scout.scout_id,
                payment_method=session_data["payment_method"],
                payment_amount="40.00",
                payment_status=payment_status_info,
                open_ceremony=getOpenCeremonybyWorkshop(workshop1_data[0], "FULL"),
                workshop1_id=getWorkshopbyCourse(workshop1_data[0], "FULL"),
                workshop1_status="IN PROGRESS",
                workshop2_id=None,
                workshop2_status="IN PROGRESS",
                confirmation_timestamp=datetime.datetime.now(),
                session_year=str(datetime.datetime.now().year)
            )
            session.save()
            course_1=getCourseBySession(session.workshop1_id)
            course_2=None
        else:
            WorkshopClosedTrigger(getWorkshopbyCourse(workshop1_data[0], workshop1_data[1]), workshop1_data[1])
            #if there is a PM CLass
            workshop2_data=None
            if(workshop_data["evening_subject"]!=None):
                workshop2_data=str(workshop_data["evening_subject"]).split('-')
                WorkshopClosedTrigger(getWorkshopbyCourse(workshop2_data[0], workshop2_data[1]), workshop2_data[1])
                session = Session(
                    scout_id=scout.scout_id,
                    payment_method=session_data["payment_method"],
                    payment_amount="40.00",
                    payment_status=payment_status_info,
                    open_ceremony=getOpenCeremonybyWorkshop(workshop1_data[0], "AM"),
                    workshop1_id=getWorkshopbyCourse(workshop1_data[0], "AM"),
                    workshop2_id=getWorkshopbyCourse(workshop2_data[0], "PM"),
                    workshop1_status="IN PROGRESS",
                    workshop2_status="IN PROGRESS",
                    confirmation_timestamp=datetime.datetime.now(),
                    session_year=str(datetime.datetime.now().year)
                )
                session.save()
                course_1=getCourseBySession(session.workshop1_id)
                course_2=getCourseBySession(session.workshop2_id)
            # Error issue
            else:
                workshop2_data=None
                print("Error")
                session = Session(
                    scout_id=scout.scout_id,
                    payment_method=session_data["payment_method"],
                    payment_amount="40.00",
                    payment_status=payment_status_info,
                    open_ceremony=getOpenCeremonybyWorkshop(workshop1_data[0], "AM"),
                    workshop1_id=getWorkshopbyCourse(workshop1_data[0], "AM"),
                    workshop1_status="IN PROGRESS",
                    workshop2_id=None,
                    workshop2_status="IN PROGRESS",
                    confirmation_timestamp=datetime.datetime.now(),
                    session_year=str(datetime.datetime.now().year)
                )
                session.save()
                course_1=getCourseBySession(session.workshop1_id)
                course_2=None

        all_models_dict ={
        	'form_data': [form.cleaned_data for form in form_list],
    		'scout': scout,
    		'session': session,
    		'workshop_1': course_1,
            'workshop_2': course_2
        }

        if(register_data["volunteer_checkbox"]):
            my_group=Group.objects.get(name="volunteer")
            username=generateUsername(register_data["register_first_name"], register_data["register_last_name"])
            password=generatePassword()
            register = Register(
                register_first_name = register_data["register_first_name"],
                register_last_name = register_data["register_last_name"],
                register_email = register_data["register_email"],
                register_sui = username,
                register_code = password,
                register_type = "volunteer",
                registration_year = str(datetime.datetime.now().year),
                volunteer = register_data["volunteer_checkbox"]
            )
            register.save()
            user = User.objects.create(
                username=register.register_sui,
                first_name =register.register_first_name,
                last_name = register.register_last_name,
                email=register.register_email,
                password=make_password(register.register_code)
            )
            my_group.user_set.add(user)

        if(register_data["mitre_employee"]):
            my_group=Group.objects.get(name="mitre")
            username=generateUsername(register_data["register_first_name"], register_data["register_last_name"])
            password=generatePassword()
            register = Register(
                register_first_name = register_data["register_first_name"],
                register_last_name = register_data["register_last_name"],
                register_email = register_data["register_email"],
                register_sui = username,
                register_code = password,
                register_type = "MITRE",
                registration_year = str(datetime.datetime.now().year),
                volunteer = register_data["volunteer_checkbox"]
            )
            register.save()
            user = User.objects.create(
                username=register.register_sui,
                first_name =register.register_first_name,
                last_name = register.register_last_name,
                email=register.register_email,
                password=make_password(register.register_code)
            )
            my_group.user_set.add(user)

        confirmation_timestamp=session.confirmation_timestamp
        confirmation_send_email(form_list, scout.scout_id, str(scout.confirmation_id))
        return render_to_response('sedUI/pages/registrationConfirmation.html', {'form_data': [form.cleaned_data for form in form_list],
    		'scout': scout,
    		'session': session,
    		'workshop_1': course_1,
            'workshop_2': course_2
        	})

def generateUsername(firstname, lastname):
    firstletter = firstname[0].lower()
    username = firstletter+lastname.lower()
    # check if sui is already taken
    sui_isfree=False
    while(sui_isfree==False):
        if(Register.objects.all().filter(register_sui=username).count()>0):
            username=username+str(randint(0,9))
        else:
            sui_isfree=True
    return username

def generatePassword():
    all_courses = Course.objects.all()
    randomInt = randint(0, len(all_courses))
    word = Course.objects.order_by('?').first().course_name
    word=word.replace(" ", "")
    if(word.find('-')!=-1):
        password = word.split("-")[0]
    else:
        password = word

    passcode = password + str(randomInt)
    return passcode

def stripeCall(request):
	# Set your secret key: remember to change this to your live secret key in production
	# See your keys here: https://dashboard.stripe.com/account/apikeys
    checkout = getCheckoutLatest()
    stripe.api_key = checkout.private_key

    # Token is created using Stripe.js or Checkout!
    # Get the payment token submitted by the form:
    token = request.POST['stripeToken']

    # Charge the user's card:
    charge = stripe.Charge.create(
    	amount=4000,
    	currency="usd",
    	description="Example charge",
    	source=token,
    )

def confirmation_send_email(form_list, scout_id, confirmation_id):
    message = None
    scout_info=None
    emergency_info=None
    payment_timestamp=None
    form_data =[form.cleaned_data for form in form_list]
    print("sending")
    #formatting data to be transmit through the message
    scout_info = ("\n\nScout Information:\n\tScout ID: "+str(scout_id)+"\n\tScout Name: "+str(form_data[2]["first_name"])+" "+str(form_data[2]["last_name"])+"\n\tScout type: "+str(form_data[2]["affiliation"])+"\n\tUnit Number: "+str(form_data[2]["unit_number"])+"\n\nScout Contact Information:\n\tPhone Number: "+str(form_data[2]["phone"])+"\n\tEmail: "+str(form_data[2]["email"]))
    emergency_info = ("\n\nEmergency Contact:\n\tEmergency Name: "+str(form_data[2]["emergency_first_name"])+" "+str(form_data[2]["emergency_last_name"])+"\n\tEmergency Phone: "+str(form_data[2]["emergency_phone"]))
    course_info=("\n\nCourses:\n\tClass 1: "+str(form_data[3]["morning_subject"])+"\n\tClass 2: "+str(form_data[3]["evening_subject"]))
    if(str(form_data[4]["payment_method"])=="Pay_Online"):
        payment_timestamp=("\n\nPayment Method: Paid Online")
    elif(str(form_data[4]["payment_method"])=="Pay_Mail"):
        payment_timestamp=("\n\nPayment Method: Paid by Mail")
    elif(str(form_data[4]["payment_method"])=="Waived"):
        payment_timestamp=("\n\nPayment Method: Waived")
    
    
    message = "Hello "+str(form_data[1]["register_first_name"])+" "+str(form_data[1]["register_last_name"])+","+scout_info+emergency_info+"\n\n"+course_info+"\n\n"+payment_timestamp+"\n\nIf there is any information that is mistaken please contact us.\n To reprint Badge, go to Get Badge and enter your confirmation number: "+confirmation_id+"\n\nThank you,\n\t Scout Engineering Day Development Team"

    #Modify for Quantico
    #message = "Hello,"+scout_info+emergency_info+"\n\nIf there is any information that is mistaken please contact us.\n\nThank you,\n\t Scout Engineering Day Development Team"


    email = EmailMessage(
        'Confirmation Message',
        message,
        settings.EMAIL_DEFAULT_USER,
        [form_data[1]["register_email"]],
        )
    email.send(fail_silently=False)
    #send_mail(subject, message, from, to)
    # send_mail('Confirmation', str(form_data), settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], fail_silently=False)
    return form_data

def checkOpenDate():
    #Note:
    # Date must match format of (Day, Month, DayDate, Year) and date must be real or else it will states that the registration is closed.
    #
    isOpen=None
    registration_force_closed=True
    aboutPage = AboutPage.objects.latest('aboutPage_id')
    current_datetime= str(datetime.datetime.now())
    if(aboutPage.forceClosed==True):
        print("registration closed")
        isOpen="Closed"
    else:
        if(current_datetime<aboutPage.saveDate and current_datetime>=aboutPage.registrationOpenDate):
            print("registration open")
            isOpen="Opened"
        else:
            # print(current_datetime)
            # print(aboutPage.saveDate)
            # print(aboutPage.registrationOpenDate)

            # print("registration closed")
            # isOpen="Closed"
	        print("registration open")
	        isOpen="Closed"
    return isOpen

## Get Commands
# Scouts
def getScoutByUniqueScout(ScoutID, ScoutYear):
    try:
        return Scout.objects.get(scout_id=ScoutID, scout_year=ScoutYear)
    except:
        return None

def getScoutByConfirmation_id(confirmation_id):
    try:
        return Scout.objects.get(confirmation_id=confirmation_id)
    except:
        return None

# Instructor
def getInstructorbyCourse(CourseID, WorkshopTime):
    try:
        return Instructor.objects.get(instructor_id=Workshop.objects.get(course_id=CourseID, workshop_time=WorkshopTime).instructor_id)
    except:
        return None

def getInstructorByID(instructorID):
    try:
        return Instructor.objects.get(instructor_id=instructorID)
    except:
        return None

# Session
def getSessionByUniqueSession(ScoutID, ScoutYear):
    try:
        return Session.objects.get(scout_id=ScoutID, session_year=ScoutYear)
    except:
        return None

def getScoutSessionsByWorkshop(workshop_id, time):
    scouts=[]
    year=datetime.datetime.now().year
    try:
        if(time=="AM" or time=="FULL"):
            sessions = Session.objects.all().filter(workshop1_id=workshop_id, session_year=year)
            for session in sessions:
                scouts.append(Scout.objects.get(scout_id=session.scout_id))
            return scouts
        else:
            sessions = Session.objects.all().filter(workshop2_id=workshop_id, session_year=year)
            for session in sessions:
                scouts.append(Scout.objects.get(scout_id=session.scout_id))
            return scouts
    except:
        return scouts

def getCountSessionInWorkshop(workshop_id, year, time):
    try:
        if(time=="AM" or time=="FULL"):
            return Session.objects.all().filter(workshop1_id=workshop_id, session_year=year).count()
        else:
            return Session.objects.all().filter(workshop2_id=workshop_id, session_year=year).count()
    except:
        return None
# Course
def getCourseBySession(SessionWorkshopID):
    try:
        return Course.objects.get(course_id=(Workshop.objects.get(workshop_id=SessionWorkshopID).course_id))
    except:
        return None

def getCourseByID(course_id):
    try:
        return Course.objects.get(course_id=course_id)
    except:
        return None

def getLocationBySession(SessionWorkshopID):
    try:
        return Course.objects.get(course_id=course_id)
    except:
        return None

# Location
def getLocationByWorkshop(WorkshopID):
    try:
        return Location.objects.get(location_id=(Workshop.objects.get(workshop_id=WorkshopID).location_id))
    except:
        return None

def getLocationByID(location_id):
    try:
        return Location.objects.get(location_id=location_id)
    except:
        return None

def getAboutPageLatest():
    try:
        return AboutPage.objects.latest('aboutPage_id')
    except:
        return None

def getHomePageLatest():
    try:
        return HomePage.objects.latest('homepage_id')
    except:
        return None

def getCheckoutLatest():
    try:
        return Location.objects.get(location_id=(Workshop.objects.get(workshop_id=SessionWorkshopID).location_id))
    except:
        return None

def getLocationByID(location_id):
    try:
        return Location.objects.get(location_id=location_id)
    except:
        return None

class workshop_object(object):
    workshop_id= None
    course_name = None
    instructor_first_name = None
    instructor_last_name = None
    open_ceremony=None
    time_slot=None
    size=0
    location_building = None
    location_room = None
    open_status=None
    workshop_year=None

    def __init__(self,  workshop_id):
        workshop=Workshop.objects.get(workshop_id=workshop_id)
        self.workshop_id= workshop.workshop_id
        self.course_name = getCourseByID(workshop.course_id).course_name
        self.instructor_first_name =getInstructorByID(workshop.instructor_id).instructor_first_name
        self.instructor_last_name =getInstructorByID(workshop.instructor_id).instructor_last_name
        self.open_ceremony=workshop.open_ceremony
        self.workshop_time=workshop.workshop_time
        self.scouts_count=getCountSessionInWorkshop(workshop.workshop_id, workshop.workshop_year, workshop.workshop_time)
        self.workshop_size=workshop.workshop_size
        self.location_building = getLocationByWorkshop(workshop.workshop_id).location_building
        self.location_room = getLocationByWorkshop(workshop.workshop_id).location_room
        self.workshop_open_status=workshop.workshop_open_status
        self.workshop_year=workshop.workshop_year

# Workshop
def getWorkshopCustom():
    workshop_customs=[]
    for workshop in Workshop.objects.all():
        x=workshop_object(workshop.workshop_id)
        workshop_customs.append(x)
    return workshop_customs

def getWorkshopbyCourse(CourseName, WorkshopTime):
    try:
        return Workshop.objects.get(course_id=Course.objects.get(course_name=CourseName).course_id, workshop_time=WorkshopTime).workshop_id
    except:
        return None

def getOpenCeremonybyWorkshop(CourseName, WorkshopTime):
    try:
        return Workshop.objects.get(course_id=Course.objects.get(course_name=CourseName).course_id, workshop_time=WorkshopTime).open_ceremony
    except:
        return None

def WorkshopClosedTrigger(workshop_id, workshopTime):
    try:
        if(workshopTime=="AM"):
            workshop_size=Session.objects.filter(workshop1_id=workshop_id).count()
            print(workshop_size)
            if(workshop_size<Workshop.objects.get(workshop_id=workshop_id).workshop_size):
                print("there is room")
                if (workshop_size+1>=Workshop.objects.get(workshop_id=workshop_id).workshop_size):
                    workshop=Workshop.objects.get(workshop_id=workshop_id)
                    workshop.workshop_open_status="CLOSED"
                    workshop.save()
            else:
                workshop=Workshop.objects.get(workshop_id=workshop_id)
                workshop.workshop_open_status="CLOSED"
                workshop.save()
        elif(workshopTime=="PM"):
            workshop_size=Session.objects.filter(workshop2_id=workshop_id).count()
            print(workshop_size)
            if(workshop_size<Workshop.objects.get(workshop_id=workshop_id).workshop_size):
                print("there is room")
                if (workshop_size+1>=Workshop.objects.get(workshop_id=workshop_id).workshop_size):
                    workshop=Workshop.objects.get(workshop_id=workshop_id)
                    workshop.workshop_open_status="CLOSED"
                    workshop.save()
            else:
                workshop=Workshop.objects.get(workshop_id=workshop_id)
                workshop.workshop_open_status="CLOSED"
                workshop.save()
        else: #if full time
            workshop_size=Session.objects.filter(workshop1_id=workshop_id).count()
            print(workshop_size)
            if(workshop_size<Workshop.objects.get(workshop_id=workshop_id).workshop_size):
                print("there is room")
                if (workshop_size+1>=Workshop.objects.get(workshop_id=workshop_id).workshop_size):
                    workshop=Workshop.objects.get(workshop_id=workshop_id)
                    workshop.workshop_open_status="CLOSED"
                    workshop.save()
            else:
                workshop=Workshop.objects.get(workshop_id=workshop_id)
                workshop.workshop_open_status="CLOSED"
                workshop.save()
    except:
        return render_to_response('sedUI/pages/errorPage.html', status=404)

def RegistrationClosedTrigger():
    try:
        max_scout_size=1000
        aboutPage = AboutPage.objects.latest('aboutPage_id')
        if (Scout.objects.all().count()+1>=max_scout_size):
            aboutPage.forceClosed=True
            aboutPage.save()
        else:
            return HttpResponse("hit max scout size")
    except:
        return render_to_response('sedUI/pages/errorPage.html', status=404)

# Basic functions
def getAboutPageLatest():
    try:
        return AboutPage.objects.latest('aboutPage_id')
    except:
        return None

def getHomePageLatest():
    try:
        return HomePage.objects.latest('homepage_id')
    except:
        return None

def getCheckoutLatest():
    try:
        return Checkout.objects.latest('checkout_id')
    except:
        return None

def getMailPaymentLatest():
    try:
        return MailPayment.objects.latest('mailPayment_id')
    except:
        return None

def scoutlistParser(scoutlist):
    try:
        scout_id_array=[]
        scout_ids=scoutlist.split(",")
        for scout_id in scout_ids:
            scout_id_array.append(scout_id)
        return scout_id_array
    except:
        return render_to_response('sedUI/pages/errorPage.html', status=404)

def workshopMassiveCheckin(request, workshop_id, scoutlist):
    scoutarray=scoutlistParser(scoutlist)
    for scout_id in scoutarray:
        workshop_checkinW(scout_id, workshop_id)
    return HttpResponseRedirect(reverse('workshop_detail/',args=(workshop_id)))

def workshopMassiveCheckout(request, workshop_id, scoutlist):
    scoutarray=scoutlistParser(scoutlist)
    for scout_id in scoutarray:
        workshop_checkoutW(scout_id, workshop_id)
    return HttpResponseRedirect(reverse('workshop_detail/',args=(workshop_id)))

def workshopMassiveCompleted(request, workshop_id, scoutlist):
    scoutarray=scoutlistParser(scoutlist)
    for scout_id in scoutarray:
        workshop_completedW(scout_id, workshop_id)
    return HttpResponseRedirect(reverse('workshop_detail/',args=(workshop_id)))
