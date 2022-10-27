from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('countries', views.countries_list),
    path('countries/pk', views.countries_details)
    
    
]

