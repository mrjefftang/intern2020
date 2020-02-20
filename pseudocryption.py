#!/bin/env python3
import string

class InvalidInputError(RuntimeError):
    """ Invalid input error
    """
    pass

class ImplementMeError(NotImplementedError):
    """ Complete the implementation of this method to demonstrate
    your programming capabilities
    """
    pass

def encrypt_xor(key, plaintext):
    """ Encrypts the given plaintext by XORing each character with
    the key

    Parameters
    ----------
    key : str
        A string containing 1 character 
    plaintext : str
        The plain text message to encrypt

    Returns
    -------
    list
        The ciphertext generated from the encryption operation
    """
    raise ImplementMeError()


def encrypt_substitution(key, plaintext):
    """ Encrypts the given plaintext by substituting each letter
    in the plaintext with the corresponding position in the key

    Parameters
    ----------
    key : str
        A string containing the new alphabet consisting of both
        lowercase and uppercase letters.
    plaintext : str
        The plain text message to encrypt

    Returns
    -------
    list
        The ciphertext generated from the encryption operation
    """
    alphabet = string.ascii_letters
    raise ImplementMeError()


def encrypt_caesar(key, plaintext):
    """ Encrypts the given plaintext by substituting each letter
    in the plaintext with the corresponding position in the key

    See: https://en.wikipedia.org/wiki/Caesar_cipher

    You may use any previously implemented functions to implement
    this feature.

    Parameters
    ----------
    key : str
        A string containing the new alphabet consisting of both
        lowercase and uppercase letters.
    plaintext : str
        The plain text message to encrypt

    Returns
    -------
    list
        The ciphertext generated from the encryption operation
    """
    raise ImplementMeError()


def encrypt_rot13(plaintext):
    """ Encrypts the given plaintext by substituting each letter
    in the plaintext with the corresponding position in the key

    See: https://en.wikipedia.org/wiki/ROT13

    You may use any previously implemented functions to implement
    this feature.

    Parameters
    ----------
    key : str
        A string containing the new alphabet consisting of both
        lowercase and uppercase letters.
    plaintext : str
        The plain text message to encrypt

    Returns
    -------
    list
        The ciphertext generated from the encryption operation
    """
    raise ImplementMeError()


def make_encrypt_rotN(N):
    """ Generates a new encryption function similar to `encrypt_rot13`
    except will rotate the letters for the given N.

    Parameters
    ----------
    N : int
        A number containing the number of positions a letter should
        be shifted during the encryption (rotation) operation

    Returns
    -------
    function
        A function which will take 1 parameter (plaintext) and encrypt
        it by shifting letters N positions
    """
    raise ImplementMeError()
