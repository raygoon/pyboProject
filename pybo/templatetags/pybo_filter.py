from django import template

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.simple_tag
def list_count(allpage, pagenum, bypagesnum):
    return allpage-(pagenum-1)*bypagesnum-1