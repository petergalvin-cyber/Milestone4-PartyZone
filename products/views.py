from django.shortcuts import render

from .models import Product, Theme

# Create your views here.
def all_products(request):
    products = Product.objects.all().filter(stock__gt=0)
    categories = Theme.objects.all()
    
    return render(request, "products.html", {"products": products, "categories": categories})


# Create your views here.
