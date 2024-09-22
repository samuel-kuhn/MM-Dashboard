# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.

from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
   pass

admin.site.register(Profile, ProfileAdmin)