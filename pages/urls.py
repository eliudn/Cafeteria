from django.urls import path
from . import views

urlpatterns = [
    #   paths del core
   
    path('<int:page_id>/',views.page, name="page"),

]