from decimal import Decimal
from typing import List

from products.models import Product
from products.repositories.products import ProductRepository

class ProductService:

    @staticmethod
    def create(name: str, price: float, stock: int) -> Product:
        return ProductRepository.create(name=name, price=price, stock=stock)

    @staticmethod
    def get_all() -> list[Product]:
        return ProductRepository.get_all()

    @staticmethod
    def get_by_id(product_id: int) -> Product | None:
        return ProductRepository.get_by_id(product_id)

    @staticmethod
    def delete(product_id: int) -> bool:
        product = ProductRepository.get_by_id(product_id=product_id)
        if product:
            return ProductRepository.delete(product_id=product_id)
        return False

    @staticmethod
    def update(product_id: int, name: str, price: float, stock: int) -> bool:
        product = ProductRepository.get_by_id(product_id=product_id)
        if product:
            ProductRepository.update(product=product, name=name, price=price, stock=stock)
            return True
        return False

    @staticmethod
    def search_by_name(name: str) -> list[Product]:
        return ProductRepository.search_by_name(name)

    @staticmethod
    def search_by_price_range(min_price: float, max_price: float) -> list[Product]:
        return ProductRepository.search_by_price_range(min_price, max_price)

    @staticmethod
    def sum_total_price(product_list: List[Product]) -> Decimal:
        total = Decimal(0)
        for product in product_list:
            total +=( product.price * product.stock)
        return total