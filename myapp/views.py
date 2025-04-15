from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.http import request
from .models import person
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
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
        return redirect('login_view')  # Redirect to login page after successful signup

    return render(request, "signup.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        

        # Check if fields are empty
        if not username or not password:
            messages.error(request, "All fields are required!")
            return redirect("login_view")

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect(about)  # Change this to your dashboard or homepage
        else:
            messages.error(request, "Invalid username or password!")
            return redirect("login_view")

    return render(request, "login.html")


    
def user_logout(request):
    logout(request)  # Logs out the user
    messages.success(request, "You have been logged out successfully!")
    return redirect('landing')

def index(request):
    name="nabin"
    mydict={
        'name':name
    }
    return 

def theam(request):
    return render(request,"portfolio.html")