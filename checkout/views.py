from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from .forms import PaymentForm, OrderForm
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from productsVinyls.models import Vinyl
import stripe
from .models import OrderLineVinyl
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

# Payment form view, log in required to checkout
@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                vinyl = get_object_or_404(Vinyl, pk=id)
                total += quantity * vinyl.price
                order_line_vinyl = OrderLineVinyl(
                    order=order,
                    vinyl=vinyl,
                    quantity=quantity
                )
                order_line_vinyl.save()
            
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('productsViynls'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = PaymentForm()
        order_form = OrderForm()
    
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})