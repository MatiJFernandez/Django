from django.urls import path

from products.views import product_list, order_list, escanear_codigo

urlpatterns = [
    path(
        route='product_list/', 
        view=product_list, 
        name='product_list'
    ),
    path(
        route='order_list/', 
        view=order_list, 
        name='order_list'
    ),
    path(route='escaner/', view=escanear_codigo, name='escaner'),
]   