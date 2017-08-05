# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

## Define the todolist (name, creation_date) and todoitem (description, completed, due_by and parent foreign key) models ##

from django.db import models
from django.contrib.auth.models import * ## importing the user table where all the users data is stored
import django.contrib.auth
class Todolists(models.Model):
      name = models.CharField(max_length=128)
      creation_date = models.DateField(auto_now_add=True)
      user = models.ForeignKey(User,on_delete=models.CASCADE, default = 1)

      def __unicode__(self):
          return self.name

class Todoitem(models.Model):
      description = models.CharField(max_length=256)
      completed = models.BooleanField(default=False)
      due_by = models.DateField()
      todolists = models.ForeignKey(Todolists,on_delete=models.CASCADE)

      def __unicode__(self):
          return self.description

