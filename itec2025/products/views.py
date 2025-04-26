from django.shortcuts import redirect, render, get_object_or_404

from products.models import Product
from products.services.products import ProductService

def product_list(request):
    all_products = ProductService.get_all()
    total_price = ProductService.sum_total_price(all_products)

    return render(
        request, 
        'products/list.html',
        dict(
            products=all_products,
            otro_atributo='Atributo 2',
            total_price = total_price
        )
    )

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(
        request,
        'products/detail.html',
        dict(
            product=product,
        )
    )

def product_create(request):
    if request.method == 'POST':
        # Obtén los datos del formulario
        name = request.POST.get('name')
        price = request.POST.get('price')
        stock = request.POST.get('stock')

        # Crea un nuevo producto en la base de datos
        Product.objects.create(
            name=name,
            price=price,
            stock=stock
        )

        # Redirige a la lista de productos después de crear el producto
        return redirect('product_list')

    # Si el método es GET, muestra el formulario
    return render(request, 'products/product_create.html')

def order_list(request):
    return render(request, 'orders/list.html')

def escanear_codigo(request):
    return render(request, 'products/escanear_codigo.html')
