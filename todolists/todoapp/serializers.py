from rest_framework import serializers
from todoapp.models import *  ## importing all the models ##


######## refer this http://www.django-rest-framework.org/tutorial/1-serialization/ ########

"""
This class works as serializer and deserializer for the models data
Steps:
1. We'll need to add our new app and the rest_framework app to INSTALLED_APPS. Let's edit the <project>/settings.py file:
2. We should create our models in  models.py
3. The first thing we need to get started on our Web API is to provide a way of
   serializing and deserializing the model instances into representations such as json.
   We can do this by declaring serializers that work very similar to Django's forms.
   Create a file in the <app> directory named serializers.py.

4. There are two types of serializers, one is Serializer and the other one is ModelSerializer
5. Before we go any further we'll familiarize ourselves with using our new Serializer class. Let's drop into the Django shell.
   >> python manage.py shell

6. Writing regular Django views using our serializers

"""

class TodolistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolists
        fields = ('id','name','creation_date','user')

class TodoitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todoitem
        fields = ('id','description','completed','due_by','todolists')



