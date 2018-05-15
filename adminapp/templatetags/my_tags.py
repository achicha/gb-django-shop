from django import template

register = template.Library()

URL_PREFIX = '/media/'


def rotation_str(string):
    result = ''
    for i in range(len(string)):
        if i % 2 == 0:
            letter = string[i].upper()
        else:
            letter = string[i].lower()
        result += letter
    return result


register.filter('rotation', rotation_str)
