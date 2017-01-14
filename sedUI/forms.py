from django.contrib.auth.models import User
from django import forms
from .models import Course

ALL_STATES = [
	("AK", "Alaska"),
	("AL", "Alabama"),
	("AR", "Arkansas"),
	("AZ", "Arizona"),
	("CA", "California"),
	("CO", "Colorado"),
	("CT", "Connecticut"),
	("DC", "District of Columbia"),
	("DE", "Delaware"),
	("FL", "Florida"),
	("GA", "Georgia"),
	("HI", "Hawaii"),
	("IA", "Iowa"),
	("ID", "Idaho"),
	("IL", "Illinois"),
	("IN", "Indiana"),
	("KS", "Kansas"),
	("KY", "Kentucky"),
	("LA", "Louisiana"),
	("MA", "Massachusetts"),
	("MD", "Maryland"),
	("ME", "Maine"),
	("MI", "Michigan"),
	("MN", "Minnesota"),
	("MO", "Missouri"),
	("MS", "Mississippi"),
	("MT", "Montana"),
	("NC", "North Carolina"),
	("ND", "North Dakota"),
	("NE", "Nebraska"),
	("NH", "New Hampshire"),
	("NJ", "New Jersey"),
	("NM", "New Mexico"),
	("NV", "Nevada"),
	("NY", "New York"),
	("OH", "Ohio"),
	("OK", "Oklahoma"),
	("OR", "Oregon"),
	("PA", "Pennsylvania"),
	("PR", "Puerto Rico"),
	("RI", "Rhode Island"),
	("SC", "South Carolina"),
	("SD", "South Dakota"),
	("TN", "Tennessee"),
	("TX", "Texas"),
	("UT", "Utah"),
	("VA", "Virginia"),
	("VT", "Vermont"),
	("WA", "Washington"),
	("WI", "Wisconsin"),
	("WV", "West Virginia"),
	("WY", "Wyoming")
]

ALL_STATES_AND_EMPTY = [('','State')] + ALL_STATES

class RegistrationForm1(forms.Form):
	citizenship = forms.ChoiceField(widget=forms.RadioSelect(), choices=[('Yes', 'Yes'),('No','No')])

class RegistrationForm2(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'input type': 'text', 'class': 'form-control', 'id': 'last_name', 'name': 'last_name', 'placeholder': 'Last Name'}))
	affiliation = forms.ChoiceField(choices=[("GSA", "Girl Scout of America"),("BSA", "Boy Scout of America"), ("OTHER","Other")], widget=forms.Select(attrs={'class': 'form-control'}))
	troop = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Troop Number', 'type': 'number'}))
	gender = forms.ChoiceField(choices=[("F", "Female"),("M", "Male")], widget=forms.Select(attrs={'class': 'form-control'}))
	street = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street', 'type': 'text'}))
	city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City', 'type': 'text'}))
	state = forms.ChoiceField(choices=ALL_STATES_AND_EMPTY, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
	zip_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code', 'type': 'number'}))
	email= forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'email'}))
	email_confirm = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Confirmation', 'type': 'email'}))
	phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone', 'type': 'tel', 'minlength': '10', 'maxlength': '10'}))
	emergency_first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact First Name', 'type': 'text'}))
	emergency_last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Last Name', 'type': 'text'}))
	emergency_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Phone', 'type': 'tel', 'minlength': '10', 'maxlength': '10'}))

class RegistrationForm3(forms.Form):
	morning_subject = forms.ModelChoiceField(queryset=Course.objects.all().order_by('class_name'))
	evening_subject = forms.ModelChoiceField(queryset=Course.objects.all().order_by('class_name'))

class RegistrationForm4(forms.Form):
	payment_method = forms.ChoiceField(widget=forms.RadioSelect(), choices=[("Check","Mail in Check"),("OnlinePay","Online Payment")])

class ContactEmailForm(forms.Form):
	contact_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Name'}))
	email_address = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'email'}))
	message_subject = forms.ChoiceField([("General Customer Service","General Customer Service"),("Payment","Payment"),("Suggestion","Suggestion"),("Product Support","Product Support"),("Badge Request","Badge Request")], widget=forms.Select(attrs={'class': 'form-control'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}))
