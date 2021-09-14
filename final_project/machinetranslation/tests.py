"""
run tests on language translators
"""
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """ test english to french class """
    def test1(self):
        """ test english to french function """
        self.assertEqual(english_to_french(None), 'text must be provided') # test null input
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test input Hello
        self.assertNotEqual(english_to_french('Hello'), 'BonjXXXour')  # test input Hello

class TestFrenchToEnglish(unittest.TestCase):
    """ test french to english class """
    def test1(self):
        """ test french to english function """
        self.assertEqual(french_to_english(None), 'text must be provided') # test null input
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test input Bonjour
        self.assertNotEqual(french_to_english('Bonjour'), 'HeXXXllo') # test input Bonjour

unittest.main()
