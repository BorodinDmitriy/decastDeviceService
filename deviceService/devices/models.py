# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
  id = models.IntegerField(primary_key=True)
  login = models.CharField(max_length=50)
  
  def __str__(self):
    return self.login


class Device(models.Model):
  id = models.AutoField(primary_key=True)
  personal_account = models.CharField(max_length=50)
  sent_reading = models.IntegerField(default=0)
  serial_number = models.CharField(max_length=50)
  user = models.ForeignKey(
    User,
    verbose_name="Владелец устройства"
  )
  
  def __str__(self):
    return self.personal_account
  
class Reading(models.Model):
  id = models.AutoField(primary_key=True)
  date = models.DateTimeField(auto_now=True)
  value = models.CharField(max_length=50)
  device = models.ForeignKey(
    Device,
    verbose_name="Устройство"
  )
  
  def __str__(self):
    return self.value