from unittest import TestCase, main
from model.product import Product


class TestProduct(TestCase):
    def test_product_without_price(self):
        product = Product('test1', 'test1 description', 'test1_img.png', '5 stars', 'test1 brand', False)


if __name__ == '__main__':
    main()