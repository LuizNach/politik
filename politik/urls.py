from django.urls import path
from . import  data_manager

from . import views

urlpatterns = [
    path('hello', views.hello_world, name='hello'),
    path('following', views.get_followed_politicians, name='following'),
]

data_manager.start_manager()