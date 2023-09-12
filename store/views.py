from django.shortcuts import render,get_object_or_404
from . models import Product
from django.db.models import Avg

# Create your views here.
def main(request):
	latest_products = Product.objects.order_by('-date_added')[:6]
	top_selling = Product.objects.order_by('-sold')[:6]
	hot_deals = Product.objects.filter(isdiscount=True)[:6]

	print(hot_deals[0].average())

	top_rated = Product.objects.annotate(
		average_rating = Avg('review__rating')
		).order_by('-average_rating')[:6]
	

	context = { 'latest_products':latest_products,

				'top_selling' : top_selling,

				'hot_deals' : hot_deals,
				'top_rated' : top_rated
					}

	return render(request,'store/main.html',context)

def store(request):
	context = {}
	return render(request,'store/store.html',context)


def checkout(request,product_id):
	
	context = {'product':product}
	return render(request,'store/checkout.html',context)

def product(request,product_id):
	product = get_object_or_404(Product,id = product_id)
	context = {'product':product}
	return render(request,'store/product.html',context)