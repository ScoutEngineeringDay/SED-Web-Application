from django.contrib.auth.models import User
from django import forms
from .models import Course, Workshop, Task
from django.db.models import Q
from captcha.fields import ReCaptchaField
from django.core.validators import MinValueValidator
import datetime

class RegistrationForm1(forms.Form):
	citizenship = forms.ChoiceField(widget=forms.RadioSelect(), choices=[('Yes', 'Yes'),('No','No')])

class RegistrationForm2(forms.Form):
	register_first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'maxlength': '50'}))
	register_last_name = forms.CharField(widget=forms.TextInput(attrs={'input type': 'text', 'class': 'form-control', 'id': 'last_name', 'name': 'last_name', 'placeholder': 'Last Name', 'maxlength': '50'}))
	register_email= forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'email', 'maxlength': '50'}))
	register_email_confirm = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Confirmation', 'type': 'email', 'maxlength': '50'}))
	register_phone =phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number',  'type': 'tel', 'minlength': '10', 'maxlength': '10'}), required=False)
	mitre_employee = forms.BooleanField(initial=False, required=False)
	volunteer_checkbox = forms.BooleanField(initial=False, required=False)
	register_is_volunteer = forms.BooleanField(initial=True, required=False)
	# CHOICES = (("myself","I am registering myself"),("others","I am registering others"),("both","I am registering myself & others"))
	# registration_type = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

class RegistrationScoutForm1(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'maxlength': '50'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'input type': 'text', 'class': 'form-control', 'id': 'last_name', 'name': 'last_name', 'placeholder': 'Last Name', 'maxlength': '50'}))
	affiliation = forms.ChoiceField(choices=[("BOY", "Boy Scout"),("GIRL", "Girl Scout"), ("OTHER","Other")], widget=forms.Select(attrs={'class': 'form-control'}))
	unit_number = forms.IntegerField(min_value=0, max_value=9999999, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unit Number', 'type': 'number', 'min': '0', 'max': '999999', 'maxlength': '6'}))
	email= forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'email', 'maxlength': '50'}))
	email_confirm = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Confirmation', 'type': 'email', 'maxlength': '50'}))
	phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number', 'type': 'tel', 'minlength': '10', 'maxlength': '10'}), required=False)

	emergency_first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact First Name', 'type': 'text', 'maxlength': '50'}))
	emergency_last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Last Name', 'type': 'text', 'maxlength': '50'}))
	emergency_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Phone Number', 'type': 'tel', 'minlength': '10', 'maxlength': '10'}))
	emergency_email= forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Email', 'type': 'email', 'maxlength': '50'}))
	emergency_email_confirm= forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Email Confirmation', 'type': 'email', 'maxlength': '50'}))
	medical_notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Medical Notes', 'maxlength': '4000'}), required=False)
	allergy_notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Allergy Notes', 'maxlength': '4000'}), required=False)
	medical_issues = forms.BooleanField(widget=forms.CheckboxInput(attrs={'onclick':'medicalChecked()'}), initial=False, required=False)
	allergy_issues = forms.BooleanField(widget=forms.CheckboxInput(attrs={'onclick':'allergyChecked()'}), initial=False, required=False)
	photo = forms.BooleanField(initial=True, required=False)
	# captcha = ReCaptchaField()

class RegistrationScoutForm2(forms.Form):
	morning_subject = forms.ModelChoiceField(queryset=Workshop.objects.filter(((Q(workshop_time="FULL") | Q(workshop_time="AM")) & Q(workshop_open_status="OPENED") & Q(workshop_year=str(datetime.datetime.now().year)))), widget=forms.Select(attrs={'class': 'dropdown'}))
	evening_subject = forms.ModelChoiceField(queryset=Workshop.objects.filter(((Q(workshop_time="FULL")| Q(workshop_time="PM")) & Q(workshop_open_status="OPENED") & Q(workshop_year=str(datetime.datetime.now().year)))), widget=forms.Select(attrs={'class': 'dropdown'}))
	more_scout = forms.BooleanField(initial=False, required=False)

class RegistrationVolunteerForm1(forms.Form):
	volunteer_first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
	volunteer_last_name = forms.CharField(widget=forms.TextInput(attrs={'input type': 'text', 'class': 'form-control', 'id': 'last_name', 'name': 'last_name', 'placeholder': 'Last Name'}))
	volunteer_email= forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'email'}))
	volunteer_email_confirm = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Confirmation', 'type': 'email'}))
	volunteer_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone', 'type': 'tel', 'minlength': '10', 'maxlength': '10'}), required=False)

class RegistrationVolunteerForm2(forms.Form):
	volunteer_event1 = forms.ModelChoiceField(queryset=Task.objects.all(), widget=forms.Select(attrs={'class': 'dropdown'}))
	volunteer_event2 = forms.ModelChoiceField(queryset=Task.objects.all(), widget=forms.Select(attrs={'class': 'dropdown'}))
	volunteer_event3 = forms.ModelChoiceField(queryset=Task.objects.all(), widget=forms.Select(attrs={'class': 'dropdown'}))

class RegistrationPaymentForm(forms.Form):
	payment_method = forms.ChoiceField(widget=forms.RadioSelect(), choices=[("Pay_Mail","Mail in Check"),("Pay_Online","Online Payment"),("Waived","Waived")])

class ContactEmailForm(forms.Form):
	contact_first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name', 'maxlength': '50'}))
	contact_last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name', 'maxlength': '50'}))
	email_address = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email', 'size': '40', 'maxlength': '50'}))
	CHOICES = (("General Customer Service","General Customer Service"),("Suggestion","Suggestion"),("Product Support","Product Support"),("MITRE Employee", "MITRE Employee Registeration Request"), ("Volunteer","Volunteer Registration"))
	message_subject = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=CHOICES)
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Message', 'maxlength': '4000'}))
	# captcha = ReCaptchaField()

class BadgeForm(forms.Form):
	confirmation_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Confirmation ID', 'class': 'form-control input-lg'}), required=False)
	scout_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Scout ID', 'class': 'form-control input-lg'}), required=False)
