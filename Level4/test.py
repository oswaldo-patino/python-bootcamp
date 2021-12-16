from exercise1 import regex_letters_joined_with_underscore
from unittest import TestCase, main

class TestRegEx(TestCase):
    """
    """

    def test_one_letter(self):
        self.assertTrue(regex_letters_joined_with_underscore("a_b"))

    def test_many_letters(self):
        self.assertTrue(regex_letters_joined_with_underscore("aaa_bbbb"))

    def test_empty(self):
        self.assertFalse(regex_letters_joined_with_underscore(""))

    def test_begins_underscore(self):
        self.assertFalse(regex_letters_joined_with_underscore("_b"))

    def test_ends_underscore(self):
        self.assertFalse(regex_letters_joined_with_underscore("a_"))

    def test_contains_spaces(self):
        self.assertFalse(regex_letters_joined_with_underscore("a a_b b"))

    def test_contains_uppercase(self):
        self.assertFalse(regex_letters_joined_with_underscore("Aa_Bb"))

    def test_many_underscores(self):
        self.assertFalse(regex_letters_joined_with_underscore("a_b_c"))

    def test_contains_numbers(self):
        self.assertFalse(regex_letters_joined_with_underscore("a1_b2"))

    def test_contains_symbols(self):
        self.assertFalse(regex_letters_joined_with_underscore("a1_b2"))

if __name__ == "__main__":
        main()