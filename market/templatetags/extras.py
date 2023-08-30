from market.models import Category
from django import template


register = template.Library()


@register.inclusion_tag("parts/categories.html")
def categories():
    categories = Category.objects.all()
    return {"categories": categories}


@register.simple_tag
def relative_url(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name, value)
    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)
    return url