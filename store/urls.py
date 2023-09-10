from django.urls import path 
from . import views


urlpatterns = [
	
	path('',views.main,name="main"),
	path('checkout/',views.checkout,name="checkout"),
	path('product/',views.product,name="product"),
	path('store/',views.store,name="store"),

	

]