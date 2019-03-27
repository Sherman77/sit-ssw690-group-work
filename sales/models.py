from django.db import models

# Create your models here.
# Create a class represents all items for sale
class SaleItem(models.Model):
    # Images
    image = models.ImageField(upload_to='images/')
    #Title
    title = models.CharField(max_length=200)
    #Description
    description = models.CharField(max_length=1000)
    #Email
    email = models.EmailField(max_length=70, blank=True)
    #Price
    price = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.title
