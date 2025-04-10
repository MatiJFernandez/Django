from products.models import Customer

class CustomerRepository:

    @staticmethod
    def create(name: str, email: str, phone: str) -> Customer:
        return Customer.objects.create(name=name, email=email, phone=phone)

    @staticmethod
    def delete(customer_id: int) -> bool:
        try:
            customer = Customer.objects.get(id=customer_id)
            customer.delete()
            return True
        except Customer.DoesNotExist:
            raise ValueError("El cliente no existe")

    @staticmethod
    def update(customer: Customer, name: str, email: str, phone: str) -> Customer:
        customer.name = name
        customer.email = email
        customer.phone = phone
        customer.save()
        return customer

    @staticmethod
    def get_all() -> list[Customer]:
        return Customer.objects.all()

    @staticmethod
    def get_by_id(customer_id: int) -> Customer | None:
        try:
            return Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return None

    @staticmethod
    def search_by_name(name: str) -> list[Customer]:
        return Customer.objects.filter(name__icontains=name)
