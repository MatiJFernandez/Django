from products.models import Order, Customer

class OrderRepository:

    @staticmethod
    def create(customer: Customer) -> Order:
        return Order.objects.create(customer=customer)

    @staticmethod
    def delete(order_id: int) -> bool:
        try:
            order = Order.objects.get(id=order_id)
            order.delete()
            return True
        except Order.DoesNotExist:
            raise ValueError("La orden no existe")

    @staticmethod
    def get_all() -> list[Order]:
        return Order.objects.all()

    @staticmethod
    def get_by_id(order_id: int) -> Order | None:
        try:
            return Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return None

    @staticmethod
    def get_by_customer(customer_id: int) -> list[Order]:
        return Order.objects.filter(customer__id=customer_id)
