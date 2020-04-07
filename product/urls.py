from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    # /product/
    path('' , views.temp, name='temp'),
    # /products/id/
    # path('<category_slug>/', views.category_list, name='category_list'),
    #/products/id/product_name


    # path('<product_code>/' , views.product_info , name='product_info'),



    # path('<article_slug>/', views.product_info, name='product_info'),
    #path('<int:article>/', views.product_info, name='product_info'),
]

