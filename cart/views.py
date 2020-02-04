from django.shortcuts import render

# The view for rendering the "cart.html" page
def view_cart(request):
    return render(request, "cart.html")

# A view to show the quantity of vinyls that a user has in their cart
def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('index'))