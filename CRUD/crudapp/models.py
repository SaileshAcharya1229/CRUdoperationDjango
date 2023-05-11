from django.db import models

# Create your models here.

class Student(models.Model):
    roll = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)


    def __str__(self):
     return f"{self.roll}, {self.name}, {self.email}, {self.phone}"

   
    

