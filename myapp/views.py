from django.shortcuts import render,redirect
from django.http import request
from .models import person
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


# def about(request):
#     return render(request,"about.html")