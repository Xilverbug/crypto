from Crypto.Util.Padding import pad

MSG = b"AAAAA"
pad_msg = pad(MSG, 16)

print(pad_msg)