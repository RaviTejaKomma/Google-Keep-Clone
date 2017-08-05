from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views
from todoapp.classviews import *
## here . means current directory ##

app_name = "todoapp"

urlpatterns = [
    # url(r'^list/$',views.TodoListListView.as_view(),name="get_all_lists"),
    # url(r'^list/create/$',views.CreateList.as_view(),name="create-list"), ## should be placed on top of the get_list_items url ##
    # url(r'^list/update/(?P<pk>[0-9]+)/$',views.UpdateList.as_view(),name="update-list"),
    # url(r'^list/delete/(?P<pk>[0-9]+)/$',views.DeleteList.as_view(),name="delete-list"),
    # url(r'^list/(?P<pk>[0-9]+)/$',views.TodoListDetailView.as_view(),name="get_list_items"),
    # url(r'^list/(?P<slug>[a-zA-Z0-9_]+)/$',views.TodoListDetailView.as_view(),name="get_list_items"),

   ## REST API urls ##
    url(r'^main/$',main_page, name="main_page"),
    url(r'^rest_list/$',List_ALL.as_view(), name="rest_list"),
    url(r'^rest_list/(?P<pk>[0-9]+)/$', List_Specific.as_view(), name='rest_list_id'),
    url(r'^rest_list/(?P<pk>[0-9]+)/items/$', List_Specific_all_items.as_view(), name='rest_list_all_items__id'),
    url(r'^rest_list/(?P<list_id>[0-9]+)/items/(?P<pk>[0-9]+)/$', List_Specific_Item_Specific.as_view(), name='rest_list_item__id'),
]

"""
    url(r'^restlist/$', List_All.as_view(), name="rest_list"),
    url(r'^restlist/(?P<pk>[0-9]+)/$', List_Specific.as_view(), name='rest_list_id'),
    url(r'^restitem/$', Item_All.as_view(), name='rest_item'),
    url(r'^restitem/(?P<pk>[0-9]+)/$', Item_Specific.as_view(), name='rest_item_id'),
    url(r'restlist/(?P<list_id>[0-9]+)/restitem/$', List_Specific_Item.as_view(), name='rest_list_id_item'),
    url(r'restlist/(?P<list_id>[0-9]+)/restitem/(?P<item_id>[0-9]+)/$', List_Specific_Item_Specific.as_view(), name='rest_list_id_item_id'),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
"""