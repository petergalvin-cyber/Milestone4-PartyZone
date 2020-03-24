from django.db import models

# Create a Product Database

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


