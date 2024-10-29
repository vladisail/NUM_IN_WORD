import unittest
from number_to_words import number_in_words

class TestNumberToWords(unittest.TestCase):

    def test_single_digits(self):
        """Тест единичных чисел (0-9)"""
        self.assertEqual(number_in_words(0), "ноль")
        self.assertEqual(number_in_words(1), "один")
        self.assertEqual(number_in_words(5), "пять")

    def test_tens(self):
        """Тест десятков"""
        self.assertEqual(number_in_words(10), "десять")
        self.assertEqual(number_in_words(21), "двадцать один")
        self.assertEqual(number_in_words(57), "пятьдесят семь")

    def test_hundreds(self):
        """Тест сотен"""
        self.assertEqual(number_in_words(100), "сто")
        self.assertEqual(number_in_words(345), "триста сорок пять")
        self.assertEqual(number_in_words(999), "девятьсот девяносто девять")

    def test_thousands(self):
        """Тест тысяч с правильным склонением"""
        self.assertEqual(number_in_words(1000), "одна тысяча")
        self.assertEqual(number_in_words(2000), "две тысячи")
        self.assertEqual(number_in_words(5000), "пять тысяч")
        self.assertEqual(number_in_words(10000), "десять тысяч")
        self.assertEqual(number_in_words(21421), "двадцать одна тысяча четыреста двадцать один")

    def test_millions(self):
        """Тест миллионов с правильным склонением"""
        self.assertEqual(number_in_words(1_000_000), "один миллион")
        self.assertEqual(number_in_words(2_000_000), "два миллиона")
        self.assertEqual(number_in_words(5_000_000), "пять миллионов")
        self.assertEqual(number_in_words(21_000_000), "двадцать один миллион")

    def test_large_numbers(self):
        """Тест чисел с миллионами и тысячами"""
        self.assertEqual(number_in_words(1_234_567), "один миллион двести тридцать четыре тысячи пятьсот шестьдесят семь")
        self.assertEqual(number_in_words(987_654_321), "девятьсот восемьдесят семь миллионов шестьсот пятьдесят четыре тысячи триста двадцать один")

    def test_negative_numbers(self):
        """Тест отрицательных чисел"""
        self.assertEqual(number_in_words(-1), "один")
        self.assertEqual(number_in_words(-999_999_999), "девятьсот девяносто девять миллионов девятьсот девяносто девять тысяч девятьсот девяносто девять")

    def test_out_of_range(self):
        """Тест чисел вне диапазона"""
        self.assertEqual(number_in_words(1_000_000_000), "Ошибка: допустимый диапазон от -999_999_999 до 999_999_999")
        self.assertEqual(number_in_words(-1_000_000_000), "Ошибка: допустимый диапазон от -999_999_999 до 999_999_999")

if __name__ == "__main__":
    unittest.main()
