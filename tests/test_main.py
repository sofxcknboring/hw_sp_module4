from main import Category, Product


def test_init(product1, product2, product3, category1):
    assert product1.name == "Product 1"
    assert product2.name == "Product 2"
    assert product3.name == "Product 3"

    assert product1.description == "Description of Product 1"
    assert product2.description == "Description of Product 2"
    assert product3.description == "Description of Product 3"

    assert product1.price == 1.0
    assert product2.price == 2.0
    assert product3.price == 3.0

    assert product1.quantity == 1
    assert product2.quantity == 2
    assert product3.quantity == 3

    assert category1.name == "Category Name"
    assert category1.description == "Category Description"
    assert category1.products == [product1, product2, product3]


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


def test_category_count(product1, product2):
    Category.category_count = 0
    Category.product_count = 0

    category1 = Category("Category 1", "Description 1", [product1, product2])
    assert category1.category_count == 1
    assert len(category1.products) == 2
    assert category1.product_count == 2

    category2 = Category("Category 2", "Description 2", [product1])

    assert category2.category_count == 2
    assert category2.product_count == 3


def test_product_count_with_empty_category():
    Category.category_count = 0
    Category.product_count = 0

    category_empty = Category("Category", "Desc", [])

    assert category_empty.category_count == 1
    assert category_empty.product_count == 0
