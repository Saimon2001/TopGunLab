#ex1 Write a Python function called is_palindrome that checks if a given word is a palindrome. 
#The function should have proper error handling and be tested with unittest
import math
import unittest

def is_palindrome(word1:str):
    #word = str(input("give me the word to check if it is a palindrome>"))
    word = word1.lower()
    median = math.ceil(len(word)/2)
    if word[:median-1] == word[:median-1:-1]:
        return print("is a palindrome")
    else:
        return print("it isn't a palindrome")

class TestPalindrome(unittest.TestCase):
    def test_1(self):
        result = is_palindrome("civic")
        self.assertEqual(result, print("is a palindrome"))

    def test_2(self):
        result = is_palindrome("deified")
        self.assertEqual(result, print("is a palindrome"))

    def test_3(self):
        result = is_palindrome("simon")
        self.assertEqual(result, print("it isn't a palindrome"))