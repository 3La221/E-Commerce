from django import template
register = template.Library()

@register.filter(name="head")
def head(value):
	return value[:3]


@register.filter(name="tail")
def tail(value):
	return value[3:]


@register.filter(name="dinarFormat")
def dinarFormat(value):
	res = "{:,}".format(int(value))
	res += "DA"
	return res


@register.filter(name="len")
def len(value):
	return len(value)