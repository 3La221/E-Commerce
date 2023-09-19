import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
	title = django_filters.CharFilter(lookup_expr="icontains")
	price__lt = django_filters.NumberFilter(field_name="price", lookup_expr="lt")
	price__gt = django_filters.NumberFilter(field_name="price", lookup_expr="gt")

	class Meta:
		model = Product
		fields = ['title','price']
