from django import template
register=template.Library()
def cut(value,arg):
    """
    This cuts tha value of arg form the string
    """
    return value.replace(arg,'')
register.filter('cut',cut)
