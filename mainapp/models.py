from django.db import models

# Create your models here.

class Book(models.Model):
    name =  models.CharField(max_length= 20,blank=False, null=False)
    author = models.CharField(max_length= 20,blank=False, null=False)
    isbn = models.IntegerField(default=0) 
    def __str__(self):
        return str(self.id)