from src.print_mixin import PrintMixin
from src.product import Product


class Category(PrintMixin):
    """
    Класс для представления категорий, их количества и количества продуктов в категориях
    """

    name: str
    description: str
    __products: list

    category_count = 0
    all_product_count = 0

    def __init__(self, name, description, products) -> None:
        self.name = name
        self.description = description
        self.__products = products
        super().__init__()
        Category.category_count += 1
        Category.all_product_count += len(self.__products)

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.all_product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        return [str(i) for i in self.__products]

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.all_product_count} шт."

    def __iter__(self):
        return ProductIterator(self)


    def middle_price(self):
        try:
            return sum(map(lambda product: product.price, self.__products)) / len(self.__products)
        except ZeroDivisionError:
            return 0



class ProductIterator:
    """
    Вспомогательный класс, с помощью которого можно перебирать товары одной категории
    """

    category: Category
    index: int

    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.products):
            product = self.category.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
