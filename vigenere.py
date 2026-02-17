#!/usr/bin/env python3

text = "Hello Mike"
key = "python"

def vigenere(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = " "
    key_index = 0

    for char in message.lower():
        if char == " ":
            encrypted_text += " "
        else:
            key_char = key[ key_index % len(key) ]
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]

    return encrypted_text

print(vigenere(text, key))
