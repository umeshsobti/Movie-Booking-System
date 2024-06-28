from django import template

register = template.Library()

@register.simple_tag
def increment_counter(counter):
    return counter + 1
@register.filter(name='add_str')
def add_str(value, arg):
    """
    Concatenate value and arg as strings.
    """
    return str(value) + str(arg)