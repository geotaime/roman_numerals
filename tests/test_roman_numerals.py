import unittest

from src.roman_numerals import roman_numerals


class roman_rumeralsTestCase(unittest.TestCase):

    def test_python_test_setup_works(self):
        self.assertTrue(True)

    def test_it_returns_I_when_number_is_1(self):
        # Arrange / Given

        # Act / When
        result = roman_numerals(1)

        # Assert / Then
        self.assertEqual('I', result)

    def test_it_returns_II_when_number_is_2(self):
        # Arrange / Given

        # Act / When
        result = roman_numerals(2)

        # Assert / Then
        self.assertEqual('II', result)

    def test_it_returns_IV_when_number_is_4(self):
        # Arrange / Given

        # Act / When
        result = roman_numerals(4)

        # Assert / Then
        self.assertEqual('IV', result)    
