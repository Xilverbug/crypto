from Crypto.Util.Padding import pad

MSG = b"A"*16
pad_msg = pad(MSG, 16)

print(pad_msg)