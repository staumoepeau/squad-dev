from django.urls import path
from .views import *

urlpatterns = [
    path('', robot, name='robot'),
    path('add_robot', add_robot, name='add_robot'),
    path('edit_robot/<robotname>', edit_robot, name='edit_robot'),
    path('delete_robot/<robotname>', delete_robot, name='delete_robot'),
    ]