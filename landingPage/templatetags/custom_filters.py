from django import template

register = template.Library()

@register.filter(name='truncate_with_ellipsis')
def truncate_with_ellipsis(value, max_length):
    if len(value) > max_length:
        return value[:max_length] + '...'
    else:
        return value[:max_length]      

@register.filter
def cart_total_quantity(cart):
    return sum(cart.values())