from django.shortcuts import render

from .models import Product, Theme

# Create your views here.
def all_products(request):
    '''
    Only return products in stock under the selected category
    '''
    products = Product.objects.all().filter(stock__gt=0).filter(category__category__icontains=request.session.get('sel_cat',''))
    categories = Theme.objects.all()
    
    return render(request, "products.html", {"products": products, "categories": categories})


# Create your views here.
