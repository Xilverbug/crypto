from random import randbytes
from Crypto.Cipher import AES

def encrypt(msg):
    key = randbytes(16)

    iv = b"\x00" * 16

    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    enc = cipher.encrypt(msg)

    return enc.hex()


msg = b"\x00" * 16

for i in range(255):
    cipher = encrypt(msg)
    print(cipher)

