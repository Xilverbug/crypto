from AES_OFB import encrypt_ofb

#Decrypt the data below.

enc_str = "2114a82cb329e49aae9acc905db864624b78990d71813f509c5b9a726eb3"

# AES-OFB Encryption Service
secret = b'A'*30
ciphertext = encrypt_ofb(secret)
print("AAA", ciphertext)

''''''

enc2_str = '343d8c4d9d1dd1ab9aafadb7799c41416b5ab36c188f3853f43ab65c4b97'

enc2_str = bytes.fromhex(enc2_str)
enc_str = bytes.fromhex(enc_str)


stream_key = ''

for c1, c2 in zip(enc2_str, secret) :
    stream_key = stream_key + chr(c1 ^ c2)


plantext = ''
for c1, c2 in zip(enc_str, stream_key) :
    plantext = plantext + chr(c1 ^ ord(c2))


print("Plantext : ", plantext)
''''''