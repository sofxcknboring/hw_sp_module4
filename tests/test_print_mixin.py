from src.category import Category
from src.product import Product


def test_print_mixin(capsys):
    Product("Product 1", "Description of Product 1", 1.0, 1)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Product 1, Description of Product 1, 1.0, 1)"

    Category(
        "Category Name",
        "Category Description",
        [],
    )
    message2 = capsys.readouterr()
    assert message2.out.strip() == "Category(Category Name, Category Description)"
