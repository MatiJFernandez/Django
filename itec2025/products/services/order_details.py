from products.models import OrderDetail, Order, Product
from products.repositories.order_details import OrderDetailRepository

class OrderDetailService:

    @staticmethod
    def create(order: Order, product: Product, quantity: int) -> OrderDetail:
        return OrderDetailRepository.create(order=order, product=product, quantity=quantity)

    @staticmethod
    def get_all() -> list[OrderDetail]:
        return OrderDetailRepository.get_all()

    @staticmethod
    def get_by_order(order_id: int) -> list[OrderDetail]:
        return OrderDetailRepository.get_by_order(order_id)

    @staticmethod
    def get_by_product(product_id: int) -> list[OrderDetail]:
        return OrderDetailRepository.get_by_product(product_id)

    @staticmethod
    def delete(order_detail_id: int) -> bool:
        detail = OrderDetailRepository.get_by_id(order_detail_id)
        if detail:
            return OrderDetailRepository.delete(order_detail_id)
        return False

    @staticmethod
    def update(order_detail_id: int, quantity: int) -> bool:
        detail = OrderDetailRepository.get_by_id(order_detail_id)
        if detail:
            OrderDetailRepository.update(detail, quantity=quantity)
            return True
        return False
