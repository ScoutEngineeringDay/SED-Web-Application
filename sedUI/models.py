from django.db import models

# Create your models here.
class Scout(models.Model):
	scout_id=models.AutoField(primary_key=True)

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
		return self.class_name + '-' +self.class_descriptionS

class Staff(models.Model):
	staff_id=models.AutoField(primary_key=True)

class Location(models.Model):
	location_id=models.AutoField(primary_key=True)

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
