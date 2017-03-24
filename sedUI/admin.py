from django.contrib import admin
from .models import Course, Scout, Instructor, Location, Session, Workshop, AboutPage, HomePage, MailPayment, Checkout

class CourseAdmin(admin.ModelAdmin):
	list_display = ["course_id","__str__"]
	class Meta:
		model = Course

class InstructorAdmin(admin.ModelAdmin):
	list_display = ["instructor_id", "__str__", "instructor_status"]
	class Meta:
		model = Instructor
		
class ScoutAdmin(admin.ModelAdmin):
	list_display = ["scout_id","__str__"]
	class Meta:
		model = Scout

class LocationAdmin(admin.ModelAdmin):
	list_display = ["location_id","__str__"]
	class Meta:
		model = Location

class SessionAdmin(admin.ModelAdmin):
	list_display = ["session_id","__str__", "open_ceremony", "__workshop1__","__workshop2__"]
	class Meta:
		model = Session

class WorkshopAdmin(admin.ModelAdmin):
	list_display = ["workshop_id","__str__", "__instructor__", "workshop_time", "workshop_open", "open_ceremony", "__room__"]
	class Meta:
		model = Workshop

class MailPaymentAdmin(admin.ModelAdmin):
	list_display = ["mailPayment_id", "__payment_person__", "__payment_address__", "__payment_due_date__"]
	class Meta:
		model = MailPayment

admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Scout, ScoutAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(AboutPage)
admin.site.register(HomePage)
admin.site.register(Checkout)
admin.site.register(MailPayment, MailPaymentAdmin)