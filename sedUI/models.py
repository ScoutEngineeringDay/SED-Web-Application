from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Scout(models.Model):
	scout_id=models.AutoField(primary_key=True)
	phone_regex = RegexValidator(regex=r'^?1?\d{9,15}$', message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed.")
	clubs_choice=(
		('BSA','Boy Scouts of America'),
		('GSA','Girl Scouts of America'),
		('Others','Others')
		)
	# scout_id=models.models.CharField(max_length=50, primary_key=True)
	# CharField(max_length=6, primary_key=True, default=pkgen)
	first_name=models.CharField(max_length=50, blank=True)
	last_name=models.CharField(max_length=50, blank=True)
	unit_number=models.IntegerField(default=0, blank=True)
	phone = models.CharField(max_length=10, blank=True)
	email=models.CharField(max_length=50, blank=True)
	emergency_first_name=models.CharField(max_length=50, blank=True)
	emergency_last_name=models.CharField(max_length=50, blank=True)
	emergency_phone=models.CharField(max_length=10, blank=True)
	emergency_email=models.CharField(max_length=50, blank=True)
	affiliation=models.CharField( max_length=6, choices=clubs_choice, blank=True)
	photo = models.BooleanField(default=False)
	medical_notes = models.CharField(max_length=500, blank=True)
	allergy_notes = models.CharField(max_length=500, blank=True)

	def __str__(self):
		return self.first_name+" "+self.last_name

	@classmethod
	def create(first_name, last_name, unit_number, phone, emergency_first_name, emergency_last_name, emergency_phone, emergency_email, affiliation, photo, medical, allergies):
		scout = Scout.object.create(first_name, last_name, unit_number, phone, emergency_first_name, emergency_last_name, emergency_phone, emergency_email, affiliation, photo, medical, allergies)
		scout.save()
		return scout



class Course(models.Model):
	course_id=models.AutoField(primary_key=True)
	course_name=models.CharField(max_length=50)
	course_description=models.CharField(max_length=500)
	course_size=models.IntegerField()

	def __str__(self):
		return self.course_name

class Staff(models.Model):
	staff_id=models.AutoField(primary_key=True)
	activity_status_choice=(
		('I','Inactive'),
		('A','Active')
		)
	staff_role=(
		('I','Instructor'),
		('C','Core Team'),
		('V','Volunteer')
		)
	first_name=models.CharField(max_length=50, blank=True)
	last_name=models.CharField(max_length=50, blank=True)
	staff_type=models.CharField(max_length=1, choices=staff_role, blank=True)
	email=models.CharField(max_length=50, blank=True)
	phone=models.CharField(max_length=10, blank=True)
	activity_status=models.CharField(max_length=1, choices=activity_status_choice, blank=True)

	def __str__(self):
		return self.first_name+" "+self.last_name

class Location(models.Model):
	location_id=models.AutoField(primary_key=True)
	building=models.CharField(max_length=50, blank=True)
	room_number=models.IntegerField(default=0)
	capacity=models.IntegerField(default=0, blank=True)

	def __str__(self):
		return self.building

class Workshop(models.Model):
	workshop_id=models.AutoField(primary_key=True)
	course_name=models.CharField(max_length=50)
	session_id=models.CharField(max_length=5)
	workshop_time=models.CharField(max_length=2, choices=[("AM","AM"),("PM","PM")])
	workshop_status=models.CharField(max_length=20, choices=[("INCOMPLETED","INCOMPLETED"),("COMPLETED","COMPLETED")])

class Session(models.Model):
	session_id=models.AutoField(primary_key=True)
	scout_id=models.CharField(max_length=5)
	payment_method=models.CharField(max_length=1, choices=[("Pay_Mail","Mail in Check"),("Pay_Online","Online Payment")], blank=True)
