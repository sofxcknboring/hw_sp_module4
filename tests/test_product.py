from src.product import Product

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