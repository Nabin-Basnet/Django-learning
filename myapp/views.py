from django.shortcuts import render,redirect,get_object_or_404
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