import base64
from Crypto.Cipher import AES

# This function takes plaintext, key, IV.
# it encrypt the given plaintext using the given IV and key, then returns it.
def encryption(plaintext, key, IV):
    padding = 16 - (len(plaintext) % 16)
    plaintext += bytes([padding]) * padding
    cipher = AES.new(key, AES.MODE_CBC, IV)
    return cipher.encrypt(plaintext)

# This function takes plaintext, ciphertext, IV, and the key.
# it calles the encryption function and store the result into encrypted variable.
# the return value check whether encrypted == ciphertext
def check_key(plaintext, ciphertext, IV, key):
    encrypted = encryption(plaintext, key, IV)
    return encrypted == ciphertext

# Pads the given key (words coming from words.txt file) with '#' to be 16 byte length.
def padKey(key):
    return key.ljust(16, b'#')

# Given information
known_plaintext = b'This is a top secret.'
ciphertext = base64.b64decode(b'dkqia1Wk2mVN9rGeS84A9O0F4JNG+w52JYPLfaKsk6I=')
IV = bytes.fromhex('aabbccddeeff00998877665544332211')

# Opens the file and go through each word.
# if word length > 16 , go to next iteration.
# else, call check_key. check_key result is either true (if it is the correct key), or false(if it is not the key).
with open('words.txt', 'r') as f:
    for line in f:
        key = padKey(line.strip().encode())
        if len(key) > 16:
            continue
        if check_key(known_plaintext, ciphertext, IV, key):
            print(f'The key is: {key.decode()}')
            break