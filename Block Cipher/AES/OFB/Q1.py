from AES_OFB import encrypt_ofb

#Decrypt the data below.

enc_str = b"2114a82cb329e49aae9acc905db864624b78990d71813f509c5b9a726eb3"

# AES-OFB Encryption Service
secret = b'Example'
ciphertext = encrypt_ofb(secret)
print(ciphertext)

