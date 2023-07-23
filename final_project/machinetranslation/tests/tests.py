import unittest
from translator import english_to_french, french_to_english
class TestTranslator(unittest.TestCase):
    def test_english_to_french_hello(self):
        english_text = "Hello"
        expected_result = "Bonjour"
        actual_result = english_to_french(english_text)
        self.assertEqual(actual_result, expected_result)

    def test_english_to_french_bonjour(self):
        english_text = "Bonjour"
        expected_result = "Bonjour"
        actual_result = english_to_french(english_text)
        self.assertEqual(actual_result, expected_result)

    def test_french_to_english_bonjour(self):
        french_text = "Bonjour"
        expected_result = "Hello"
        actual_result = french_to_english(french_text)
        self.assertEqual(actual_result, expected_result)

    def test_french_to_english_hello(self):
        french_text = "Hello"
        expected_result = "Hello"
        actual_result = french_to_english(french_text)
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
