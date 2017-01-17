from django.shortcuts import render, render_to_response, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Course, Scout
import os
from django.views import generic
from django.core.urlresolvers import reverse
from django.views.generic import View
from .forms import RegistrationForm1, RegistrationForm2, RegistrationForm3, RegistrationForm4, ContactEmailForm
from formtools.wizard.views import WizardView
from formtools.wizard.views import SessionWizardView, CookieWizardView

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage

FORMS = [("citizenship", RegistrationForm1),
         ("scout_info", RegistrationForm2),
         ("selection", RegistrationForm3),
         ("payment", RegistrationForm4)]

# Create your views here.
class IndexView(generic.TemplateView):
  template_name='sedUI/pages/index.html'
  def get(self, request, *args, **kwargs):
    img_fileNames = []
    #Add first image
    img_fileNames.append(os.path.join('img/images/', '00001.jpg'))
    # for filename in os.listdir("sed/sedUI/static/img/homeImages"):    # Use if running on AWS Server
    for filename in os.listdir("sedUI/static/img/homeImages"):          # Use if running on Local Machine
        img_fileNames.append(os.path.join('img/homeImages/', filename))
    return render(request, 'sedUI/pages/index.html', {"fileNames" : img_fileNames})

class ContactView(SessionWizardView):
    form_list=[ContactEmailForm]
    template_name = 'sedUI/pages/contact.html'

    def done(self, form_list, **kwargs):
        print("send")
        contact_send_email(form_list)
        return render_to_response('sedUI/pages/registration_done.html', {'form_data': [form.cleaned_data for form in form_list]})

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
    context_object_name='course'
    def get_queryset(self):
        return Course.objects.get(class_id=self.kwargs['class_id'])

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

class ReportView(generic.TemplateView):
    template_name = 'sedUI/pages/reportAnalysis.html'


class ProfileView(generic.TemplateView):
    template_name = 'sedUI/pages/profile.html'

class AboutView(generic.TemplateView):
    template_name='sedUI/pages/about.html'
    # context_object_name = 'all_courses'
    def get(self, request, *args, **kwargs):
        all_courses = Course.objects.all()
        left_items = all_courses[:(len(all_courses)+1)/2]
        right_items = all_courses[(len(all_courses)+1)/2:]
        context = {
            'all_courses' : all_courses,
            'left_items' : left_items,
            'right_items' : right_items,
        }
    	return render(request, 'sedUI/pages/about.html', context);

class RegistrationWizard(SessionWizardView):
    form_list = [RegistrationForm1, RegistrationForm2, RegistrationForm3, RegistrationForm4]
    template_name = 'sedUI/pages/registration_form.html'

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
                return redirect(reverse('index'))

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
        scout_data=self.get_cleaned_data_for_step('1')
        scout = Scout(first_name=scout_data["first_name"],
            last_name=scout_data["last_name"], 
            unit_number=scout_data["unit_number"],
            phone=scout_data["phone"], 
            emergency_first_name=scout_data["emergency_first_name"],
            emergency_last_name=scout_data["emergency_last_name"], 
            emergency_phone=scout_data["emergency_phone"], 
            emergency_email=scout_data["emergency_email"], 
            affiliation=scout_data["affiliation"], 
            photo=scout_data["photo"], 
            medical_notes=scout_data["medical_notes"], 
            allergy_notes=scout_data["allergy_notes"])
        scout.save()
        workshop_data=self.get_cleaned_data_for_step('2')
        # generate_Workshop(workshop_data)
        # form_data = confirmation_send_email(form_list)
        return render_to_response('sedUI/pages/registrationConfirmation.html', {'form_data': [form.cleaned_data for form in form_list]})


def confirmation_send_email(form_list):
    message = None
    scout_info=None
    emergency_info=None
    payment_timestamp=None
    form_data =[form.cleaned_data for form in form_list]
    print("sending")
    #formatting data to be transmit through the message
    scout_info = ("\n\nScout Information:\n\tScout Name: "+str(form_data[1]["first_name"])+" "+str(form_data[1]["last_name"])+"\n\tOrganization: "+str(form_data[1]["affiliation"])+"\n\tTroop#:"+str(form_data[1]["unit_number"])+"\n\nScout Contact Information:\n\tPhone Number: "+str(form_data[1]["phone"])+"\n\tEmail: "+str(form_data[1]["email"]))
    emergency_info = ("\n\nEmergency Contact:\n\tEmergency Name:"+str(form_data[1]["emergency_first_name"])+" "+str(form_data[1]["emergency_last_name"])+"\n\tEmergency Phone: "+str(form_data[1]["emergency_phone"]))
    # course_info=("\n\nCourses:\tClass 1:"+form_data[2]["morning_subject"]+"\tClass 2:"+form_data[2]["evening_subject"])
    payment_timestamp=("\n\nPayment Method: "+str(form_data[3]["payment_method"])+"\n\nTimeStamp: ")
    message = "Hello,"+scout_info+emergency_info+payment_timestamp+"\n\nIf there is any information that is mistaken please contact us.\n\nThank you,\n\t Scout Engineering Day Development Team"


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
