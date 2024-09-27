class Category:
    """
    Класс для представления категорий, их количества и количества продуктов в категориях
    """

    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return "".join([f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n" for p in self.__products])
