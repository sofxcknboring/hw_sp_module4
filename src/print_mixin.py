class PrintMixin:
    def __init__(self, *args, **kwargs) -> None:
        print(repr(self))

    def __repr__(self):
        if self.__class__.__name__ == "Category":
            return f"{self.__class__.__name__}({self.name}, {self.description})"
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
