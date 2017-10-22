# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User, Device, Reading

# Register your models here.
admin.site.register(User)
admin.site.register(Device)
admin.site.register(Reading)
