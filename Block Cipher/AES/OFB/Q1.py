from AES_OFB import encrypt_ofb

#Decrypt the data below.

enc_str = b"a92bf9a24a1c39037d30421307e9f54f81871dc134972cca32517658df1b44e2331b7346b98c0e183ad46af3"

# AES-OFB Encryption Service
secret = b'Example'
ciphertext = encrypt_ofb(secret)
print(ciphertext)

