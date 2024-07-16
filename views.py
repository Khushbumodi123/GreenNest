from django.shortcuts import render, get_object_or_404
from .models import Order

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    previous_orders = Order.objects.filter(user=request.user).exclude(id=order_id)
    context = {
        'order': order,
        'previous_orders': previous_orders
    }
    return render(request, 'order_detail.html', context)
