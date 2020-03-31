from django.shortcuts import render
from products.models import Product, Theme

# Create your views here.
def do_search(request):
    products = Product.objects.filter(category__category__icontains=request.GET['q'])
    sel_cat = request.GET['q'].strip()
    
    categories = Theme.objects.all()
    return render(request, "products.html", {"products": products, "categories": categories, "sel_cat": sel_cat})
