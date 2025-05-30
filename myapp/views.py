from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request
from .models import person
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *


# from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        address = request.POST["address"]
        discription = request.POST["discription"]
        image = request.FILES["image"]
        p = person.objects.create(
            name=name, age=age, address=address, discription=discription, image=image
        )
        p.save()
        return redirect("home")
    return render(request, "index.html")


def about(request):
    p = person.objects.all()
    return render(request, "about.html", {"p": p})


def delete(request, p_id):
    p = person.objects.get(id=p_id)
    p.delete()
    return redirect(about)


def edit(request, p_id):
    p = get_object_or_404(person, id=p_id)
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        address = request.POST["address"]
        discription = request.POST["discription"]
        image = request.FILES["image"]
        p.name = name
        p.age = age
        p.address = address
        p.discription = discription
        p.image = image
        p.save()
        return redirect(about)
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, "signup.html")

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return render(request, "signup.html")

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered")
            return render(request, "signup.html")

        # Create the user
        myuser = User.objects.create_user(
            username=username, email=email, password=password
        )
        myuser.save()

        messages.success(request, "Your account has been successfully created!")
        return redirect("login_view")  # Redirect to login page after successful signup

    return render(request, "signup.html")


def user_logout(request):
    logout(request)  # Logs out the user
    messages.success(request, "You have been logged out successfully!")
    return redirect("landing")


def index(request):
    name = "nabin"
    mydict = {"name": name}
    return


def theam(request):
    return render(request, "portfolio.html")


def contact(request):
    return render(request, "contact.html")


def login_form(request):
    if request.method == "POST":
        form = Login_forms(request.POST)
        if form.is_valid:
            email=request.POST["email"]
            password=request.POST['password']
            myDict={
                    'form':form 
                }
            
            errorflag=False
            Error=[]
            import re   #regular expression import
            regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  #it is variable it an be put any
            
            if not re.search(regex,email):
                errorflag=True
                errormsg="email is not valid"
                Error.append(errormsg)
                
            elif password != password.lower():
                errorflag=True
                errormsg="password should be in lowercase"
                Error.append(errormsg)

            else:
                myDict['success']=True
                myDict['successMsg']="form successfully submited"
            
            myDict['error']=errorflag
            myDict["errors"]=Error
            #myDict['successMsg']="form successfully submited"

            return render(request,"home.html", context=myDict)
        
       
    elif request.method == "GET":
        LoginForm = Login_forms()
        loginDict = {"form": LoginForm}
        return render(request, "home.html", context=loginDict)
