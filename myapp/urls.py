from django.urls import path
from myapp.views import home,about
# from django.contrib import admin

urlpatterns=[
    path("home",home),
    path("",about)
]