from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt():
    key = b"1234567890123456"
    iv = b"1234567890123456"
    msg = pad(b"Hello World", 16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    enc = cipher.encrypt(msg)

    return iv+enc

def decrypt(ivmsg):
    key = b"1234567890123456"
    iv = ivmsg[:16]
    ciphertext = ivmsg[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    dec2 = cipher.decrypt(ciphertext)

    dec = unpad(dec2, 16)

    return dec2



enc = encrypt()
print("ENC : ", enc.hex() )
iv = enc[:16]
ciphertext = enc[16:]

print("IV : ", iv.hex())


# Padding Error
'''
ciphertext = bytearray(ciphertext)
iv = bytearray(iv)
# Check Last byte(Padding..)
ciphertext[15] = ciphertext[15] ^ 8
ciphertext = bytes(ciphertext)
iv = bytes(iv)

try:
    dec = decrypt(iv+ciphertext)
except ValueError as e:
    print(e)
'''


# Last byte(Padding) - bruteforce
'''
org = iv[15]
for i in range(255):

    if org == i :
        continue

    # Check Last byte(Padding..)
    iv = bytearray(iv)
    iv[15] = i # Find 01 padiing
    iv = bytes(iv)

    try:
        decrypt(iv+ciphertext)
        print("Success : ", hex(i))
    except ValueError as e:
        pass
        #print(e)

# Result : 0x32
'''

'''
for i in range(255):

    iv = bytearray(iv)
    # Check Last byte(Padding..)
    # XX 02
    # Find 01 padiing, IV(Cipher n-1) 0x32 -> 0x01, 
    # BlockEnc[Last] = 0x32(Cipher n-1) ^ 0x01(Plantext) = 0x33(Block Decription) -->  0x33 ^ XX = 0x02 --> 0x33 ^ 0x02 = 0x31

    iv[15] = 0x31
    iv[14] = i # Find 02 padiing
    iv = bytes(iv)

    try:
        ret = decrypt(iv+ciphertext)
        print("Success : ", hex(i))
        print(ret.hex())
    except ValueError as e:
        pass
        #print(e)

# Result : 0x32
'''


''''''
for i in range(255):

    iv = bytearray(iv)
    # Check Last byte(Padding..)
    # XX 02
    # Find 01 padiing, IV(Cipher n-1) 0x32 -> 0x02, 
    # BlockEnc[Last] = 0x32(Cipher n-1) ^ 0x02(Plantext) = 0x30(Block Decription) -->  0x33 ^ XX = 0x02 --> 0x33 ^ 0x02 = 0x30

    iv[15] = 0x30 # 
    iv[14] = 0x33 # 
    iv[13] = i # Find Padding
    iv = bytes(iv)

    try:
        ret = decrypt(iv+ciphertext)
        print("Success : ", hex(i))
        print(ret.hex())
    except ValueError as e:
        pass
        #print(e)
''''''