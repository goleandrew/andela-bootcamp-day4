'''unittest for find_missing function'''
import unittest
from missing_numbers import find_missing

class Test(unittest.TestCase):
    """docstring for ExtraMissingNumberTest"""

    def test_missing_entry_one(self):
        '''testing missing entry one'''
        self.assertEqual(54, find_missing([1, 2], [1, 2, 54]),
                         msg='should return 54 for [1,2],[1,2,54]')

    def test_missing_entry_two(self):
        '''testing missing entry two'''
        self.assertEqual(44, find_missing([4, 6, 20], [4, 6, 20, 44]),
                         msg='should return 44 for [4, 6, 20],[4, 6, 20, 44]')
                         