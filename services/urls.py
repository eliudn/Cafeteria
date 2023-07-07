from django.urls import path
from . import views

urlpatterns = [
    #   paths del core
  
    path('services/',views.services, name="services"),
   
]