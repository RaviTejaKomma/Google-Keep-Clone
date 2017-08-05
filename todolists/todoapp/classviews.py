from . import * ## importing the models ##

### REST API's imports ###
from todoapp.models import *
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from serializers import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def main_page(request):
    template = loader.get_template('todoapp/main.html')
    return HttpResponse(template.render())


class List_ALL(LoginRequiredMixin,ListCreateAPIView):
    ## over riding this method ##

    def get_queryset(self):
        self.queryset = Todolists.objects.filter(user = self.request.user)
        return super(List_ALL, self).get_queryset()

    serializer_class = TodolistsSerializer

class List_Specific(LoginRequiredMixin,RetrieveUpdateDestroyAPIView):
    ## over riding this method ##
    def get_queryset(self):
        self.queryset = Todolists.objects.filter(user = self.request.user)
        return super(List_Specific, self).get_queryset()

    serializer_class = TodolistsSerializer

class List_Specific_all_items(LoginRequiredMixin,ListCreateAPIView):
    def get_queryset(self):
        self.queryset = Todoitem.objects.filter(todolists__id = self.kwargs["pk"])
        return super(List_Specific_all_items, self).get_queryset()

    serializer_class = TodoitemSerializer

class List_Specific_Item_Specific(LoginRequiredMixin,RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        self.queryset = Todoitem.objects.filter(todolists__id=self.kwargs["list_id"])
        return super(List_Specific_Item_Specific, self).get_queryset()

    serializer_class = TodoitemSerializer

