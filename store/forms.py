from django import forms
from .models import Order


class ShippingForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['first_name','last_name','wilaya','address','telephone']


