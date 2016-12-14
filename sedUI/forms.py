from django.contrib.auth.models import User
from django import forms
from .models import Course

class RegistrationForm1(forms.Form):
	citizenship = forms.ChoiceField(widget=forms.RadioSelect, choices=(('y', 'Yes'),('n','No')))

class RegistrationForm2(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	affiliation = forms.ChoiceField(choices=[("GSA", "Girl Scout of America")]+[("BSA", "Boy Scout of America")])
	age = forms.IntegerField()
	gender = forms.ChoiceField(choices=[("F", "Female")]+[("M", "Male")])
	street = forms.CharField()
	city = forms.CharField()
	state = forms.CharField()
	zip_code = forms.CharField()
	email= forms.CharField()
	email_confirm = forms.CharField()
	phone = forms.CharField()
	emergency_first_name = forms.CharField()
	emergency_last_name = forms.CharField()
	emergency_phone = forms.CharField()

class RegistrationForm3(forms.Form):
	morning_subject = forms.ModelChoiceField(queryset=Course.objects.all().order_by('class_name'))
	evening_subject = forms.ModelChoiceField(queryset=Course.objects.all().order_by('class_name'))

class RegistrationForm4(forms.Form):
	payment_method = forms.CharField()

# class ContactEmail(forms.Form):
