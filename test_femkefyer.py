from unittest import TestCase

target = __import__('femkefyer').femkefy


class Test(TestCase):
    def test_femkefyer(self):
        result = target("VVVvvvVVVfffFFFfff sssSSSsssZZZzzzZZZ")
        self.assertEqual("FFFfffFFFfffFFFfff sssSSSsssSSSsssSSS", result)
