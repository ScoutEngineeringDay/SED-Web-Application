from django.db import models
from django.core.validators import RegexValidator
import hashlib
import time

def _createHash():
    """This function generate 10 character long hash"""
    hash = hashlib.sha1()
    hash.update(str(time.time()))
    return  hash.hexdigest()[:-10]

# Create your models here.
class Scout(models.Model):
	scout_id=models.AutoField(primary_key=True)
	confirmation_id=models.CharField(max_length=32, default=_createHash, unique=True)
	phone_regex = RegexValidator(regex=r'^?1?\d{9,15}$', message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed.")
	clubs_choice=(
		('BOY','BOY'),
		('GIRL','GIRL'),
		('OTHER','OTHER')
		)
	food_choice=(
		('MEAL_PLAN1','MEAL_PLAN1'),
		('MEAL_PLAN2','MEAL_PLAN2'),
		('PACKED','PACKED')
		)
	scout_status=(
		('EVENT_CHECKIN','EVENT_CHECKIN'),
		('WORKSHOP1_CHECKIN','WORKSHOP1_CHECKIN'),
		('WORKSHOP1_CHECKOUT','WORKSHOP1_CHECKOUT'),
		('WORKSHOP2_CHECKIN','WORKSHOP2_CHECKIN'),
		('WORKSHOP2_CHECKOUT','WORKSHOP2_CHECKOUT'),
		('EVENT_CHECKOUT', 'EVENT_CHECKOUT'),
		('UNDERWAY','UNDERWAY')
		)
	# scout_id=models.models.CharField(max_length=50, primary_key=True)
	# CharField(max_length=6, primary_key=True, default=pkgen)
	scout_first_name=models.CharField(max_length=50, blank=True)
	scout_last_name=models.CharField(max_length=50, blank=True)
	unit_number=models.PositiveIntegerField(default=0, blank=True)
	scout_phone = models.CharField(max_length=10, blank=True)
	scout_email=models.CharField(max_length=50, blank=True)
	emergency_first_name=models.CharField(max_length=50, blank=True)
	emergency_last_name=models.CharField(max_length=50, blank=True)
	emergency_phone=models.CharField(max_length=10, blank=True)
	emergency_email=models.CharField(max_length=50, blank=True)
	scout_type=models.CharField( max_length=6, choices=clubs_choice, blank=True)
	scout_photo = models.BooleanField(default=False)
	scout_medical = models.CharField(max_length=500, blank=True)
	scout_allergy = models.CharField(max_length=500, blank=True)
	scout_status = models.CharField( max_length=20, choices=scout_status, blank=True)
	scout_year=models.CharField(max_length=4)

	def __str__(self):
		return self.scout_first_name+" "+self.scout_last_name

	@classmethod
	def create(scout_first_name, scout_last_name, unit_number, scout_phone, emergency_first_name, emergency_last_name, emergency_phone, emergency_email, scout_type, scout_photo, scout_medical, scout_allergy):
		scout = Scout.object.create(scout_first_name, scout_last_name, unit_number, phone, emergency_first_name, emergency_last_name, emergency_phone, emergency_email, scout_type, scout_photo, scout_medical, scout_allergy)
		scout.save()
		return scout

class Course(models.Model):
	course_id=models.AutoField(primary_key=True)
	course_name=models.CharField(max_length=50)
	course_description=models.CharField(max_length=500)
	course_size=models.IntegerField()
	course_duration=models.CharField(max_length=4, choices=[("HALF","HALF"),("FULL","FULL")], blank=True)

	def __str__(self):
		return self.course_name

class Instructor(models.Model):
	instructor_id=models.AutoField(primary_key=True)
	instructor_first_name=models.CharField(max_length=50, blank=True)
	instructor_last_name=models.CharField(max_length=50, blank=True)
	instructor_email=models.CharField(max_length=50, blank=True)
	instructor_phone=models.CharField(max_length=10, blank=True)
	instructor_status=models.CharField(max_length=8, choices=[("ACTIVE","ACTIVE"),("INACTIVE","INACTIVE")], blank=True)

	def __str__(self):
		return self.instructor_first_name+" "+self.instructor_last_name

class Location(models.Model):
	location_id=models.AutoField(primary_key=True)
	location_building=models.CharField(max_length=50, blank=True)
	location_room=models.CharField(max_length=10, blank=True)
	location_capacity=models.IntegerField(default=0)

	def __str__(self):
		return self.location_building+" "+self.location_room

class Workshop(models.Model):
	workshop_id=models.AutoField(primary_key=True)
	course_id=models.CharField(max_length=10)
	open_ceremony=models.CharField(max_length=1)
	location_id=models.CharField(max_length=10)
	instructor_id=models.CharField(max_length=10)
	workshop_time=models.CharField(max_length=4, choices=[("AM","AM"),("PM","PM"),("FULL","FULL")], blank=True)
	workshop_open=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

	def __str__(self):
		try:
			return str(Course.objects.get(course_id=str(self.course_id)).course_name)+"-"+str(self.workshop_time)
		except:
			return "no course name"

	def __instructor__(self):
		try:
			return str(Instructor.objects.get(instructor_id=str(self.instructor_id)).instructor_first_name+" "+Instructor.objects.get(instructor_id=str(self.instructor_id)).instructor_last_name)
		except:
			return "No teacher"

	def __room__(self):
		try:
			return str(Location.objects.get(location_id=self.location_id).location_room)
		except:
			return "location missing"

class Session(models.Model):
	session_id=models.AutoField(primary_key=True)
	scout_id=models.CharField(max_length=10)
	payment_method=models.CharField(max_length=12, choices=[("Pay_Mail","Mail in Check"),("Pay_Online","Online Payment"),("Waived","Waived")], blank=True)
	payment_amount=models.DecimalField(max_digits=6, decimal_places=2)
	payment_status=models.CharField(max_length=8, choices=[("PAID","PAID"),("NOT PAID","NOT PAID")], blank=False)
	open_ceremony=models.CharField(max_length=1)
	workshop1_id=models.CharField(max_length=10)
	workshop1_status=models.CharField(max_length=12, choices=[("IN PROGRESS","IN PROGRESS"),("COMPLETE","COMPLETE"),("INCOMPLETE","INCOMPLETE")], blank=False)
	workshop2_id=models.CharField(max_length=10)
	workshop2_status=models.CharField(max_length=12, choices=[("IN PROGRESS","IN PROGRESS"),("COMPLETE","COMPLETE"),("INCOMPLETE","INCOMPLETE")], blank=False)
	confirmation_timestamp=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	event_checkin=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	event_checkout=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	workshop1_checkin=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	workshop1_checkout=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	workshop2_checkin=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	workshop2_checkout=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	session_year=models.CharField(max_length=4)

	def __str__(self):
		try:
			return str(Scout.objects.get(scout_id=str(self.scout_id), scout_year=self.session_year).scout_first_name)+" "+str(Scout.objects.get(scout_id=str(self.scout_id), scout_year=self.session_year).scout_last_name)
		except:
			return "Removed Scout Data: "+ str(self.session_year)

	def __workshop1__(self):
		try:
			return str(Course.objects.get(course_id=Workshop.objects.get(workshop_id=self.workshop1_id).course_id).course_name)
		except:
			return "workshop1 missing "

	def __workshop2__(self):
		try:
			return str(Course.objects.get(course_id=Workshop.objects.get(workshop_id=self.workshop2_id).course_id).course_name)
		except:
			return "workshop2 missing"

class AboutPage(models.Model):
	aboutPage_id=models.AutoField(primary_key=True)
	saveDate=models.CharField(max_length=5000)
	eventLocation=models.CharField(max_length=5000)
	registrationOpenDate=models.CharField(max_length=5000)
	registrationOpenTime=models.CharField(max_length=5000)
	locationMap=models.CharField(max_length=5000)
	forceClosed=models.BooleanField(default=False)

class HomePage(models.Model):
	homepage_id=models.AutoField(primary_key=True)
	homepage_description=models.CharField(max_length=50000000)
	homepage_news_event=models.CharField(max_length=50000000)

class Checkout(models.Model):
	checkout_id=models.AutoField(primary_key=True)
	checkout_title=models.CharField(max_length=100)
	checkout_description=models.CharField(max_length=200)
	checkout_cost=models.PositiveIntegerField()
	public_key=models.CharField(max_length=32)
	private_key=models.CharField(max_length=32)

class MailPayment(models.Model):
	states_choice=(
		('AL','AL'), ('AK','AK'), ('AZ','AZ'), ('AR','AR'), ('CA','CA'), 
		('CO','CO'), ('CT','CT'), ('DE','DE'), ('FL','FL'), ('GA','GA'), 
		('HI','HI'), ('ID','ID'), ('IL','IL'), ('IN','IN'), ('IA','IA'), 
		('KS','KS'), ('KY','KY'), ('LA','LA'), ('ME','ME'), ('MD','MD'), 
		('MA','MA'), ('MI','MI'), ('MN','MN'), ('MS','MS'), ('MO','MO'), 
		('MT','MT'), ('NE','NE'), ('NV','NV'), ('NH','NH'), ('NJ','NJ'), 
		('NM','NM'), ('NY','NY'), ('NC','NC'), ('ND','ND'), ('OH','OH'), 
		('OK','OK'), ('OR','OR'), ('PA','PA'), ('RI','RI'), ('SC','SC'), 
		('SD','SD'), ('TN','TN'), ('TX','TX'), ('UT','UT'), ('VT','VT'), 
		('VA','VA'), ('WA','WA'), ('WV','WV'), ('WI','WI'), ('WY','WY'))
	
	mailPayment_id = models.AutoField(primary_key=True)
	mailPayment_person = models.CharField(max_length=100)
	mailPayment_building = models.CharField(max_length=50)
	mailPayment_street = models.CharField(max_length=50)
	mailPayment_city = models.CharField(max_length=50)
	mailPayment_state = models.CharField(max_length=2, choices=states_choice, blank=True)
	mailPayment_zip = models.CharField(max_length=6)
	mailPayment_due_date = models.CharField(max_length=8)


	def __payment_person__(self):
		return self.mailPayment_person
	def __payment_address__(self):
		return self.mailPayment_building+" "+self.mailPayment_street+", "+self.mailPayment_city+", "+self.mailPayment_state+", "+self.mailPayment_zip 
	def __payment_due_date__(self):
		return self.mailPayment_due_date

#
# Deffered for this interation
#
# class Volunteer2(models.Model):
# 	volunteer_id=models.AutoField(primary_key=True)
# 	volunteer_first_name=models.CharField(max_length=50, blank=True)
# 	volunteer_last_name=models.CharField(max_length=50, blank=True)
# 	volunteer_email=models.CharField(max_length=50, blank=True)
# 	volunteer_phone=models.CharField(max_length=10, blank=True)
# 	volunteer_area=models.CharField(max_length=5000, blank=True)
# 	volunteer_status=models.CharField(max_length=8, choices=[("ACTIVE","ACTIVE"),("INACTIVE","INACTIVE")], blank=True)

# 	def __str__(self):
# 		return self.volunteer_first_name+" "+self.volunteer_last_name