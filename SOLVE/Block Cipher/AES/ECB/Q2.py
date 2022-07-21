import AES_EBC

msg = b""

# 1. Length Check
'''
for i in range(16) :
    msg = msg + b"A"
    ret = AES_EBC.Encrypt(msg)
    print(i, ret)
'''
# "A"*7 + "XXXXXXXXXX" # 16byte
# "XXXXXXXXXX" + "\x10" * 16

# 1c0c483ee773680edae72ddbfb2dae54
# 5384d4737451cbb97a1698e377913569

# 2. Second Block Check
'''
ret = AES_EBC.Encrypt(b"\x10"*16)
print(ret)
# 5384d4737451cbb97a1698e377913569  # \x10 * 16
# ab91714c887851aea5012c657acc158c  # SECRET DATA + padding
'''


# 3. Shift...
# First Block  : A * 8 + SERECT(10 - 1 byte)
# Second Block : SERECT(last 1 byte) + padding
'''
ret = AES_EBC.Encrypt(b"A"*8) 
print(ret)

# First Block : 408639bed12984e7e2f68200ec71e06d
# Second Block :91f62cdfe52c49529fb035c00cd8b0b8 <-- last 1 byte + padding(0x0f)
'''


#4. BruteForce
# First Block : "X" + 0x0f*15
'''
for i in range(255) :
    msg = i.to_bytes(1, byteorder='big') + b'\x0f'*15
    #print("Input" + msg.hex())
    ret = AES_EBC.Encrypt(msg) 
    if "91f62cdfe52c49529fb035c00cd8b0b8" in ret :
        print(chr(i), ret)

# k 91f62cdfe52c49529fb035c00cd8b0b8ab91714c887851aea5012c657acc158c
'''

# 3-1. Shift...
# First Block  : A * 9 + SERECT(10 - 1 byte)
# Second Block : SERECT(last 1 byte) + padding
'''
ret = AES_EBC.Encrypt(b"A"*9) 
print(ret)

# First Block : d6f10a8b5c3a3ce8aabf4cc366095fa4
# Second Block :10df3bfc831a6496379b225523d68ecf <-- last 2 byte + padding(0x0f)
'''

#4-1. BruteForce
# First Block : "X" + 0x0f*15
'''
for i in range(255) :
    msg = i.to_bytes(1, byteorder='big') + b'k' +  b'\x0e'*14
    #print("Input" + msg.hex())
    ret = AES_EBC.Encrypt(msg) 
    if "10df3bfc831a6496379b225523d68ecf" in ret :
        print(chr(i), ret)

# c 10df3bfc831a6496379b225523d68ecf0290fc5b39ae1782b803c5e2f9e4f633
# k 91f62cdfe52c49529fb035c00cd8b0b8ab91714c887851aea5012c657acc158c
'''

# 
''''''
SECRET = b''
l = 8
for k in range(15, 0, -1):
    CipherText = AES_EBC.Encrypt(b"A"*l) 
    for i in range(255) :
        msg = i.to_bytes(1, byteorder='big') + SECRET +  k.to_bytes(1, byteorder='big')*k

        ret = AES_EBC.Encrypt(msg) 
        if CipherText[32:] in ret[:32] :
            print(chr(i), ret)
            SECRET = i.to_bytes(1, byteorder='big') + SECRET
            break

    l = l + 1

print(SECRET)
''''''
