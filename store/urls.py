from django.urls import path
from store import views
#from django.contrib.auth import views
#from django.contrib.auth import views as g


urlpatterns = [
        
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('lg/',views.login,name="lgn"),
	#path('lg/',g.LoginView.as_view(template_name="store1/login.html"),name="lgn"),
	path('update_item/', views.updateItem, name="update_item"),	
	path('process_order/', views.processOrder, name="process_order"),	
]