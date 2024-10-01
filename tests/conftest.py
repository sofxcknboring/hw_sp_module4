import pytest

from src.category import Category
from src.product import Product


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
def category1(product1, product2, product3):
    return Category(
        "Category Name",
        "Category Description",
        [product1, product2, product3],
    )
