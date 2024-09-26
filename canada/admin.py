from django.contrib import admin
from django.contrib.gis import admin
from .models import *
# Register your models here.


@admin.register(Contact)
class Admin(admin.ModelAdmin):
    list_display = ['name','email','phno','companyname','message']
