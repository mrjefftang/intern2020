#!/bin/env python3
import string
import unittest
#import pseudocryption
import pseudocryption_solution as pseudocryption

input_string = "Hello from the Cylance Applied Research Team!"
input_string2 = input_string.replace(' ', '')[:-1]

class TestPseudocryptionMethods(unittest.TestCase):
    def test_xor_types(self):
        xor_key = 'A'
        output = pseudocryption.encrypt_xor(xor_key, 'Hello World!')
        self.assertTrue(isinstance(output, list))
        self.assertTrue(isinstance(output[0], int))

    def test_xor_A(self):
        xor_key = 'A'
        answer = [9, 36, 45, 45, 46, 97, 39, 51, 46, 44, 97, 53, 41, 36, 97, 2, 56, 45, 32, 47, 34, 36, 97, 0, 49, 49, 45, 40, 36, 37, 97, 19, 36, 50, 36, 32, 51, 34, 41, 97, 21, 36, 32, 44, 96]
        output = pseudocryption.encrypt_xor(xor_key, input_string)
        self.assertEqual(output, answer)

    def test_xor_AAAA(self):
        xor_key = 'AAAA'
        answer = [9, 36, 45, 45, 46, 97, 39, 51, 46, 44, 97, 53, 41, 36, 97, 2, 56, 45, 32, 47, 34, 36, 97, 0, 49, 49, 45, 40, 36, 37, 97, 19, 36, 50, 36, 32, 51, 34, 41, 97, 21, 36, 32, 44, 96]
        output = pseudocryption.encrypt_xor(xor_key, input_string)
        self.assertEqual(output, answer)

    def test_substitution_types(self):
        key = string.ascii_letters
        output = pseudocryption.encrypt_substitution(key, input_string2)
        self.assertTrue(isinstance(output, list))
        self.assertTrue(isinstance(output[0], str))

    def test_substitution(self):
        key = 'mdyCHrajXDAKgSPtVIJUuBwQZRxceGfhMoEnLlzYFWqkpNOTvsib'
        answer = ['o', 'H', 'K', 'K', 'P', 'r', 'I', 'P', 'g', 'U', 'j', 'H', 'e', 'Z', 'K', 'm', 'S', 'y', 'H', 'x', 't', 't', 'K', 'X', 'H', 'C', 'k', 'H', 'J', 'H', 'm', 'I', 'y', 'j', 'N', 'H', 'm', 'g']
        output = pseudocryption.encrypt_substitution(key, input_string2)
        self.assertEqual(output, answer)

    def test_substitution_null(self):
        key = string.ascii_letters
        answer = [x for x in input_string2]
        output = pseudocryption.encrypt_substitution(key, input_string2)
        self.assertEqual(output, answer)

    def test_caesar_types(self):
        answer = [x for x in input_string2]
        output = pseudocryption.encrypt_caesar(3, input_string2)
        self.assertTrue(isinstance(output, list))
        self.assertTrue(isinstance(output[0], str))

    def test_caesar_null(self):
        answer = [x for x in input_string2]
        output = pseudocryption.encrypt_caesar(0, input_string2)
        self.assertEqual(output, answer)

    def test_caesar_6(self):
        answer = ['N', 'k', 'r', 'r', 'u', 'l', 'x', 'u', 's', 'z', 'n', 'k', 'I', 'E', 'r', 'g', 't', 'i', 'k', 'G', 'v', 'v', 'r', 'o', 'k', 'j', 'X', 'k', 'y', 'k', 'g', 'x', 'i', 'n', 'Z', 'k', 'g', 's']
        output = pseudocryption.encrypt_caesar(6, input_string2)
        self.assertEqual(output, answer)

    def test_caesar_25(self):
        answer = ['g', 'D', 'K', 'K', 'N', 'E', 'Q', 'N', 'L', 'S', 'G', 'D', 'b', 'X', 'K', 'z', 'M', 'B', 'D', 'Z', 'O', 'O', 'K', 'H', 'D', 'C', 'q', 'D', 'R', 'D', 'z', 'Q', 'B', 'G', 's', 'D', 'z', 'L']
        output = pseudocryption.encrypt_caesar(25, input_string2)
        self.assertEqual(output, answer)

    def test_caesar_25_symmetric(self):
        answer = [x for x in input_string2]
        output = pseudocryption.encrypt_caesar(25, input_string2)
        output2 = pseudocryption.encrypt_caesar(len(string.ascii_letters)-25, ''.join(output))
        self.assertEqual(output2, answer)

    def test_rot13_types(self):
        output = pseudocryption.encrypt_rot13("HelloWorld")
        self.assertTrue(isinstance(output, list))
        self.assertTrue(isinstance(output[0], str))

    def test_rot13(self):
        answer = ['U', 'r', 'y', 'y', 'B', 's', 'E', 'B', 'z', 'G', 'u', 'r', 'P', 'L', 'y', 'n', 'A', 'p', 'r', 'N', 'C', 'C', 'y', 'v', 'r', 'q', 'e', 'r', 'F', 'r', 'n', 'E', 'p', 'u', 'g', 'r', 'n', 'z']
        output = pseudocryption.encrypt_rot13(input_string2)
        self.assertEqual(output, answer)

    def test_rot13_circle(self):
        answer = [x for x in input_string2]
        output = pseudocryption.encrypt_rot13(input_string2)
        output2 = pseudocryption.encrypt_rot13(''.join(output))
        output3 = pseudocryption.encrypt_rot13(''.join(output2))
        output4 = pseudocryption.encrypt_rot13(''.join(output3))
        self.assertEqual(output4, answer)

    def test_make_encrypt_rot1(self):
        fn = pseudocryption.make_encrypt_rotN(1)
        self.assertTrue(callable(fn))

    def test_make_encrypt_rot1(self):
        fn = pseudocryption.make_encrypt_rotN(1)
        answer = ['I', 'f', 'm', 'm', 'p', 'g', 's', 'p', 'n', 'u', 'i', 'f', 'D', 'z', 'm', 'b', 'o', 'd', 'f', 'B', 'q', 'q', 'm', 'j', 'f', 'e', 'S', 'f', 't', 'f', 'b', 's', 'd', 'i', 'U', 'f', 'b', 'n']
        output = fn(input_string2)
        self.assertEqual(output, answer)

    def test_make_encrypt_rot2(self):
        fn = pseudocryption.make_encrypt_rotN(2)
        answer = ['J', 'g', 'n', 'n', 'q', 'h', 't', 'q', 'o', 'v', 'j', 'g', 'E', 'A', 'n', 'c', 'p', 'e', 'g', 'C', 'r', 'r', 'n', 'k', 'g', 'f', 'T', 'g', 'u', 'g', 'c', 't', 'e', 'j', 'V', 'g', 'c', 'o']
        output = fn(input_string2)
        self.assertEqual(output, answer)

    def test_make_encrypt_rot13(self):
        fn = pseudocryption.make_encrypt_rotN(13)
        output = fn(input_string2)
        output13 = pseudocryption.encrypt_rot13(input_string2)
        self.assertEqual(output, output13)

    def test_make_encrypt_rot1_docstring(self):
        fn = pseudocryption.make_encrypt_rotN(1)
        self.assertTrue(fn.__doc__ != None)

if __name__ == "__main__":
    unittest.main()
