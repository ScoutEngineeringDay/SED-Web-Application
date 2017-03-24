from django.shortcuts import render, render_to_response, redirect, HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Course, Scout, Workshop, Session, Instructor, AboutPage, HomePage, Checkout, MailPayment, Location
import os
from django.views import generic
from django.core.urlresolvers import reverse
from django.views.generic import View
from .forms import RegistrationForm1, RegistrationForm2, RegistrationForm3, RegistrationForm4, ContactEmailForm, BadgeForm
from formtools.wizard.views import WizardView
from formtools.wizard.views import SessionWizardView, CookieWizardView
import datetime
import re
import pytz
import stripe
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.core.management.utils import get_random_secret_key

FORMS = [("citizenship", RegistrationForm1),
         ("scout_info", RegistrationForm2),
         ("selection", RegistrationForm3),
         ("payment", RegistrationForm4)]

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

class RegistrationIssueView(generic.TemplateView):
    template_name = 'sedUI/pages/registrationIssue.html'

class ContactConfirmationView(generic.TemplateView):
    template_name = 'sedUI/pages/contactConfirmation.html'

class ContactView(SessionWizardView):
    form_list=[ContactEmailForm]
    template_name = 'sedUI/pages/contact.html'

    def done(self, form_list, **kwargs):
        print("send")
        contact_send_email(form_list)
        return render_to_response('sedUI/pages/contactConfirmation.html', {'form_data': [form.cleaned_data for form in form_list]})

def contact_send_email(form_list):
    form_data =[form.cleaned_data for form in form_list]
    message=("Contact Email: "+ form_data[0]["email_address"]+"\n\nContact name: "+form_data[0]["contact_name"]+"\n\nMessage:\n"+form_data[0]["message"])
    #send_mail(subject, message, from, to)
    send_mail(form_data[0]["message_subject"], message, form_data[0]["email_address"], [settings.EMAIL_HOST_USER], fail_silently=False)
    return form_data

def login(request):
    return render(request, 'sedUI/pages/basic.html')

def loginOrRegister(request):
    return render(request, 'sedUI/pages/loginOrRegister.html')

class CourseView(generic.ListView):
    template_name = 'sedUI/pages/courses.html'
    context_object_name = 'all_courses'
    def get_queryset(self):
        return Course.objects.all()

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
        if(scout.scout_status=="UNDERWAY" or scout.scout_status=='EVENT_CHECKOUT'):
            scout.scout_status='EVENT_CHECKIN'
            scout.save()
            session=getSessionByUniqueSession(scout_id, scout.scout_year)
            session.event_checkin=datetime.datetime.now()
            session.save()
            return HttpResponseRedirect(reverse('scout_detail/', args=(scout_id,)))
            #add checkin check
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
    try:
        scout=getScoutByUniqueScout(scout_id, datetime.datetime.now().year)
        session=getSessionByUniqueSession(scout_id, scout.scout_year)
        if(scout.scout_status=='EVENT_CHECKIN'):
            scout.scout_status='WORKSHOP1_CHECKIN'
            scout.save()
            session.workshop1_status='IN PROGRESS'
            session.workshop1_checkin=datetime.datetime.now()
            session.save()
            return HttpResponseRedirect(reverse('scout_detail/', args=(scout_id,)))
        elif(scout.scout_status=='WORKSHOP1_CHECKOUT' and session.workshop2_id != '0'):
            scout.scout_status='WORKSHOP2_CHECKIN'
            scout.save()
            session.workshop2_status='IN PROGRESS'
            session.workshop2_checkin=datetime.datetime.now()
            session.save()
            return HttpResponseRedirect(reverse('scout_detail/', args=(scout_id,)))
        else:
            return render_to_response('sedUI/pages/errorPage.html', status=404)
    except:
        return render_to_response('sedUI/pages/errorPage.html', status=404)

def workshop_completed(request, scout_id):
    try:
        scout=getScoutByUniqueScout(scout_id, datetime.datetime.now().year)
        session=getSessionByUniqueSession(scout_id, scout.scout_year)
        if(scout.scout_status=='WORKSHOP1_CHECKIN'):
            scout.scout_status='WORKSHOP1_CHECKOUT'
            scout.save()
            session.workshop1_status="COMPLETE"
            session.workshop1_checkout=datetime.datetime.now()
            session.save()
            return HttpResponseRedirect(reverse('scout_detail/', args=(scout_id,)))
        elif(scout.scout_status=='WORKSHOP2_CHECKIN'):
            scout.scout_status='WORKSHOP2_CHECKOUT'
            scout.save()
            session.workshop2_status="COMPLETE"
            session.workshop2_checkout=datetime.datetime.now()
            session.save()
            return HttpResponseRedirect(reverse('scout_detail/', args=(scout_id,)))
        else:
            return render_to_response('sedUI/pages/errorPage.html', status=404)
    except:
        return render_to_response('sedUI/pages/errorPage.html', status=404)

def workshop_checkout(request, scout_id):
    try:
        scout=getScoutByUniqueScout(scout_id, datetime.datetime.now().year)
        session=getSessionByUniqueSession(scout_id, scout.scout_year)
        if(scout.scout_status=='WORKSHOP1_CHECKIN'):
            scout.scout_status='WORKSHOP1_CHECKOUT'
            scout.save()
            session.workshop1_status="INCOMPLETE"
            session.workshop1_checkout=datetime.datetime.now()
            session.save()
            return HttpResponseRedirect(reverse('scout_detail/', args=(scout_id,)))
        elif(scout.scout_status=='WORKSHOP2_CHECKIN'):
            scout.scout_status='WORKSHOP2_CHECKOUT'
            scout.save()
            session.workshop2_status="INCOMPLETE"
            session.workshop2_checkout=datetime.datetime.now()
            session.save()
            return HttpResponseRedirect(reverse('scout_detail/', args=(scout_id,)))
        else:
            return render_to_response('sedUI/pages/errorPage.html', status=404)
    except:
        return render_to_response('sedUI/pages/errorPage.html', status=404)

class ReportView(generic.TemplateView):
    template_name = 'sedUI/pages/reportAnalysis.html'

class ProfileView(generic.TemplateView):
    template_name = 'sedUI/pages/profile.html'

class AboutView(generic.TemplateView):
    template_name='sedUI/pages/about.html'
    # context_object_name = 'all_courses'
    def get(self, request, *args, **kwargs):
    	aboutPage = getAboutPageLatest()
        all_courses = Course.objects.all()
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
    	return render(request, 'sedUI/pages/about.html', context);

class BadgeView(SessionWizardView):
    form_list=[BadgeForm]
    template_name = 'sedUI/pages/getBadge.html'

    def done(self, form_list, **kwargs):
        form_data=self.get_cleaned_data_for_step('0')
        confirmation_id=form_data["confirmation_id"]
        try:
            scout_data=getScoutByConfirmation_id(confirmation_id)
            session_data=getSessionByUniqueSession(scout_data.scout_id, scout_data.scout_year)
            course_1=getCourseBySession(session_data.workshop1_id)
            location_1=getLocationBySession(session_data.workshop1_id)
            if(session_data.workshop2_id!='0' or session_data.workshop2_id!=None):
                course_2=getCourseBySession(session_data.workshop2_id)
                location_2=getLocationBySession(session_data.workshop2_id)
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
           location_1=getLocationBySession(session_data.workshop1_id)
           location_2=getLocationBySession(session_data.workshop2_id)
           workshop_1=getCourseBySession(session_data.workshop1_id)
           workshop_2=getCourseBySession(session_data.workshop2_id)
           try:
             workshop_1_data=str(workshop_1.course_name)+" - "+str(location_1.location_room)
           except:
             workshop_2_data=" "
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

class RegistrationWizard(SessionWizardView):
    form_list = [RegistrationForm1, RegistrationForm2, RegistrationForm3, RegistrationForm4]
    template_name = 'sedUI/pages/registration_form.html'

    def get_context_data(self, **kwargs):
        ctx=super(RegistrationWizard, self).get_context_data(**kwargs)
        try:
            ctx['isOpen']=checkOpenDate()
            ctx['payment']=getMailPaymentLatest()
            ctx['checkout']=getCheckoutLatest()
        except:
            ctx['isOpen']=checkOpenDate()
            ctx['payment']=None
            ctx['checkout']=None
        return ctx

    def render(self, form=None, **kwargs):
        form = form or self.get_form()
        if self.steps.current=='3':
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

    def done(self, form_list, **kwargs):
        course_1=None
        course_2=None
        scout_data=self.get_cleaned_data_for_step('1')
        workshop_data=self.get_cleaned_data_for_step('2')
        session_data=self.get_cleaned_data_for_step('3')

        if(session_data["payment_method"]=="Pay_Online"):
        	stripeCall(self.request)

        # store into database scout table
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
        if(session_data["payment_method"]=="Waived"):
            payment_status_info="PAID"
        elif(session_data["payment_method"]=="Pay_Online"):
            payment_status_info="PAID"
        else:
            payment_status_info="NOT PAID"
        if(workshop1_data[1]=="FULL"):
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
            location_1=getLocationBySession(session.workshop1_id)
            location_2=None
        else:
            #if there is a PM CLass
            workshop2_data=None
            if(workshop_data["evening_subject"]!=None):
                workshop2_data=str(workshop_data["evening_subject"]).split('-')
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
                location_1=getLocationBySession(session.workshop1_id)
                location_2=getLocationBySession(session.workshop2_id)
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
                location_1=getLocationBySession(session.workshop1_id)
                location_2=None
        all_models_dict ={
        	'form_data': [form.cleaned_data for form in form_list],
    		'scout': scout,
    		'session': session,
    		'workshop_1': course_1,
            'workshop_2': course_2,
            'location_1': location_1,
            'location_2': location_2
        }
        confirmation_timestamp=session.confirmation_timestamp
        confirmation_send_email(form_list, scout.scout_id, str(scout.confirmation_id))
        return render_to_response('sedUI/pages/registrationConfirmation.html', {'form_data': [form.cleaned_data for form in form_list],
    		'scout': scout,
    		'session': session,
    		'workshop_1': course_1,
            'workshop_2': course_2,
            'location_1': location_1,
            'location_2': location_2
        	})

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
    scout_info = ("\n\nScout Information:\n\tScout ID: "+str(scout_id)+"\n\tScout Name: "+str(form_data[1]["first_name"])+" "+str(form_data[1]["last_name"])+"\n\tScout type: "+str(form_data[1]["affiliation"])+"\n\tUnit Number:"+str(form_data[1]["unit_number"])+"\n\nScout Contact Information:\n\tPhone Number: "+str(form_data[1]["phone"])+"\n\tEmail: "+str(form_data[1]["email"]))
    emergency_info = ("\n\nEmergency Contact:\n\tEmergency Name:"+str(form_data[1]["emergency_first_name"])+" "+str(form_data[1]["emergency_last_name"])+"\n\tEmergency Phone: "+str(form_data[1]["emergency_phone"]))
    # course_info=("\n\nCourses:\tClass 1:"+form_data[2]["morning_subject"]+"\tClass 2:"+form_data[2]["evening_subject"])
    payment_timestamp=("\n\nPayment Method: "+str(form_data[3]["payment_method"]))
    message = "Hello,"+scout_info+emergency_info+payment_timestamp+"\n\nIf there is any information that is mistaken please contact us.\n To reprint Badge, go to Get Badge and enter your confirmation number: "+confirmation_id+"\n\nThank you,\n\t Scout Engineering Day Development Team"


    email = EmailMessage(
        'Confirmation Message',
        message,
        settings.EMAIL_HOST_USER,
        [form_data[1]["email"]],
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
        print("registration forced closed")
        isOpen="ForcedClosed"
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
	        isOpen="Opened"
    return isOpen

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

def getInstructorbyCourse(CourseID, WorkshopTime):
    try:
        return Instructor.objects.get(instructor_id=Workshop.objects.get(course_id=CourseID, workshop_time=WorkshopTime).instructor_id)
    except:
        return None

def getSessionByUniqueSession(ScoutID, ScoutYear):
    try:
        return Session.objects.get(scout_id=ScoutID, session_year=ScoutYear)
    except:
        return None

def getCourseBySession(SessionWorkshopID):
    try:
        return Course.objects.get(course_id=(Workshop.objects.get(workshop_id=SessionWorkshopID).course_id))
    except:
        return None

def getLocationBySession(SessionWorkshopID):
    try:
        return Location.objects.get(location_id=(Workshop.objects.get(workshop_id=SessionWorkshopID).location_id))
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
        return Checkout.objects.latest('checkout_id')
    except:
        return None

def getMailPaymentLatest():
    try:
        return MailPayment.objects.latest('mailPayment_id')
    except:
        return None

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