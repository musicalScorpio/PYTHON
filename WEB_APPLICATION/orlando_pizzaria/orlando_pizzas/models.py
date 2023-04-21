from django.db import models
from enum import Enum

# Create your models here.
class Pizza (models.Model):
    name = models.CharField(max_length=25)
    date_added = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
class Toppings (models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    text = models.CharField(max_length=25)
    date_added = models.DateTimeField(auto_now=True)
    toppping_name = models.CharField(max_length=25,default='Default')
