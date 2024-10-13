from unicodedata import category

import pytest

from src.category import Category, ProductIterator
from src.product import Product
from tests.conftest import category1


def test_category_init(product1, product2, product3, category1):
    assert category1.name == "Category Name"
    assert category1.description == "Category Description"
    assert len(category1.products) == 3


def test_category_str(category1):
    expected_str = f"Category Name, количество продуктов: {category1.all_product_count} шт."
    assert str(category1) == expected_str


def test_add_product(category1):
    new_product = Product("Product 4", "Description of Product 4", 4.0, 4)
    non_product = "Non product"
    category1.add_product(new_product)
    with pytest.raises(TypeError):
        category1.add_product(non_product)
    assert len(category1.products) == 4
    assert str(new_product) in category1.products


def test_products_output_format(category1):
    expected_output = [
        "Product 1, 1.0 руб. Остаток: 1 шт.",
        "Product 2, 2.0 руб. Остаток: 2 шт.",
        "Product 3, 3.0 руб. Остаток: 3 шт.",
    ]
    assert category1.products == expected_output


def test_category_count():
    initial_count = Category.category_count
    Category("New Category", "New Description", [])
    assert Category.category_count == initial_count + 1


def test_product_count(category1):
    initial_product_count = Category.all_product_count
    new_product = Product("Product 4", "Description of Product 4", 4.0, 4)
    category1.add_product(new_product)
    assert Category.all_product_count == initial_product_count + 1


def test_product_iterator(category1):
    iterator = ProductIterator(category1)

    products = list(iterator)
    expected_products = [str(product) for product in category1.products]
    assert products == expected_products


def test_category_middle_price_exception():
    category1 = Category('Category', 'desc', [])
    assert category1.middle_price() == 0


def test_middle_price(product1, product2):
    category1 = Category('Category', 'desc', [product1, product2])
    assert category1.middle_price() == 1.5