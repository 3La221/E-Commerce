from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	
	path('',views.main,name="main"),
	path('checkout/<uuid:product_id>',views.checkout,name="checkout"),
	path('product/<uuid:product_id>',views.product,name="product"),
	path('store/',views.store,name="store"),
	

	

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)