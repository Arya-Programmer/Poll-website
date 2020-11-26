from django import template

register = template.Library()

@register.filter
def divide(value, arg):
    try:
        return round(int(value) / int(arg))
    except Exception:
        return 10


@register.filter
def percentage(value, arg):
    try:
        divided = round(int(value) / int(arg), 2)
        return int(float(divided * 100))
    except (ValueError, TypeError) as e:
        print(e)
        return None

@register.filter
def islist(value):
    if isinstance(value, list):
        return True
    else:
        return False


@register.filter
def inside(value, arg):
    try:
        return dict(value)[arg]
    except (ValueError, ZeroDivisionError):
        return None




@register.filter
def index(value, arg):
    return value.index(arg)




@register.simple_tag
def define(val=None):
  return val