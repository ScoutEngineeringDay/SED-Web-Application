from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import Http404
from .models import Course, Scout

# Create your views here.
def index(request):
    return render(request, 'sedUI/pages/index.html')

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
    c = {}
    c.update(csrf(request))
    return render_to_response('sedUI/pages/loginOrRegister.html', c)

def auth(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/loginOrRegister')

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
    return render(request, 'sedUI/pages/about.html')
