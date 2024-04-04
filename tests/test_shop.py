"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(500)
        assert product.check_quantity(999)
        assert product.check_quantity(1000)
        assert not product.check_quantity(1001)
        assert not product.check_quantity(1500)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(500)
        assert product.buy(999)
        assert product.buy(1000)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        try:
            product.buy(1001)
        except ValueError:
            assert True
        else:
            assert False, "Expected ValueError was not raised"


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
