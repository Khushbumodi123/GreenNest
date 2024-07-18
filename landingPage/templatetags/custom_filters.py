from django import template

register = template.Library()

@register.filter(name='truncate_with_ellipsis')
def truncate_with_ellipsis(value, max_length):
    if len(value) > max_length:
        return value[:max_length] + '...'
    else:
        return value[:max_length]      
