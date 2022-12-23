from django.contrib import admin
from .models import Student

# Register your models here.
"""by this we can able to see student table at admin side"""
@admin.register(Student)
class Studentadmin(admin.ModelAdmin):

    list_display = ["id","name","city","std","result","checkby"]