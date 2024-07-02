from django import template

register = template.Library()

@register.filter
def to(value, end):
    return range(value, end + 1)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
