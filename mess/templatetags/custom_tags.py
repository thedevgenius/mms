from django import template
import datetime
from account.models import *

register = template.Library()

@register.simple_tag
def CurrentYear():
    return datetime.datetime.now().year

@register.filter
def UserIcon(value):
    return value[0]

@register.filter
def TmpForLoop(value):
    return range(1, value+1)

@register.filter
def GetUserFirstName(value):
    user = User.objects.get(id=value)
    return(user.first_name)

@register.filter
def StrToDisc(value):
    return eval(value)

@register.filter
def GetDataType(value):
    new_dit = eval(value)
    return new_dit.values()
    