# Weak keys in DES
import os
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad

IV = os.urandom(8)
SECRET = 'des_weak_key_crypto'


def encrypt(key, plaintext):
    try:
        key = bytes.fromhex(key)
        plaintext = bytes.fromhex(plaintext)

        cipher = DES3.new(key, DES3.MODE_ECB)
        ciphertext = cipher.encrypt(plaintext)

        return ciphertext.hex()

    except ValueError as e:
        return {"error": str(e)}


def encrypt_flag(key):
    return encrypt(key, pad(SECRET.encode(), 8).hex())


key = b"DESKEYDA12345678"

flag = encrypt_flag(key.hex())
cipher = encrypt(key.hex(), flag)
print(bytes.fromhex(cipher))