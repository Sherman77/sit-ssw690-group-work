from django.db import models

# Create your models here.
class People(models.Model):
    #Portfolio picture
    image = models.ImageField(upload_to='images/')
    #Name
    name = models.CharField(max_length=50)
    #Personal introduction
    introduction = models.CharField(max_length=1000)
    #Email
    email = models.EmailField(max_length=70, blank=True)

    def __str__(self):
        return self.name
