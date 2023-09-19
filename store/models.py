from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.




class Product(models.Model):
	id = models.UUIDField(
		default=uuid.uuid4,unique=True,
		primary_key=True,editable=False
		)
	title = models.CharField(max_length=25,null=True)
	description = models.TextField(null=True,blank=True)
	price = models.FloatField()
	quantity = models.PositiveIntegerField(default=1)
	sold = models.PositiveIntegerField(default=0)
	categories = models.ManyToManyField('Category')
	date_added = models.DateTimeField(auto_now_add=True,blank=True,null=True)
	isdiscount = models.BooleanField(default=False)
	new_price = models.FloatField(null = True, blank=True , default='product02.png')
	image = models.ImageField(default = "pc.png" ,null = True, blank = True)

	def __str__(self):
		return self.title



	def average(self):
		reviews = self.review_set.all()
		if reviews:
			ratings = [review.rating for review in reviews]
			return sum(ratings) / len(reviews)
		else:
			return 0  # Handle the case when there are no reviews.




class Review(models.Model):
	id = models.UUIDField(
		default=uuid.uuid4,unique=True,
		primary_key=True,editable=False
		)
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	name = models.CharField(max_length=25)
	description = models.TextField(null=True,blank=True)
	rating = models.IntegerField(default=5)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name + "review"


class Category(models.Model):
	id = models.UUIDField(
		default=uuid.uuid4,unique=True,
		primary_key=True,editable=False
		)
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class OrderItem(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	order = models.ForeignKey('Order',on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0)
	
	@property
	def get_total(self):

		return (self.product.price * self.quantity)
	


class Customer(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,null = True,blank=True)
	name = models.CharField(max_length=200,null=True)
	email = models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.name


class Order(models.Model):
	id = models.UUIDField(
		default=uuid.uuid4,unique=True,
		primary_key=True,editable=False
		)
	customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
	address = models.CharField(max_length=100)
	wilaya = models.CharField(max_length=50)
	zip_code = models.IntegerField()
	complete = models.BooleanField(default=False)
	telephone = models.CharField(max_length=16)
	transaction_id = models.CharField(max_length=200,null=True)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = [item.get_total for item in orderitems]
		return sum(total)


	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = [item.quantity for item in orderitems]
		return sum(total)
	


	def __str__(self):
		return  " Order " + str(self.id)
