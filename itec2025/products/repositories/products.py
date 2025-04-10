from products.models import Product

class ProductRepository:
    """
    Clase de repositorio que se encargará de conectarse con la DB para manipular Productos
    """

    @staticmethod
    def create(
        name: str,
        price: float, 
        stock: int
        ) -> Product:
            return Product.objects.create(
                name=name, 
                price=price, 
                stock=stock)
    
    @staticmethod
    def delete(product: Product):
        """
        Método que elimina un objeto (producto) de la DB
        """
        try:
            Product.delete
        except Product.DoesNotExist: # type: ignore
            raise ValueError("El producto no existe")
        
    @staticmethod
    def update(
        product: Product,
        name: str,
        price: float, 
        stock: int,
        ) -> Product:
        Product.name = name
        Product.price = price
        Product.stock = stock
        Product.save
    
        return Product.objects.update(
            name=name, 
            price=price, 
            stock=stock
        )
            


    @staticmethod
    def get_all() -> list[Product]:
        """
        Método que obtiene todos los objetos (productos) de la DB
        """
        return Product.objects.all()
    
    @staticmethod
    def get_by_id(product_id: int) -> Product:
        """
        Método que obtiene un objeto (producto) de la DB por su ID
        """
        try:
            return Product.objects.get(id=product_id)
        except:
            Product.DoesNotExist: # type: ignore 
            return None

    @staticmethod
    def search_by_name(name: str) -> list[Product]:
        """
        Método que busca un objeto (producto) en la DB por su nombre (por parte de su nombre)
        """

        return Product.objects.filter(name__icontains=name) #lookups que retorna todos los objetos que contengan el valor ingresado 
        ############################# atributo__queContenga=valor

    @staticmethod
    def search_by_price_range(min_price: float, max_price: float) -> list[Product]:
        """
        Método que busca un objeto (producto) en la DB por su precio
        """
        return Product.objects.filter(price_range=(min_price, max_price))

        return Product.objects.filter(
            price__gte=min_price,
            price__lte=max_price
        ) #lookups que retorna todos los objetos que contengan el valor ingresado. Código inalcanzable por tener un return antes 
