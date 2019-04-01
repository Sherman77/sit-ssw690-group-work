from django.db import models


class JobPost(models.Model):
    # Images
    image = models.ImageField(upload_to='images/')
    #Title
    title = models.CharField(max_length=200)
    #Description
    description = models.CharField(max_length=1000)
    #Email
    email = models.EmailField(max_length=70, blank=True)


    def __str__(self):
        return self.title
