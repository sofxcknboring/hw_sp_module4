from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Абстрактный класс для продуктов.
    """
    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass

    @property
    @abstractmethod
    def price(self):
        pass
