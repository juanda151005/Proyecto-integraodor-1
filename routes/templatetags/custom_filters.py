from django import template

register = template.Library()

@register.filter
def split_and_join(value, arg):
    if value:
        return ', '.join(value.split(arg))
    return ''
