from django import forms
from .models import Order,Review


class ShippingForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['first_name','last_name','wilaya','address','telephone']

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review 
		fields = ['name','description','rating']

