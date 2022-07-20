from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt_ofb(msg) :
    if type(msg) is not bytes:
        raise Exception("[Error] The msg type must be bytes.")

    key = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_OFB)
    cipher_text = cipher.encrypt(msg)

    return cipher_text.hex()

