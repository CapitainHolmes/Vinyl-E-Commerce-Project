from django.shortcuts import render, redirect, reverse

# The view for rendering the "cart.html" page
def view_cart(request):
    return render(request, "cart.html")

# A view to show the quantity of vinyls that a user has in their cart
def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('vinyls'))

# A view to adjust the quantity of vinyls a user will have in their cart
def adjust_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))