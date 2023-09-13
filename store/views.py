from django.shortcuts import render,get_object_or_404
from django.db.models import Avg
from . models import Product,Order,OrderItem
import uuid,json
from django.http import JsonResponse



# Create your views here.
def main(request):
	latest_products = Product.objects.order_by('-date_added')[:6]
	top_selling = Product.objects.order_by('-sold')[:6]
	hot_deals = Product.objects.filter(isdiscount=True)[:6]
	top_rated = Product.objects.annotate(
		average_rating = Avg('review__rating')
		).order_by('-average_rating')[:6]

	if request.user.is_authenticated:
		customer = request.user.customer
		order , created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
	else :
		items = []
		order = {
			'get_cart_total':0,
			'get_cart_items':0,
			'id':uuid.uuid4()
		}
	

	context = { 
				'latest_products':latest_products,
				'top_selling' : top_selling,
				'hot_deals' : hot_deals,
				'top_rated' : top_rated,
				'items' : items,
				'order':order 

				}

	return render(request,'store/main.html',context)

def store(request):
	context = {}
	return render(request,'store/store.html',context)


def checkout(request,order_id):
	order = get_object_or_404(Order,id=order_id)
	context = {'order':order}
	return render(request,'store/checkout.html',context)

def product(request,product_id):
	product = get_object_or_404(Product,id = product_id)
	customer = request.user.customer 
	order,created = Order.objects.get_or_create(customer=customer,complete=False)
	items = order.orderitem_set.all()

	context = {'product':product,'order':order,'items':items}
	return render(request,'store/product.html',context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order,created = Order.objects.get_or_create(customer=customer,complete=False)

	orderItem , created = OrderItem.objects.get_or_create(order=order,product=product)

	if action == "add":
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == "remove":
		orderItem.quantity -= 1

	orderItem.save()
	if orderItem.quantity <=0:
		orderItem.delete()

	print(productId,action)
	return JsonResponse("Item was added",safe=False)
