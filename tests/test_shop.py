"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(500)
        assert product.check_quantity(999)
        assert product.check_quantity(1000)
        assert not product.check_quantity(1001)
        assert not product.check_quantity(1500)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        initial_quantity = product.quantity
        product.buy(500)
        expected_quantity = product.quantity
        assert expected_quantity == initial_quantity - 500

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_to_cart(self, product, cart):
        # Добавить продукт в корзину
        cart.add_product(product, buy_count=2)
        assert cart.products[product] == 2

        # Добавить продукт еще раз в корзину без указания buy_count
        cart.add_product(product)
        assert cart.products[product] == 3

    def test_remove_product_none(self, product, cart):
        # Добавить продукт в корзину
        cart.add_product(product, buy_count=5)
        assert cart.products[product] == 5

        # Удалить 1 продукт из корзины
        cart.remove_product(product, remove_count=1)
        assert cart.products[product] == 4

        # Удалить все продукты из корзины без указания remove_count
        cart.remove_product(product)
        assert not cart.products

    def test_remove_product_quantity(self, product, cart):
        # Добавить продукт в корзину
        cart.add_product(product, buy_count=5)
        assert cart.products[product] == 5

        # Удалить все продукты из корзины
        cart.remove_product(product, remove_count=50)
        assert not cart.products

    def test_remove_product_eql_add(self, product, cart):
        # Добавить продукт в корзину
        cart.add_product(product, buy_count=5)
        assert cart.products[product] == 5

        # Удалить все продукты из корзины
        cart.remove_product(product, remove_count=5)
        assert not cart.products

    def test_clear(self, product, cart):
        # Добавить продукт в корзину
        cart.add_product(product, buy_count=5)
        assert cart.products[product] == 5

        # Очищаем корзину
        cart.clear()
        assert not cart.products

    def test_get_total_price(self, product, cart):
        # Добавить продукт в корзину
        cart.add_product(product, buy_count=5)
        assert cart.products[product] == 5

        # Получаем полную стоимость корзины
        total_price = cart.get_total_price(product)
        assert total_price == 500

    def test_buy(self, product, cart):
        # Добавить продукт в корзину
        cart.add_product(product, buy_count=5)
        assert cart.products[product] == 5

        # Покупаем товары
        initial_quantity = product.quantity
        cart.buy(product)
        expected_quantity = product.quantity
        assert expected_quantity == initial_quantity - 5

    def test_buy_more_than_available(self, product, cart):
        # Добавить продукт в корзину
        cart.add_product(product, buy_count=1001)
        with pytest.raises(ValueError):
            cart.buy(product)
