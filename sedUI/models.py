from django.db import models
<<<<<<< HEAD

# Create your models here.
class Scout(models.Model):
	scout_id=models.AutoField(primary_key=True)
=======
from django.core.validators import RegexValidator

US_states=(
	('AL','Alabama'),
	('AK','Alaska'),
	('AZ','Arizona'),
	('AR','Arkansas'),
	('CA','California'),
	('CO','Colorado'),
	('CT','Connecticut'),
	('DE','Delaware'),
	('FL','Florida'),
	('GA','Georgia'),
	('HI','Hawaii'),
	('ID','Idaho'),
	('IL','Illinois'),
	('IN','Indiana'),
	('IA','Iowa'),
	('KS','Kansas'),
	('KY','Kentucky'),
	('LA','Louisiana'),
	('ME','Maine'),
	('MD','Maryland'),
	('MA','Massachusetts'),
	('MI','Michigan'),
	('MN','Minnesota'),
	('MS','Mississippi'),
	('MO','Missouri'),
	('MT','Montana'),
	('NE','Nebraska'),
	('NV','Nevada'),
	('NH','New Hampshire'),
	('NJ','New Jersey'),
	('NM','New Mexico'),
	('NY','New York'),
	('NC','North Carolina'),
	('ND','North Dakota'),
	('OH','Ohio'),
	('OK','Oklahoma'),
	('OR','Orgeon'),
	('PA','Pennsylvania'),
	('RI','Rhode Island'),
	('SC','South Carolina'),
	('SD','South Dakota'),
	('TN','Tennessee'),
	('TX','Texas'),
	('UT','Utah'),
	('VT','Vermont'),
	('VA','Virginia'),
	('WA','Washington'),
	('WV','West Virginia'),
	('WI','Wisconsin'),
	('WY','Wyoming')
	)

# Create your models here.
class Scout(models.Model):
	phone_regex = RegexValidator(regex=r'^?1?\d{9,15}$', message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed.")
	gender_choice=(
		('m', 'male'),
		('f', 'female')
		)
	clubs_choice=(
		('BSA','Boy Scouts of America'),
		('GSA','Girl Scouts of America'),
		('VC','Venture Crew')
		)
	scout_id=models.AutoField(primary_key=True)
	first_name=models.CharField(max_length=50, blank=True)
	last_name=models.CharField(max_length=50, blank=True)
	gender=models.CharField( max_length=1, choices=gender_choice, blank=True)
	age=models.IntegerField(default=0, blank=True)
	street=models.CharField(max_length=50, blank=True)
	city=models.CharField(max_length=50, blank=True)
	state=models.CharField( max_length=2, choices=US_states, blank=True)
	zip_code=models.IntegerField(default=0, blank=True)
	phone_number = models.CharField(max_length=10, blank=True)
	email=models.CharField(max_length=50, blank=True)
	emergency_first_name=models.CharField(max_length=50, blank=True)
	emergency_last_name=models.CharField(max_length=50, blank=True)
	emergency_phone=models.CharField(max_length=10, blank=True)
	affiliation=models.CharField( max_length=4, choices=gender_choice, blank=True)

	def __str__(self):
		return self.first_name+" "+self.last_name
>>>>>>> 9ac481a003d3b9b5e650f8899651fb8571966e21

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
<<<<<<< HEAD
		return self.class_name + '-' +self.class_descriptionS

class Staff(models.Model):
	staff_id=models.AutoField(primary_key=True)

class Location(models.Model):
	location_id=models.AutoField(primary_key=True)
=======
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
	street=models.CharField(max_length=50, blank=True)
	city=models.CharField(max_length=50, blank=True)
	state=models.CharField( max_length=2, choices=US_states, blank=True)
	zip_code=models.IntegerField(default=0, blank=True)
	phone_number=models.CharField(max_length=10, blank=True)
	activity_status=models.CharField(max_length=1, choices=activity_status_choice, blank=True)

	def __str__(self):
		return self.first_name+" "+self.last_name


class Location(models.Model):
	location_id=models.AutoField(primary_key=True)
	street=models.CharField(max_length=50, blank=True)
	city=models.CharField(max_length=50, blank=True)
	state=models.CharField( max_length=2, choices=US_states, blank=True)
	zip_code=models.IntegerField(default=0, blank=True)
	building=models.CharField(max_length=50, blank=True)
	room_number=models.IntegerField(default=0)
	capacity=models.IntegerField(default=0, blank=True)

	def __str__(self):
		return self.building
>>>>>>> 9ac481a003d3b9b5e650f8899651fb8571966e21

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
