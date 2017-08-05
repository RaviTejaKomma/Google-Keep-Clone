# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
## creating the class views ##

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from todoapp.models import Todolists,Todoitem
from django.core.urlresolvers import reverse_lazy

class TodoListListView(ListView):
      model = Todolists
      context_object_name = "all_lists"
      template_name = "todoapp/get_all_lists.html"

class TodoListDetailView(DetailView):
    model = Todolists   ## we are retrieving the details of a particular college
    template_name = "todoapp/itemsdetails.html"

    slug_field = "name"

    def get_context_data(self, **kwargs):
        context = super(TodoListDetailView, self).get_context_data(**kwargs)

        context["all_items"] = Todoitem.objects.values("description","completed","due_by")\
            .filter(todolists = context["object"])
        ## context["object"] or context["todolists"] ##
        return context

class CreateList(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "todoapp.add_todolists"   ## we should the convention appname.<add or delete or update>_modelname
    permission_denied_message = "You do not have permissions to create a list!! \n please contact the admininstrators"
    # raise_exception = True

    model = Todolists
    fields = ["name","creation_date"]
    template_name = "todoapp/create_list_form.html"
    success_url = "/todo/list"

    def handle_no_permission(self):  ## it will be triggred oly when no one is logged in ##
        if self.request.user.is_authenticated:
            raise PermissionDenied(self.get_permission_denied_message())
        return super(CreateList, self).handle_no_permission()

class UpdateList(UpdateView):
    model = Todolists
    fields = ["name", "creation_date"]
    template_name = "todoapp/update_list_form.html"
    success_url = "/todo/list"

class DeleteList(DeleteView):
    model = Todolists
    template_name = "todoapp/delete_list_form.html"
    success_url = "/todo/list"



