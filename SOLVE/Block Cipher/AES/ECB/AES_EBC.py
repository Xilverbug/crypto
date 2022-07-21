from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def Encrypt(msg):
    if type(msg) is not bytes :
        raise Exception("[Error] The msg type must be bytes.")

    key = b"22S456A890K23456" # 16 byte - AES128

    msg = msg + b"EBCAttack"
    msg = pad(msg, 16)

    #print("DEBUG : ", msg.hex())

    aes = AES.new(key, AES.MODE_ECB)
    CipherText = aes.encrypt(msg)

    return CipherText.hex()