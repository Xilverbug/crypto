from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b"1234567890123456" # 16 byte - AES128
iv =  b"1234567890123456"

BS = 16

msg = b"A"*16 + b"B"*16 + b"123456"
msg = pad(msg, 16)

aes = AES.new(key, AES.MODE_CBC, iv)
CipherText = aes.encrypt(msg)
print("Encryption : ", CipherText.hex())

CipherText = bytearray(CipherText)
PlainText = bytearray(msg)

#CipherText[8] = XXXXXXXXXXXXXXXXXXX 

CipherText = bytes(CipherText)

aes = AES.new(key, AES.MODE_CBC, iv)
PlanText = aes.decrypt(CipherText)

print("Decryption : ", PlanText)