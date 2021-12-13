import json
import pickle

from django import template

register = template.Library()


@register.filter(name='dict_key')
def dict_key(data, key):
    return data[key]


@register.filter(name='has_groups')
def has_groups(user, groups):
    groups = json.loads(str(groups))
    if user.is_authenticated and user.groups.filter(name__in=groups).exists():
        return True
    return False