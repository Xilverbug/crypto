from AES_CBC import decrypt



CipherText = bytes.fromhex("31323334353637383930313233343536672383a24337dc8a3564a200f21ee8c0") # IV + CipherText

decrypt(CipherText)
