from products.models import OrderDetail, Order, Product

class OrderDetailRepository:

    @staticmethod
    def create(order: Order, product: Product, quantity: int) -> OrderDetail:
        return OrderDetail.objects.create(order=order, product=product, quantity=quantity)

    @staticmethod
    def delete(order_detail_id: int) -> bool:
        try:
            detail = OrderDetail.objects.get(id=order_detail_id)
            detail.delete()
            return True
        except OrderDetail.DoesNotExist:
            raise ValueError("El detalle de orden no existe")

    @staticmethod
    def update(detail: OrderDetail, quantity: int) -> OrderDetail:
        detail.quantity = quantity
        detail.save()
        return detail

    @staticmethod
    def get_all() -> list[OrderDetail]:
        return OrderDetail.objects.all()

    @staticmethod
    def get_by_order(order_id: int) -> list[OrderDetail]:
        return OrderDetail.objects.filter(order__id=order_id)

    @staticmethod
    def get_by_product(product_id: int) -> list[OrderDetail]:
        return OrderDetail.objects.filter(product__id=product_id)
