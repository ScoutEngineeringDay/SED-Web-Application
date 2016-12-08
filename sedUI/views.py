from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import Http404
from .models import Course, Scout
import os

# Create your views here.
def index(request):
    img_fileNames = []
    #Add first image
    img_fileNames.append(os.path.join('img/images/', '00001.jpg'))
    # for filename in os.listdir("sed/sedUI/static/img/homeImages"):    # Use if running on AWS Server
    for filename in os.listdir("sedUI/static/img/homeImages"):          # Use if running on Local Machine
        img_fileNames.append(os.path.join('img/homeImages/', filename))
    return render(request, 'sedUI/pages/index.html', {"fileNames" : img_fileNames})

def contact(request):
    return render(request, 'sedUI/pages/contact.html')

def login(request):
    return render(request, 'sedUI/pages/basic.html')

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

def loginOrRegister(request):
    return render(request, 'sedUI/pages/loginOrRegister.html')

def courses(request):
    all_courses = Course.objects.all()
    context = {
        'all_courses' : all_courses,
    }
    return render(request, 'sedUI/pages/courses.html', context)

def scouts(request):
    all_scouts = Scout.objects.all()
    context = {
        'all_scouts' : all_scouts,
    }
    return render(request, 'sedUI/pages/scouts.html', context)

def reportAnalysis(request):
    return render(request, 'sedUI/pages/reportAnalysis.html')

def profile(request):
    return render(request, 'sedUI/pages/profile.html')

def about(request):
    all_courses = Course.objects.all()
    context = {
        'all_courses' : all_courses,
    }
    left_items = all_courses[:(len(all_courses)+1)/2]
    right_items = all_courses[(len(all_courses)+1)/2:]
    context = {
        'all_courses' : all_courses,
        'left_items' : left_items,
        'right_items' : right_items,
    }
    return render(request, 'sedUI/pages/about.html', context)
