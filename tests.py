import unittest
import multiples


class MultiplesTests(unittest.TestCase):

    def test_is_multiple_of_three(self):
        self.assertTrue(multiples.is_multiple_of_three(9))

    def test_is_not_multiple_of_three(self):
        self.assertFalse(multiples.is_multiple_of_three(4))

    def test_is_multiple_of_five(self):
        self.assertTrue(multiples.is_multiple_of_five(10))

    def test_is_not_multiple_of_five(self):
        self.assertFalse(multiples.is_multiple_of_five(14))

    def test_is_multiple_of_three_and_five(self):
        self.assertTrue(multiples.is_multiple_of_three_and_five(15))

    def test_is_not_multiple_of_three_and_five(self):
        self.assertFalse(multiples.is_multiple_of_three_and_five(12))

    def test_is_multiple_of_three_but_not_of_five(self):
        self.assertFalse(multiples.is_multiple_of_three_and_five(9))

    def test_is_multiple_of_five_but_not_of_three(self):
        self.assertFalse(multiples.is_multiple_of_three_and_five(10))

    def test_format_to_print_a_number(self):
        self.assertEqual("1", multiples.format(1))

    def test_format_to_print_a_multiple_of_three(self):
        self.assertEqual("Three", multiples.format(6))

    def test_format_to_print_a_multiple_of_five(self):
        self.assertEqual("Five", multiples.format(10))

    def test_format_to_print_a_multiple_of_three_and_five(self):
        self.assertEqual("ThreeFive", multiples.format(15))


if __name__ == "__main__":
    unittest.main()