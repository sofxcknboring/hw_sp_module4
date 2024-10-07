## Module4


### Установка

1. Убедитесь, что установлен [Poetry](https://python-poetry.org/).
2. Клонируйте репозиторий:
   ```bash
   git clone <URL_репозитория>
   cd <имя_папки_репозитория>
   ```
3. Установите зависимости:
   ```bash
   poetry install
   ```

### Что реализовано на данный момент:

```python
class Product:
    """
    Класс для представления продуктов
    """

    name: str
    description: str
    price: float
    quantity: int
```

```python
class Category:
    """
    Класс для представления категорий, их количества и количества продуктов в категориях
    """

    name: str
    description: str
    products: list
```

```python
class ProductIterator:
    """
    Вспомогательный класс, с помощью которого можно перебирать товары одной категории
    """
    category: Category
    index: int
```

## Тестирование

```bash
poetry run pytest
```

### Отчёт о покрытии

Сформировать отчёт:
```bash
coverage html
```