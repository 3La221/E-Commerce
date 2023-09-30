from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Avg
from . models import Product,Order,OrderItem,Category,Review
import uuid,json
from django.http import JsonResponse
from django.core.paginator import Paginator
from .filter import ProductFilter
from .forms import ShippingForm,ReviewForm






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
	products = Product.objects.all()

	query = request.GET.get('query')
	if query:
		products = products.filter(title__icontains=query)
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
	


	selected_categories = request.GET.getlist('categories')
	min_price = request.GET.get('min_price','0')
	max_price = request.GET.get('max_price','1000000')

	print(f"Selected categories: {selected_categories}")
	print(f"Min price: {min_price}")
	print(f"Max price: {max_price}")

	if max_price:
		max_price = float(max_price)
		products = products.filter(price__lte=max_price)
	if min_price :
		products = products.filter(price__gte=float(min_price))
	if selected_categories:
		products = products.filter(categories__name__in = selected_categories)


	paginator = Paginator(products , 3)
	page_number = request.GET.get("page")
	page_obj = paginator.get_page(page_number)

	categories = Category.objects.all()
	max_price = str(max_price) if max_price else '1000000'
	min_price = str(min_price) if min_price else ''
	print(f" MAX = {max_price}")
	context = {
	 'page_obj': page_obj,
	 'categories': categories,
	 'selected_categories': selected_categories,
	 'min_price': min_price, 
	  'max_price': max_price , 
	  'order':order,
	  'items':items}
	return render(request,'store/store.html',context)


def checkout(request,order_id):
	order = get_object_or_404(Order,id=order_id)

	if request.method =="POST":
		form = ShippingForm(request.POST)
		if form.is_valid():
			
			order = form.save(commit=False)
			order.customer = request.user.customer
			order.complete = True
			order.save() 
			order = Order.objects.get(customer=request.user.customer,complete=False)
			order.orderitem_set.all().delete()

			return redirect('main')
	form = ShippingForm()


	context = {'order':order,'form':form}
	return render(request,'store/checkout.html',context)

def product(request,product_id):

	product = get_object_or_404(Product,id = product_id)
	reviews = Review.objects.filter(product=product)
	customer = request.user.customer 
	order,created = Order.objects.get_or_create(customer=customer,complete=False)
	items = order.orderitem_set.all()
	print(len(reviews))
	stars = range(1, 6)
	ss = []
	five_stars = reviews.filter(rating=5)
	four_stars = reviews.filter(rating=4)
	three_stars = reviews.filter(rating=3)
	two_stars = reviews.filter(rating=2)
	one_stars = reviews.filter(rating=1)

	ss.append(len(five_stars))
	ss.append(len(four_stars))
	ss.append(len(three_stars))
	ss.append(len(two_stars))
	ss.append(len(one_stars))


	paginator = Paginator(reviews,4)
	page_number = request.GET.get("page")
	page_obj = paginator.get_page(page_number)

	

	if request.method == "POST":
		form = ReviewForm(request.POST)
		if form.is_valid:
			f = form.save(commit=False)
			f.product = product
			f.save()
		context = {
	'product':product,
	'order':order,
	'items':items,
	'reviews':reviews,
	'stars':stars,
	'ss':ss,
	'page_obj':page_obj,
	'form':form
	}
		return render(request,'store/product.html',context)
	form = ReviewForm()




	context = {
	'product':product,
	'order':order,
	'items':items,
	'reviews':reviews,
	'stars':stars,
	'ss':ss,
	'page_obj':page_obj,
	'form':form
	}
	return render(request,'store/product.html',context)

def resetOrder(request):
	data = json.loads(request.body)
	orderId = data['orderId']
	action = data['action']
	if orderId:
		order = Order.objects.get(id = orderId)

	if action == "reset":
		order.orderitem_set.all().delete()
	print(orderId)

	return JsonResponse("Order Cleared",safe=False)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	quantity = data.get('quantity')
	if quantity:
		quantity = int(quantity)
	else :
		quantity = 1
	print(quantity)
	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order,created = Order.objects.get_or_create(customer=customer,complete=False)

	orderItem , created = OrderItem.objects.get_or_create(order=order,product=product)
	print(productId)
	if action == "add":

		orderItem.quantity = (orderItem.quantity + (quantity))
	elif action == "remove":
		orderItem.quantity -= 1

	orderItem.save()
	if orderItem.quantity <=0:
		orderItem.delete()  

	return JsonResponse("Item was added",safe=False)
