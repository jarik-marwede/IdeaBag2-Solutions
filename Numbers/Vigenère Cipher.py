#!/usr/bin/env python3
"""
Title:
Vigenère Cipher

Description:
Make a program to accept some plaintext and a key from the user
and use them to perform a Vigenère Cipher and output the result.
More info on Vigenère Ciphers:
https://en.m.wikipedia.org/wiki/Vigenère_cipher
Bonus points:
Give the user a message if their input is invalid
(empty/just numbers/etc)
Submitted by Imperial_Squid
"""


def vigenere_table() -> tuple:
    """Return vigenère table
    """
    alphabet = ("a", "b", "c", "d", "e", "f",
                "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r",
                "s", "t", "u", "v", "w", "x",
                "y", "z")
    result = [alphabet, ]
    for shift in range(1, 26):
        result.append(alphabet[shift:] + alphabet[:shift])
    return tuple(result)


def get_key(string: str, key: str) -> str:
    """Return key repeated to fit the length of string
    """
    full_key = key
    while len(full_key) < len(string):
            if len(full_key + key) <= len(string):
                full_key += key
            # if adding key would make full_key longer than string
            else:
                full_key += key[:len(string) - len(full_key)]
    return full_key


def encrypt(string: str, key: str) -> str:
    """Return encrypted version of string using key
    """
    if not isinstance(string, str):
        raise TypeError("Expected type 'str', "
                        "got type '{}'".format(type(string)))
    if not isinstance(key, str):
        raise TypeError("Expected type 'str', "
                        "got type '{}'".format(type(key)))
    if string == "":
        raise ValueError("String can not be empty")
    if key == "":
        raise ValueError("Key can not be empty")
    alphabet = ("a", "b", "c", "d", "e", "f",
                "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r",
                "s", "t", "u", "v", "w", "x",
                "y", "z")
    full_key = get_key(string, key)
    table = vigenere_table()
    result = ""
    for index, character in enumerate(string):
        for row in table:
            if row[0] == full_key[index]:
                current_row = row
                break
        else:
            continue
        if character.lower() not in alphabet:
            result += character
        elif character.lower() != character:
            result += current_row[alphabet.index(character.lower())].upper()
        else:
            result += current_row[alphabet.index(character.lower())]
    return result


if __name__ == "__main__":
    while True:
        STRING = input("Please input the string you want to encrypt: ")
        KEY = input("Please input the encryption key: ")
        try:
            print("Encrypted: " + encrypt(STRING, KEY))
        except ValueError:
            print("Please make sure your input is correct.")
        print("")
