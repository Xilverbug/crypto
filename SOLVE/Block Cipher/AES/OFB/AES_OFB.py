from Crypto.Cipher import AES


def encrypt_ofb(msg) :
    if type(msg) is not bytes:
        raise Exception("[Error] The msg type must be bytes.")

    key = b'1234567890123456'
    iv = b'1234567890123456'

    cipher = AES.new(key, AES.MODE_OFB, iv=iv)
    cipher_text = cipher.encrypt(msg)

    return cipher_text.hex()

