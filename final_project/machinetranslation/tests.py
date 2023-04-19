import unittest

from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Today'), 'Demain')
        self.assertEqual(englishToFrench(' '), ' ')
    
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Demain'), 'Today')
        self.assertEqual(frenchToEnglish(' '), ' ')
        
if __name__ == "__main__":
    unittest.main()
    