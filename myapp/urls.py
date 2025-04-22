from django.urls import path
from .forms import *
from myapp.views import home,about,delete,edit,signup,user_logout,theam,contact,login_form
# from django.contrib import admin

urlpatterns=[
    path("",home,name="home"),
    path("about/",about,name="about"),

    path("delete/<int:p_id>",delete,name="delete"),
    path("edit/<int:p_id>",edit,name="edit"),

    path("contact/",contact,name="contact"),
    path('signup/', signup, name='signup'),  # Custom signup page
    path('user_logout/', user_logout, name='user_logout'),
    path('theam/', theam, name='theam'),
    
    path("login/",login_form,name='login_form')
    
   
]