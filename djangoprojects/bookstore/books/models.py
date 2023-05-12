from django.db import models

class Auther(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=50)
    created = models.DateTimeField("date created")

class Book(models.Model):
    def __str__(self):
      return self.name
      
    name =  models.CharField(max_length=50)
    created = models.DateTimeField("date created")
    auther = models.ForeignKey(Auther,on_delete= models.CASCADE)
    price = models.DecimalField(decimal_places=2 , max_digits=4, null= True)