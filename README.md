# Background

The goal of this exercise is to understand your ability to write short snippets of code that would be useful from the perspective of automation and reverse engineering.

Our expectation is that you will be able to quickly identify the necessary background information and complete the short coding exercises within 30-60 minutes.

Implement each exercise as specified and document any assumptions. Some details are intentionally vague to give you creative freedom and provide an opportunity for you to demonstrate your knowledge and skills.

During the course of our interview, we’ll refer back to your code and ask you questions regarding your assumptions and decisions to understand your thinking.

## Exercise #1

Implement a small program to determine the file type of a given file. The program identify the following executable file formats and their native CPU architecture:- Portable Executable (PE)- Executable and Linkable Format (ELF)- Mach Object (Mach-O)

Your program will be given a relative file name passed in as the first argument and it should return a string representing the file type and architecture on standard out.

You may implement this in whatever language feels comfortable to you.

Expected output

```
[user @ machine]$ ./exercise1 24d004a104d4d54034dbcffc2a4b19a11f39008a575aa614ea04703480b1022c
PE32

[user @ machine]$ ./exercise1 4a740227eeb82c20286d9c112ef95f0c1380d0e90ffb39fc75c8456db4f60756
PE64

[user @ machine]$ ./exercise1 1996ddc461861c59034fae84a4db45788d9f3b3e809389d36800d194dab138bd
MO32

[user @ machine]$ ./exercise1 4131d4737fe8dfe66d407bfd0a0df18a4a77b89347471cc012da8efc93c661a5
MO64

[user @ machine]$ ./exercise1 49595bd732f619f82900a91718bcc033da454889696eef923ffc7052549ac282
ELF32

[user @ machine]$ ./exercise1 16eb66ebe74931e637d856b2189714fc3e25baf8af5ba41bb75f976ca56ee307
ELF64
```

## Exercise #2

The second exercise it’s to complete the implementation of a skeleton project.

The project is available here:

You may (re)implement this in whatever language feels comfortable to you.

The goal of this exercise is to give you the opportunity to demonstrate your programming capabilities in a low-stress environment. Your challenge is to implement the functions which raise an `ImplementMeError` in `pseudocryption.py`.

You must implement every function that returns ImplementMeError. A test harness has been provided for you to examine the correctness of your implementation.

### Tests
A small suite of testcases have been provided to test your code but by no means is this test suite thorough.

The testsuite can be executed by running the `test_pseudocryption.py` file directly or via Python3's `unittest` module.

```
[user @ host] $ python -m unittest -v -v
test_caesar_25 (test_pseudocryption.TestPseudocryptionMethods) ... ok
test_caesar_25_symmetric (test_pseudocryption.TestPseudocryptionMethods) ... ok
test_caesar_6 (test_pseudocryption.TestPseudocryptionMethods) ... ok
test_caesar_null (test_pseudocryption.TestPseudocryptionMethods) ... ok
test_caesar_types (test_pseudocryption.TestPseudocryptionMethods) ... ok
test_make_encrypt_rot1 (test_pseudocryption.TestPseudocryptionMethods) ... ok
test_make_encrypt_rot13 (test_pseudocryption.TestPseudocryptionMethods) ... ok
test_make_encrypt_rot1_docstring (test_pseudocryption.TestPseudocryptionMethods) ... ok
test_make_encrypt_rot2 (test_pseudocryption.TestPseudocryptionMethods) ... ok
test_rot13 (test_pseudocryption.TestPseudocryptionMethods) ... ok
test_rot13_circle (test_pseudocryption.TestPseudocryptionMethods) ... ok
test_rot13_types (test_pseudocryption.TestPseudocryptionMethods) ... ok
test_substitution (test_pseudocryption.TestPseudocryptionMethods) ... ok
test_substitution_null (test_pseudocryption.TestPseudocryptionMethods) ... ok
test_substitution_types (test_pseudocryption.TestPseudocryptionMethods) ... ok
test_xor_A (test_pseudocryption.TestPseudocryptionMethods) ... ok
test_xor_AAAA (test_pseudocryption.TestPseudocryptionMethods) ... ok
test_xor_types (test_pseudocryption.TestPseudocryptionMethods) ... ok

----------------------------------------------------------------------
Ran 18 tests in 0.001s

OK
```