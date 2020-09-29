from django.contrib import admin
from .models import Location, Course, Student

admin.site.register(Location)
admin.site.register(Course)
admin.site.register(Student)