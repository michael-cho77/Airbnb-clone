from django import template

# 새로운 tag를 등록 
register = template.Library()


@register.filter
def make_capitals(value):
    return value.capitalize()

"""
Case2: 
@register.filter(name="make_capitals")
def Blah_blah(value):
    return value.capitalize()

"""