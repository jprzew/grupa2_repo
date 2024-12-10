import unittest
from age import categorize_by_age


class TestCategorizeByAge(unittest.TestCase):

    def test_child(self):
        self.assertEqual(categorize_by_age(5), 'Child')

    def test_teenager(self):
        self.assertEqual(categorize_by_age(15), 'Teenager')

    def test_adult(self):
        self.assertEqual(categorize_by_age(30), 'Adult')

    def test_senior(self):
        self.assertEqual(categorize_by_age(70), 'Senior')

    def test_negative_age(self):
        self.assertEqual(categorize_by_age(-5), 'Invalid age: -5.')

    def test_invalid_value(self):

        with self.assertRaises(ValueError):
            categorize_by_age('Hello')


if __name__ == '__main__':
    unittest.main(verbosity=2)

# Oprócz unittest.skip mamy jeszcze:
# - unittest.skipIf(condition, reason)
#   np. condition = sys.version_info < (3, 3)
#
# - unittest.skipUnless(condition, reason)


# Tutaj sobie wypiszemy inne funkcje z grupy "assert"
