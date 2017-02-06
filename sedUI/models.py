from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Scout(models.Model):
	scout_id=models.AutoField(primary_key=True)
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
	unit_number=models.IntegerField(default=0, blank=True)
	scout_phone = models.CharField(max_length=10, blank=True)
	scout_email=models.CharField(max_length=50, blank=True)
	emergency_first_name=models.CharField(max_length=50, blank=True)
	emergency_last_name=models.CharField(max_length=50, blank=True)
	emergency_phone=models.CharField(max_length=10, blank=True)
	emergency_email=models.CharField(max_length=50, blank=True)
	scout_type=models.CharField( max_length=6, choices=clubs_choice, blank=True)
	scout_food = models.CharField( max_length=10, choices=food_choice, blank=True)
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
	location_id=models.CharField(max_length=10)
	instructor_id=models.CharField(max_length=10)
	workshop_time=models.CharField(max_length=4, choices=[("AM","AM"),("PM","PM"),("FULL","FULL")], blank=True)
	workshop_open=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

	def __str__(self):
		return str(Course.objects.get(course_id=str(self.course_id)).course_name)+"-"+str(self.workshop_time)

	def __instructor__(self):
		return str(Instructor.objects.get(instructor_id=str(self.instructor_id)).instructor_first_name+" "+Instructor.objects.get(instructor_id=str(self.instructor_id)).instructor_last_name)

class Session(models.Model):
	session_id=models.AutoField(primary_key=True)
	scout_id=models.CharField(max_length=10)
	payment_method=models.CharField(max_length=12, choices=[("Pay_Mail","Mail in Check"),("Pay_Online","Online Payment")], blank=True)
	payment_amount=models.DecimalField(max_digits=6, decimal_places=2)
	workshop1_id=models.CharField(max_length=10)
	workshop1_status=models.CharField(max_length=12, choices=[("COMPLETE","COMPLETE"),("INCOMPLETE","INCOMPLETE"),("IN PROGRESS","IN PROGRESS")], default="IN PROGRESS", blank=False)
	workshop2_id=models.CharField(max_length=10)
	workshop2_status=models.CharField(max_length=12, choices=[("COMPLETE","COMPLETE"),("INCOMPLETE","INCOMPLETE"),("IN PROGRESS","IN PROGRESS")], default="IN PROGRESS", blank=False)
	confirmation_timestamp=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	event_checkin=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	event_checkout=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	workshop1_checkin=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	workshop1_checkout=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	workshop2_checkin=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	workshop2_checkout=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	session_year=models.CharField(max_length=4)

	def __str__(self):
		return str(Scout.objects.get(scout_id=str(self.scout_id)).scout_first_name)+" "+str(Scout.objects.get(scout_id=str(self.scout_id)).scout_last_name)

class AboutPage(models.Model):
	aboutPage_id=models.AutoField(primary_key=True)
	saveDate=models.CharField(max_length=5000)
	eventLocation=models.CharField(max_length=5000)
	registrationOpenDate=models.CharField(max_length=5000)
	registrationOpenTime=models.CharField(max_length=5000)
	locationMap=models.CharField(max_length=5000)

class HomePage(models.Model):
	homepage_id=models.AutoField(primary_key=True)
	homepage_description=models.CharField(max_length=50000000)
	homepage_news_event=models.CharField(max_length=50000000)



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