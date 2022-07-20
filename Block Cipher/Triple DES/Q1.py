import os
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

key = b"DESKEYDA12345678"
cipher = DES3.new(key, DES3.MODE_ECB)

enc = cipher.encrypt(pad(b'TEST', 16))
print(enc)

text = cipher.decrypt(enc)
print(unpad(text, 16))