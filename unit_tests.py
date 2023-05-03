import unittest
from reverse_words.app import reverse_words

class TestReverseWord(unittest.TestCase):
    def test_reverse_word_1(self):
        self.assertEqual(reverse_words('a1a'),'a1a')

    def test_reverse_word_2(self):
        self.assertEqual(reverse_words('abcd efgh'),'dcba hgfe')

    def test_reverse_word_3(self):
        self.assertEqual(reverse_words('a1bcd efg!h'),'d1cba hgf!e')

    def test_reverse_word_4(self):
        self.assertEqual(reverse_words(''),'')

