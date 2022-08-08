from unittest import TestCase
from functions import divide

class Test(TestCase):
    def Test_divide(self):
        dividend=15
        divisor = 3
        expected_value = 9
        self.assertAlmostEquals((divide(dividend,divisor), expected_value,))
