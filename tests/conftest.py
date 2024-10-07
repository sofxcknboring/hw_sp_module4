import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


@pytest.fixture
def product1():
    return Product("Product 1", "Description of Product 1", 1.0, 1)


@pytest.fixture
def product2():
    return Product("Product 2", "Description of Product 2", 2.0, 2)


@pytest.fixture
def product3():
    return Product("Product 3", "Description of Product 3", 3.0, 3)


@pytest.fixture
def smartphones():
    return (
        Smartphone("Smartphone 1", "Desc Smartphone1", 100.0, 2, 95.0, "Model1", 256, "Green"),
        Smartphone("Smartphone 2", "Desc Smartphone2", 150.0, 2, 195.0, "Model2", 512, "Red"),
    )


@pytest.fixture
def lawn_grasses():
    return (
        LawnGrass("LawnGrass 1", "Desc LG 1", 50.0, 4, "Country1", "1 Days", "Green"),
        LawnGrass("LawnGrass 2", "Desc LG 2", 20.0, 5, "Country2", "2 Days", "Red"),
    )


@pytest.fixture
def category1(product1, product2, product3):
    return Category(
        "Category Name",
        "Category Description",
        [product1, product2, product3],
    )
