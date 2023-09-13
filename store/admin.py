from django.contrib import admin
from . models import Product,Category,Review,Order,OrderItem,Customer


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)

# Register your models here.
