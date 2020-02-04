from django.shortcuts import get_object_or_404
from productsVinyls.models import Vinyl

# This allows all cart items to be visible on every page

def cart_contents(request):
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    vinyl_count = 0
    
    for id, quantity in cart.items():
        vinyl = get_object_or_404(Vinyl, pk=id)
        total += quantity * vinyl.price
        vinyl_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'vinyl': vinyl})
    
    return {'cart_items': cart_items, 'total': total, 'vinyl_count': vinyl_count}