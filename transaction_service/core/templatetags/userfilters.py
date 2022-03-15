from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter
def addattrs(field, attrs):
    attr1, attr2 = attrs.split(',')
    return field.as_widget(attrs={'class': attr1,
                                  'placeholder': attr2})
