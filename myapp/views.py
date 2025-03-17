from django.shortcuts import render,redirect
from django.http import request
from .models import person
# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST["name"]     
        p=person.objects.create(name=name)
        p.save()
        return redirect('home')
    return render (request,"index.html")

def index(request):
    p=person.objects.all()
    return render(request,"index.html",{"p":p})

def about(request):
    return render(request,"about.html")