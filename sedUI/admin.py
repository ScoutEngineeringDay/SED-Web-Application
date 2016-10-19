from django.contrib import admin
from .models import Course, Scout, Staff, Location, Question_list, Workshop

admin.site.register(Course)
admin.site.register(Staff)
admin.site.register(Scout)
admin.site.register(Location)
admin.site.register(Question_list)
admin.site.register(Workshop)
