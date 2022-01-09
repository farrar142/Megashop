from django import template

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg
@register.filter
def multiple(value, arg):
    try:
        value = int(value)
    except:
        pass
    try:
        arg = int(arg)
    except:
        pass
    result = str(value*arg)
    return result