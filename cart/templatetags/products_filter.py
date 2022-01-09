from django import template

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def multiple(value, arg):
    result = int(value)*int(arg)
    return result