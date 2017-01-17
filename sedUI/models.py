from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Scout(models.Model):
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

class Health(models.Model):
	scout_id=models.ForeignKey(Scout, on_delete=models.CASCADE)

class Question_list(models.Model):
	question_id=models.AutoField(primary_key=True)
	question=models.CharField(max_length=500)

class Course(models.Model):
	class_id=models.AutoField(primary_key=True)
	class_name=models.CharField(max_length=50)
	class_description=models.CharField(max_length=500)

	def __str__(self):
		return self.class_name

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
	# street=models.CharField(max_length=50, blank=True)
	# city=models.CharField(max_length=50, blank=True)
	# state=models.CharField( max_length=2, choices=US_states, blank=True)
	# zip_code=models.IntegerField(default=0, blank=True)
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

class Group_staff(models.Model):
	group_staff_id=models.AutoField(primary_key=True)

class Security_question(models.Model):
	scout_id=models.ForeignKey(Scout, on_delete=models.CASCADE)

class Registration(models.Model):
	registration_id=models.AutoField(primary_key=True)

class Workshop_session(models.Model):
	workshop_session_id=models.AutoField(primary_key=True)
