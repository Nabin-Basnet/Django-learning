from django.urls import path
from myapp.views import home,about,delete,edit,landing,login,signup
# from django.contrib import admin

urlpatterns=[
    path("",landing,name="landing"),
    path("home/",home,name="home"),
    path("about/",about),
    path("delete/<int:p_id>",delete,name="delete"),
    path("edit/<int:p_id>",edit,name="edit"),
     path('login/', login, name='login'),  # Custom login page
    path('signup/', signup, name='signup'),  # Custom signup page
]