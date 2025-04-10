from products.models import Customer
from products.repositories.customers import CustomerRepository

class CustomerService:

    @staticmethod
    def create(name: str, email: str, phone: str) -> Customer:
        return CustomerRepository.create(name=name, email=email, phone=phone)

    @staticmethod
    def get_all() -> list[Customer]:
        return CustomerRepository.get_all()

    @staticmethod
    def get_by_id(customer_id: int) -> Customer | None:
        return CustomerRepository.get_by_id(customer_id)

    @staticmethod
    def delete(customer_id: int) -> bool:
        customer = CustomerRepository.get_by_id(customer_id)
        if customer:
            return CustomerRepository.delete(customer_id)
        return False

    @staticmethod
    def update(customer_id: int, name: str, email: str, phone: str) -> bool:
        customer = CustomerRepository.get_by_id(customer_id)
        if customer:
            CustomerRepository.update(customer, name=name, email=email, phone=phone)
            return True
        return False

    @staticmethod
    def search_by_name(name: str) -> list[Customer]:
        return CustomerRepository.search_by_name(name)
