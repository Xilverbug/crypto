import AES_EBC

'''
msg --> msg + salt

Encrypt(msg + Salt)
'''
msg = b"Hello World"

ret = AES_EBC.Encrypt(msg)
print(ret)


