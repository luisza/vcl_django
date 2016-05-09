from django.contrib import admin

# Register your models here.
from .models import Schedule, Scheduletimes

admin.site.register([Schedule, Scheduletimes])