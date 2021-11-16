from django.urls import path
from .views import (
    add_new_member,
    view_all_members,
    load_cities
)

urlpatterns = [
    path('add_member', add_new_member, name='add_member'),
    path('members', view_all_members, name='members_list'),
    path('load-cities/', load_cities, name='ajax_load_cities'),
]