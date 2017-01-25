from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Scout2(models.Model):
	scout_id=models.AutoField(primary_key=True)
	phone_regex = RegexValidator(regex=r'^?1?\d{9,15}$', message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed.")
	clubs_choice=(
		('BSA','Boy Scouts of America'),
		('GSA','Girl Scouts of America'),
		('Others','Others')
		)
	food_choice=(
		('MEAL_PLAN1','MEAL_PLAN1'),
		('MEAL_PLAN2','MEAL_PLAN2'),
		('PACKED','PACKED')
		)
	# scout_id=models.models.CharField(max_length=50, primary_key=True)
	# CharField(max_length=6, primary_key=True, default=pkgen)
	scout_first_name=models.CharField(max_length=50, blank=True)
	scout_last_name=models.CharField(max_length=50, blank=True)
	troop_number=models.IntegerField(default=0, blank=True)
	scout_phone = models.CharField(max_length=10, blank=True)
	scout_email=models.CharField(max_length=50, blank=True)
	emergency_first_name=models.CharField(max_length=50, blank=True)
	emergency_last_name=models.CharField(max_length=50, blank=True)
	emergency_phone=models.CharField(max_length=10, blank=True)
	emergency_email=models.CharField(max_length=50, blank=True)
	organization=models.CharField( max_length=6, choices=clubs_choice, blank=True)
	scout_food = models.CharField( max_length=10, choices=food_choice, blank=True)
	scout_photo = models.BooleanField(default=False)
	scout_medical = models.CharField(max_length=500, blank=True)
	scout_allergy = models.CharField(max_length=500, blank=True)

	def __str__(self):
		return self.scout_first_name+" "+self.scout_last_name

	@classmethod
	def create(scout_first_name, scout_last_name, troop_number, scout_phone, emergency_first_name, emergency_last_name, emergency_phone, emergency_email, organization, scout_photo, scout_medical, scout_allergy):
		scout = Scout2.object.create(scout_first_name, scout_last_name, troop_number, phone, emergency_first_name, emergency_last_name, emergency_phone, emergency_email, organization, scout_photo, scout_medical, scout_allergy)
		scout.save()
		return scout



class Course2(models.Model):
	course_id=models.AutoField(primary_key=True)
	course_name=models.CharField(max_length=50)
	instructor_id=models.CharField(max_length=10)
	course_description=models.CharField(max_length=500)
	course_size=models.IntegerField()

	def __str__(self):
		return self.course_name

class Instructor2(models.Model):
	instructor_id=models.AutoField(primary_key=True)
	instructor_first_name=models.CharField(max_length=50, blank=True)
	instructor_last_name=models.CharField(max_length=50, blank=True)
	instructor_email=models.CharField(max_length=50, blank=True)
	instructor_phone=models.CharField(max_length=10, blank=True)
	instructor_status=models.CharField(max_length=8, choices=[("ACTIVE","ACTIVE"),("INACTIVE","INACTIVE")], blank=True)

	def __str__(self):
		return self.instructor_first_name+" "+self.instructor_last_name

class Location2(models.Model):
	location_id=models.AutoField(primary_key=True)
	location_building=models.CharField(max_length=50, blank=True)
	location_room=models.CharField(max_length=10, blank=True)
	location_capacity=models.IntegerField(default=0)

	def __str__(self):
		return self.location_building+" "+self.location_room

class Workshop2(models.Model):
	workshop_id=models.AutoField(primary_key=True)
	course_id=models.CharField(max_length=10)
	location_id=models.CharField(max_length=10)
	workshop_time=models.CharField(max_length=4, choices=[("AM","AM"),("PM","PM"),("FULL","FULL")], blank=True)
	workshop_open=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

	def __str__(self):
		return str(Course2.objects.get(course_id=str(self.course_id)).course_name)+"("+str(self.workshop_open)+")"

class Session2(models.Model):
	session_id=models.AutoField(primary_key=True)
	scout_id=models.CharField(max_length=10)
	payment_method=models.CharField(max_length=12, choices=[("Pay_Mail","Mail in Check"),("Pay_Online","Online Payment")], blank=True)
	payment_amount=models.DecimalField(max_digits=6, decimal_places=2)
	am_workshop_id=models.CharField(max_length=10)
	am_workshop_status=models.CharField(max_length=12, choices=[("COMPLETE","COMPLETE"),("INCOMPLETE","INCOMPLETE"),("IN PROGRESS","IN PROGRESS")], blank=True)
	pm_workshop_id=models.CharField(max_length=10)
	pm_workshop_status=models.CharField(max_length=12, choices=[("COMPLETE","COMPLETE"),("INCOMPLETE","INCOMPLETE"),("IN PROGRESS","IN PROGRESS")], blank=True)
	confirmation_timestamp=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	event_checkin=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	event_checkout=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	am_checkin=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	am_checkout=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	pm_checkin=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	pm_checkout=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

	def __str__(self):
		return str(Scout2.objects.get(scout_id=str(self.scout_id)).scout_first_name)+" "+str(Scout2.objects.get(scout_id=str(self.scout_id)).scout_last_name)+" Session("+str(self.confirmation_timestamp)+")"

class Volunteer2(models.Model):
	volunteer_id=models.AutoField(primary_key=True)
	volunteer_first_name=models.CharField(max_length=50, blank=True)
	volunteer_last_name=models.CharField(max_length=50, blank=True)
	volunteer_email=models.CharField(max_length=50, blank=True)
	volunteer_phone=models.CharField(max_length=10, blank=True)
	volunteer_area=models.CharField(max_length=5000, blank=True)
	volunteer_status=models.CharField(max_length=8, choices=[("ACTIVE","ACTIVE"),("INACTIVE","INACTIVE")], blank=True)

	def __str__(self):
		return self.volunteer_first_name+" "+self.volunteer_last_name