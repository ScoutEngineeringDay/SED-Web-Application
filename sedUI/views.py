from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Course, Scout
import os
from django.views import generic
from django.views.generic import View
from .forms import RegistrationForm1, RegistrationForm2, RegistrationForm3, RegistrationForm4
from formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail

FORMS = [("citizenship", RegistrationForm1), 
         ("scout_info", RegistrationForm2), 
         ("selection", RegistrationForm3), 
         ("payment", RegistrationForm4)]

# TEMPLATES = {"citizenship": "sedUI/pages/registrationCitizen.html",
#                          "scout_info": "sedUI/pages/registrationInfo.html", 
#                          "selection": "sedUI/pages/registrationSelection.html", 
#                          "payment": "sedUI/pages/registrationPayment.html"}

TEMPLATES = {"citizenship": "sedUI/pages/registrationCitizen.html",
                         "scout_info": "sedUI/pages/registration_form.html", 
                         "selection": "sedUI/pages/registration_form.html", 
                         "payment": "sedUI/pages/registration_form.html"}

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

class ContactView(generic.TemplateView):
    template_name='sedUI/pages/contact.html'

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
# class ScoutQR1View(generic.):
# class ScoutQR2View(generic.):

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
    # def get_template_names(self):
    #       return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
    # email failing due to configuration error
        # form_data = process_send_email(form_list)
        print(form_list)
        # return render_to_response('sedUI/pages/registrationConfirmation.html', {'form_data': [form.cleaned_data for form in form_list]})
        return render_to_response('sedUI/pages/registration_done.html', {'form_data': [form.cleaned_data for form in form_list]})


def registration1(request):
    return render(request, 'sedUI/pages/registrationCitizen.html')

def registration2(request):
    return render(request, 'sedUI/pages/registrationInfo.html')

def registration3(request):
    all_courses = Course.objects.all()
    context = {
        'all_courses' : all_courses,
    }
    return render(request, 'sedUI/pages/registrationSelection.html', context)

def registration4(request):
    return render(request, 'sedUI/pages/registrationPayment.html')

def registration5(request):
    return render(request, 'sedUI/pages/registrationConfirmation.html')
