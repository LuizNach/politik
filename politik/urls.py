from django.urls import path
from . import  data_manager

from . import views

urlpatterns = [
    path('hello', views.hello_world, name='hello'),
]

data_manager.start_manager()