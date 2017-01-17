from django.contrib import admin
from .models import Course, Scout, Staff, Location, Session, Workshop

admin.site.register(Course)
admin.site.register(Staff)
admin.site.register(Scout)
admin.site.register(Location)
admin.site.register(Session)
admin.site.register(Workshop)
