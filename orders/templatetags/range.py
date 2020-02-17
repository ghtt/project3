from django import template


register = template.Library()


@register.filter()
def get_range(n):
    return range(n)
