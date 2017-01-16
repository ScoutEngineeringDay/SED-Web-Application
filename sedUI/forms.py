from django.contrib.auth.models import User
from django import forms
from .models import Course

class RegistrationForm1(forms.Form):
	citizenship = forms.ChoiceField(widget=forms.RadioSelect(), choices=[('Yes', 'Yes'),('No','No')])

class RegistrationForm2(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'input type': 'text', 'class': 'form-control', 'id': 'last_name', 'name': 'last_name', 'placeholder': 'Last Name'}))
	affiliation = forms.ChoiceField(choices=[("GSA", "Girl Scout of America"),("BSA", "Boy Scout of America"), ("OTHER","Other")], widget=forms.Select(attrs={'class': 'form-control'}))
	unit_number = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unit Number', 'type': 'number'}))
	gender = forms.ChoiceField(choices=[("F", "Female"),("M", "Male")], widget=forms.Select(attrs={'class': 'form-control'}))
	#street = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street', 'type': 'text'}))
	#city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City', 'type': 'text'}))
	#state = forms.ChoiceField(choices=ALL_STATES_AND_EMPTY, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
	#zip_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code', 'type': 'number'}))
	email= forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'email'}))
	email_confirm = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Confirmation', 'type': 'email'}))
	phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone', 'type': 'tel', 'minlength': '10', 'maxlength': '10'})) #TODO make not reqired

	emergency_first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact First Name', 'type': 'text'}))
	emergency_last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Last Name', 'type': 'text'}))
	emergency_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Phone', 'type': 'tel', 'minlength': '10', 'maxlength': '10'}))
	medical_issues = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Medical Notes'}))
	allergy_issues = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Allergy Notes'}))
	medical_notes = forms.BooleanField()
	allergy_notes = forms.BooleanField()
	photo = forms.BooleanField()

class RegistrationForm3(forms.Form):
	medical_issues = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Medical Notes'}))
	allergy_issues = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Allergy Notes'}))

class RegistrationForm4(forms.Form):
	morning_subject = forms.ModelChoiceField(queryset=Course.objects.all().order_by('class_name'))
	evening_subject = forms.ModelChoiceField(queryset=Course.objects.all().order_by('class_name'))
class RegistrationForm4(forms.Form):
	payment_method = forms.ChoiceField(widget=forms.RadioSelect(), choices=[("Pay_Mail","Mail in Check"),("Pay_Online","Online Payment")])
	# Registration_timestamp = forms.DateField(auto_now=True, auto_now_add=True)

class ContactEmailForm(forms.Form):
	contact_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Name'}))
	email_address = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'email'}))
	message_subject = forms.ChoiceField([("General Customer Service","General Customer Service"),("Payment","Payment"),("Suggestion","Suggestion"),("Product Support","Product Support"),("Badge Request","Badge Request")], widget=forms.Select(attrs={'class': 'form-control'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}))
