from django.contrib.auth.models import User
from django import forms
from .models import Course

class RegistrationForm1(forms.Form):
	citizenship = forms.ChoiceField(widget=forms.RadioSelect(), choices=[('Yes', 'Yes'),('No','No')])

class RegistrationForm2(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'size': '40'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'size': '40'}))
	affiliation = forms.ChoiceField(choices=[("GSA", "Girl Scout of America"),("BSA", "Boy Scout of America"), ("Venture Crew","Venture Crew")])
	age = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Age', 'size': '40'}))
	gender = forms.ChoiceField(choices=[("F", "Female"),("M", "Male")])
	street = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Street', 'size': '40'}))
	city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City', 'size': '40'}))
	state = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'State', 'size': '40'}))
	zip_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Zip Code', 'size': '40'}))
	email= forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'size': '40'}))
	email_confirm = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Confirmation', 'size': '40'}))
	phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone', 'size': '40'}))
	emergency_first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Emergency Contact First Name', 'size': '40'}))
	emergency_last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Emergency Contact Last Name', 'size': '40'}))
	emergency_phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Emergency Contact Phone', 'size': '40'}))

class RegistrationForm3(forms.Form):
	morning_subject = forms.ModelChoiceField(queryset=Course.objects.all().order_by('class_name'))
	evening_subject = forms.ModelChoiceField(queryset=Course.objects.all().order_by('class_name'))

class RegistrationForm4(forms.Form):
	payment_method = forms.ChoiceField(widget=forms.RadioSelect(), choices=[("Check","Mail in Check"),("OnlinePay","Online Payment")])

class ContactEmailForm(forms.Form):
	contact_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Contact Name'}))
	email_address = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'size': '40'}))
	message_subject = forms.ChoiceField([("General Customer Service","General Customer Service"),("Suggestion","Suggestion"),("Product Support","Product Support")])
	message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}))