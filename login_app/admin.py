from django.contrib import admin
from django.contrib.admin.sites import site
from login_app.models import UserLogin

# Register your models here.

admin.site.register(UserLogin)