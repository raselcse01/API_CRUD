from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.name
    



