#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTests(unittest.TestCase):
    """Acme Products Testing Suite"""
    def test_default_product_price(self):
        """Test default product price"""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight"""
        prod = Product('Test Product 2')
        self.assertEqual(prod.weight, 20)

    def test_explodability_method(self):
        """Test explodability method output"""
        prod = Product('Test Product 3', 15, 25, .9)
        self.assertEqual(prod.explode(), "...boom!")

class AcmeReportTests(unittest.TestCase):
    """Acme Reporting Sytem Testing Suite"""
    def test_default_num_products(self):
        """Test """
        products = generate_products()
        self.assertEqual(len(products), 30)
    def test_legal_names(self):
        products = generate_products()
        for product in products:
            split_name = product.name.split()
            self.assertEqual(len(split_name), 2)
            self.assertIn(split_name[0], ADJECTIVES)
            self.assertIn(split_name[1], NOUNS)

if __name__ == '__main__':
    unittest.main()