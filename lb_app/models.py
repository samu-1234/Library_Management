from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField
    author=models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)
    isbn=models.IntegerField
    category=models.CharField(max_length=100)


    def __str__(self):
        return self.title,self.author,self.category