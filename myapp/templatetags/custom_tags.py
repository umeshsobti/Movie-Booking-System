from django import template

register = template.Library()

@register.simple_tag
def increment_counter(counter):
    return counter + 1
