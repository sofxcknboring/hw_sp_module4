from src.category import Category
from src.product import Product


def test_category_init(product1, product2, product3, category1):
    assert category1.name == "Category Name"
    assert category1.description == "Category Description"
    assert len(category1.products) > 0


def test_add_product(category1):
    new_product = Product("Product 4", "Description of Product 4", 4.0, 4)
    category1.add_product(new_product)

    assert len(category1.products.splitlines()) == 4
    assert "Product 4" in category1.products


def test_products_output_format(category1):
    expected_output = (
        "Product 1, 1.0 руб. Остаток: 1 шт.\n"
        "Product 2, 2.0 руб. Остаток: 2 шт.\n"
        "Product 3, 3.0 руб. Остаток: 3 шт.\n"
    )
    assert category1.products == expected_output


def test_category_count():
    initial_count = Category.category_count
    Category("New Category", "New Description", [])
    assert Category.category_count == initial_count + 1


def test_product_count(category1):
    initial_product_count = Category.product_count
    new_product = Product("Product 4", "Description of Product 4", 4.0, 4)
    category1.add_product(new_product)
    assert Category.product_count == initial_product_count + 1
