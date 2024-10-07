from unittest.mock import patch

from src.product import Product


def test_new_product_class_method():
    product_data = {"name": "Product 2", "description": "Description of Product 2", "price": 200.0, "quantity": 5}
    new_product = Product.new_product(product_data)
    assert new_product.name == "Product 2"
    assert new_product.description == "Description of Product 2"
    assert new_product.price == 200.0
    assert new_product.quantity == 5


def test_product_attributes(product1):
    assert product1.name == "Product 1"
    assert product1.description == "Description of Product 1"
    assert product1.price == 1.0
    assert product1.quantity == 1

    product1.name = "Product 2"
    product1.description = "Desc1"
    product1.price = 15.0
    product1.quantity = 2

    assert product1.name == "Product 2"
    assert product1.description == "Desc1"
    assert product1.price == 15.0
    assert product1.quantity == 2


def test_product_without_attr():
    product_wn = Product("", "Desc", 1.0, 1)
    assert product_wn.name == ""


def test_price_setter_valid(product1):
    product1.price = 150.0
    assert product1.price == 150.0


def test_price_setter_invalid_negative(product1):
    product1.price = -50.0
    assert product1.price == 1.0


def test_price_setter_lower_price(product1):
    with patch("builtins.input", return_value="n"):
        product1.price = 0.7
        assert product1.price == 1.0


def test_price_setter_lower_price_accept(product1):
    with patch("builtins.input", return_value="y"):
        product1.price = 0.7
        assert product1.price == 0.7


def test_add_price_and_quantity(product1, product2):
    total_price = product1 + product2
    assert total_price == 5
