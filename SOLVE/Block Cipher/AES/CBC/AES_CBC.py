from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def decrypt(ivmsg):
    key = b"1234567890123456"
    iv = ivmsg[:16]
    ciphertext = ivmsg[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    dec2 = cipher.decrypt(ciphertext)

    unpad(dec2, 16)
    print("[OK] Decript complate")


