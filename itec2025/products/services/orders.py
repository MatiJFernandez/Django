from products.models import Order, Customer
from products.repositories.orders import OrderRepository

class OrderService:

    @staticmethod
    def create(customer: Customer) -> Order:
        return OrderRepository.create(customer=customer)

    @staticmethod
    def get_all() -> list[Order]:
        return OrderRepository.get_all()

    @staticmethod
    def get_by_id(order_id: int) -> Order | None:
        return OrderRepository.get_by_id(order_id)

    @staticmethod
    def delete(order_id: int) -> bool:
        order = OrderRepository.get_by_id(order_id)
        if order:
            return OrderRepository.delete(order_id)
        return False

    @staticmethod
    def get_by_customer(customer_id: int) -> list[Order]:
        return OrderRepository.get_by_customer(customer_id)
