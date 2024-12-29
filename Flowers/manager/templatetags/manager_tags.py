from django import template
from ..models import *

register = template.Library()

@register.simple_tag
def all_types():
    return Types.objects.all()
