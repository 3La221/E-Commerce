from django.db import models
import uuid

# Create your models here.




class Product(models.Model):
	id = models.UUIDField(
		default=uuid.uuid4,unique=True,
		primary_key=True,editable=False
		)
	title = models.CharField(max_length=25,null=True)
	description = models.TextField(null=True,blank=True)
	price = models.FloatField()
	quantity = models.IntegerField()
	categories = models.ManyToManyField('Category')

	#image

	def __str__(self):
		return self.title



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
	quantity = models.IntegerField(default=1)
	transaction_id = models.CharField(max_length=200,null=True)



class Order(models.Model):
	id = models.UUIDField(
		default=uuid.uuid4,unique=True,
		primary_key=True,editable=False
		)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	wilaya = models.CharField(max_length=50)
	zip_code = models.IntegerField()
	telephone = models.IntegerField()

	def __str__(self):
		return self.last_name + "order"
