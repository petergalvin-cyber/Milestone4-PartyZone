from django.shortcuts import render

from .models import Product, Theme

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    categories = Theme.objects.all()
    if categories:
        print("srwerwr")
    return render(request, "products.html", {"products": products, "categories": categories})


# Create your views here.
