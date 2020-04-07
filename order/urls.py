from django.urls import path
from . import views

app_name = 'order'


urlpatterns = [
    # path('' , views.index , name='index'),
    # path('<category_slug>/<item_slug>/<quantity>/', views.add_to_cart, name='add_to_cart'),
    # path('cart/', views.cart_detail, name='cart_detail'),
    # path('add/<item_slug>/', views.add_to_cart, name='add_to_cart'),
	# path('remove/<item_slug>/', views.remove_from_cart, name='remove_from_cart'),
	# path('ajax/quick_add/', views.quick_add, name='quick_add'),
	# path('ajax/increment/', views.increment, name='increment'),
    # path('ajax/decrement/', views.decrement, name='decrement'),
	# path('customer-info/', views.customer_info , name='customer_info'),
	path('checkout/', views.checkout, name='checkout'),
]
