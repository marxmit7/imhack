import unittest

from extract_most_common_word import most_common_words


class TestMostCommon(unittest.TestCase):
    def test_simple(self):
        file_contents = 'the most common word is common'
        expected = [('common', 2)]
        self.assertEqual(most_common_words(file_contents), expected)

    def test_large_file(self):
        with open('ExtractMost Common Word from text file/test.txt') as f:
            file_contents = f.read()
        expected = [('sed', 1651)]
        self.assertEqual(most_common_words(file_contents), expected)
