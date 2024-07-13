from django import template

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "₹ "+str(number)



@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1

@register.filter(name='truncate_with_ellipsis')
def truncate_with_ellipsis(value, max_length):
    if len(value) > max_length:
        return value[:max_length] + '...'
    return value


