from django.urls import path, include
from . import views

urlpatterns =[
    path('get/', views.get_details, name="get_details"),
    path('insert/', views.push_details, name="push_details"),
    
]