from django.urls import path
from myapp.views import home,about,delete
# from django.contrib import admin

urlpatterns=[
    path("",home,name="home"),
    path("about/",about),
    path("delete/<int:p_id>",delete,name="delete")
]