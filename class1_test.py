# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 15:48:42 2024

@author: jc
"""

import unittest
import class1 

# TEST 1

class TestWordLength(unittest.TestCase):
    def test_word_length(self):
        self.assertEqual(class1.word_length("Hello"), 5)
        self.assertEqual(class1.word_length("Exelent"), 7)
        self.assertEqual(class1.word_length(456), "No recibe numeros.")
        
# TEST 2
        
class TestCountLetters(unittest.TestCase):
    def test_count_letters(self):
        self.assertEqual(class1.count_letters("Programmer"), 20)
        self.assertEqual(class1.count_letters("Developer"), 18)
        self.assertEqual(class1.count_letters("Full-Stack"), 18)
        
# TEST 4

# Test 2
        
class TestReverseWord(unittest.TestCase):
    def test_reverse_word(self):
        self.assertEqual(class1.reverse_word("System"), "metsyS")
        self.assertEqual(class1.reverse_word("Programming Lenguage"), "egaugneL gnimmargorP")
        self.assertEqual(class1.reverse_word("Mom"), "Encontre un Palíndromo!")
        
if __name__ == '__main__':
    unittest.main()