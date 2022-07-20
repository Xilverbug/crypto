from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b"1234567890123456" # 16 byte - AES128
msg = pad(b"Hello World", 16)

aes = AES.new(key, AES.MODE_ECB)
CipherText = aes.encrypt(msg)
print("Encryption : ", CipherText.hex())

aes = AES.new(key, AES.MODE_ECB)
PlanText = aes.decrypt(CipherText)

print("Decryption : ", PlanText)
print("Decryption : ", unpad(PlanText, 16))