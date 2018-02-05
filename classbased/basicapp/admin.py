from django.contrib import admin

# Register your models here.
from basicapp.models import Student, School

admin.site.register(Student)
admin.site.register(School)
