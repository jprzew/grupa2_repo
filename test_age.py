import unittest
from age import categorize_by_age


class TestCategorizeByAge(unittest.TestCase):

    def test_child(self):
        self.assertEquals(categorize_by_age(5), 'Child')
