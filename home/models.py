from os import truncate
from django.db import models

class Address(models.Model):
    my_address = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    country = models.CharField(max_length=10000)
    nationality = models.CharField(max_length=10000)

def ___str__(self):
    return self.my_address

class People(models.Model):
    Lname = models.CharField(max_length=1000)
    Fname= models.CharField(max_length=1000)
    #phone_no = models.ManyToManyField(Address, on_delete=models.CASCADE)

def ___str__(self):
    return self.User_ID

class Doctor(models.Model):
    dr_lname = models.CharField(max_length=1000)
    dr_fname = models.ForeignKey(People, on_delete=models.CASCADE)
    
def ___str__(self):
    return self.dr_fname

class Bio(models.Model):
    Fname = models.CharField(max_length=1000)
    bio = models.OneToOneField(People, on_delete=models.CASCADE)

def ___str__(self):
    return self.bio

class Product(models.Model):
    pro_name = models.CharField(max_length=1000)
    quantity = models.CharField(max_length=1000)
    price = models.CharField(max_length=10000)
    store_name = models.CharField(max_length=10000)
   
