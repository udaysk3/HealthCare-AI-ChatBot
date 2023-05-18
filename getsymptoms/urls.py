
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.getsymptoms),
    path('getsymptoms',views.getsymptoms, name='getsymptoms')
]
