from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.models import Cart
from django.conf import settings
from django.contrib.sessions.backends.db import SessionStore


def OrderCreate(request):
    user = request.user
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            orders = form.save()

            for item in cart:
                OrderItem.objects.create(order=orders,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'],
                                         )
            cart.clear()
            return render(request, 'thanks.html', {'orders': orders})
    else:
        form = OrderCreateForm()

    return render(request, 'order.html', {'cart': cart, 'form': form})
    pass
