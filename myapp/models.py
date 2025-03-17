from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(null=True)
    address=models.CharField(max_length=50,null=True)
    image=models.ImageField(upload_to='media',null=True,blank=True)
    discription=models.TextField(null=True)

