import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters


chars = list(chars)
key = chars.copy()

random.shuffle(key)



# print(f"Characters: {chars}")
# print(f"Key: {key}")


# encryption

plain_text = input("Enter the text to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    # print (index)
    # key = key[index]
    # print(key)
    cipher_text += key[index]

print(f"Plain text: {plain_text}")

print(f"Cipher text: {cipher_text}")


# decryption

cipher_text = input("Enter the text to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    # print (index)
    # key = key[index]
    # print(key)
    plain_text += chars[index]

print(f"Cipher text: {cipher_text}")

print(f"Plain text: {plain_text}")