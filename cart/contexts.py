from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})
    sel_cat = request.session.get('sel_cat', "")
    cart_items = []
    total = 0
    product_count = 0
    cartIDS = []


    for id, quantity in cart.items():
        
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cartIDS.append(int(id))
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
        
    # add sel_cat to the return list
    return {"cartIDS": cartIDS, 'cart_items': cart_items, 'total': total, 'product_count': product_count, 'sel_cat': sel_cat}