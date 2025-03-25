from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.http import request
from .models import person
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST["name"]
        age=request.POST["age"]   
        address=request.POST["address"]   
        discription=request.POST["discription"]
        image=request.FILES["image"]  
        p=person.objects.create(name=name,age=age,address=address,discription=discription,image=image)
        p.save()
        return redirect('home')
    return render (request,"index.html")

def about(request):
    p=person.objects.all()
    return render(request,"about.html",{'p':p})

def delete(request,p_id):
    p=person.objects.get(id=p_id)
    p.delete()
    return redirect(about)


def edit(request,p_id):
    p=get_object_or_404(person,id=p_id)
    if request.method=="POST":
        name=request.POST["name"]
        age=request.POST["age"]   
        address=request.POST["address"]   
        discription=request.POST["discription"]
        image=request.FILES["image"]  
        p.name=name
        p.age=age
        p.address=address
        p.discription=discription
        p.image=image
        p.save()
        return redirect(about)
    return render(request,"index.html")

def landing(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

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
        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.save()

        messages.success(request, "Your account has been successfully created!")
        return redirect('login')  # Redirect to login page after successful signup

    return render(request, "signup.html")
