from django import template

register = template.Library()

@register.filter
def get_attribute(obj, attr):
    return getattr(obj, attr, '')

@register.filter
def get_data_by_column(data, column):
    return data.filter(column=column).first().data if data.filter(column=column).first() else ""