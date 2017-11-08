# -*- coding: utf-8 -*-

import unittest
from app import hello_world

class HelloWorldTestCase(unittest.TestCase):
    """Testa `app.py`."""

    def test_se_output_e_Flask_dockerizado(self):
        """O metodo hello_world retorna a string 'Flask dockerizado'?"""
        self.assertTrue(hello_world() == "Ola Mundo")

if __name__ == '__main__':
    unittest.main()
