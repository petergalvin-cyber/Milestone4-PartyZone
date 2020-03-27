from django.db import models

# Create a Product Database
class Theme(models.Model):
    category = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.category


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Theme, null=True)

    def __str__(self):
        return self.name




