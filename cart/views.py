from django.shortcuts import render

# The view for rendering the "cart.html" page
def view_cart(request):
    return render(request, "cart.html")