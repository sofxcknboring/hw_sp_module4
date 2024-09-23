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

## Тестирование

```bash
poetry run pytest
```

### Отчёт о покрытии

Чтобы просмотреть отчет, откройте файл index.html, который находится в папке htmlcov, в вашем веб-браузере. Вы можете сделать это, выполнив следующую команду:
```bash
open htmlcov/index.html  # Для macOS
xdg-open htmlcov/index.html  # Для Linux
start htmlcov/index.html  # Для Windows
```