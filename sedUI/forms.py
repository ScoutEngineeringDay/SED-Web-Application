from django.contrib.auth.models import User
from django import forms
from .models import Course, Workshop
from django.db.models import Q
from captcha.fields import ReCaptchaField
from django.core.validators import MinValueValidator

class RegistrationForm1(forms.Form):
	citizenship = forms.ChoiceField(widget=forms.RadioSelect(), choices=[('Yes', 'Yes'),('No','No')])

class RegistrationForm2(forms.Form):
	register_first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
	register_last_name = forms.CharField(widget=forms.TextInput(attrs={'input type': 'text', 'class': 'form-control', 'id': 'last_name', 'name': 'last_name', 'placeholder': 'Last Name'}))
	register_email= forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'email'}))
	register_email_confirm = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Confirmation', 'type': 'email'}))
	mitre_employee = forms.BooleanField(initial=False, required=False)
	CHOICES = (("myself","I am registering myself"),("others","I am registering others"),("both","I am registering myself & others"))
	registration_type = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

class RegistrationScoutForm1(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'input type': 'text', 'class': 'form-control', 'id': 'last_name', 'name': 'last_name', 'placeholder': 'Last Name'}))
	affiliation = forms.ChoiceField(choices=[("BOY", "Boy Scout"),("GIRL", "Girl Scout"), ("OTHER","Other")], widget=forms.Select(attrs={'class': 'form-control'}))
	unit_number = forms.IntegerField(min_value=0, max_value=99999999, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unit Number', 'type': 'number'}))
	email= forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'email'}))
	email_confirm = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Confirmation', 'type': 'email'}))
	phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone', 'type': 'tel', 'minlength': '10', 'maxlength': '10'}), required=False) #TODO make not reqired

	emergency_first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact First Name', 'type': 'text'}))
	emergency_last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Last Name', 'type': 'text'}))
	emergency_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Phone', 'type': 'tel', 'minlength': '10', 'maxlength': '10'}))
	emergency_email= forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Email', 'type': 'email'}))
	medical_notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Medical Notes'}), required=False)
	allergy_notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Allergy Notes'}), required=False)
	medical_issues = forms.BooleanField(initial=False, required=False)
	allergy_issues = forms.BooleanField(initial=False, required=False)
	photo = forms.BooleanField(initial=True, required=False)
	# captcha = ReCaptchaField()

class RegistrationScoutForm2(forms.Form):
	morning_subject = forms.ModelChoiceField(queryset=Workshop.objects.filter((Q(workshop_time="FULL") | Q(workshop_time="AM") & Q(workshop_open_status="OPENED"))), widget=forms.Select(attrs={'class': 'dropdown'}))
	evening_subject = forms.ModelChoiceField(queryset=Workshop.objects.filter((Q(workshop_time="FULL") | Q(workshop_time="PM") & Q(workshop_open_status="OPENED"))), widget=forms.Select(attrs={'class': 'dropdown'}))

class RegistrationVolunteerForm1(forms.Form):
	volunteer_first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
	volunteer_last_name = forms.CharField(widget=forms.TextInput(attrs={'input type': 'text', 'class': 'form-control', 'id': 'last_name', 'name': 'last_name', 'placeholder': 'Last Name'}))
	volunteer_email= forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'email'}))
	volunteer_email_confirm = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Confirmation', 'type': 'email'}))
	volunteer_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone', 'type': 'tel', 'minlength': '10', 'maxlength': '10'}), required=False) #TODO make not reqired

class RegistrationVolunteerForm2(forms.Form):
	morning_subject = forms.ModelChoiceField(queryset=Workshop.objects.filter((Q(workshop_time="FULL") | Q(workshop_time="AM") & Q(workshop_open_status="OPENED"))), widget=forms.Select(attrs={'class': 'dropdown'}))
	evening_subject = forms.ModelChoiceField(queryset=Workshop.objects.filter((Q(workshop_time="FULL") | Q(workshop_time="PM") & Q(workshop_open_status="OPENED"))), widget=forms.Select(attrs={'class': 'dropdown'}))


class RegistrationPaymentForm(forms.Form):
	payment_method = forms.ChoiceField(widget=forms.RadioSelect(), choices=[("Pay_Mail","Mail in Check"),("Pay_Online","Online Payment"),("Waived","Waived")])

class ContactEmailForm(forms.Form):
	contact_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Contact Name'}))
	email_address = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email', 'size': '40'}))
	message_subject = forms.ChoiceField([("General Customer Service","General Customer Service"),("Suggestion","Suggestion"),("Product Support","Product Support"),("MITRE Employee", "MITRE Employee"), ("Volunteer","Volunteer")], widget=forms.Select(attrs={'class': 'form-control'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Message'}))
	# captcha = ReCaptchaField()

class BadgeForm(forms.Form):
	confirmation_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Confirmation ID', 'class': 'form-control input-lg'}), required=False)
	scout_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Scout ID', 'class': 'form-control input-lg'}), required=False)
