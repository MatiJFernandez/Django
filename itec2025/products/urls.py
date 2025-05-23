from django.urls import path

from products.views import (
    order_list, 
    product_detail,
    product_list, 
    escanear_codigo,
    product_create,
)

urlpatterns = [
    path(
        route='product_list/', 
        view=product_list, 
        name='product_list'
    ),
    path(
        route='product_detail/<int:product_id>/',
        view=product_detail,
        name='product_detail'
    ),
    path(
        route='order_list/', 
        view=order_list, 
        name='order_list'
    ),
    path(route='escaner/', view=escanear_codigo, name='escaner'),
    path(route='create/', view=product_create, name='product_create'),
]