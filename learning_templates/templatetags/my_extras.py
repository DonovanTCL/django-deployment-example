from django import templates
{% load templatestags %}

register = template.Library()

def cut(vaule,args):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace (arg,'')

register.filter('cut',cut)
