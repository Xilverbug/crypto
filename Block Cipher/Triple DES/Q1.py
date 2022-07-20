from Crypto.Cipher import DES

key = "1234567812345678"
cipher = DES.new(key, DES.MODE_ECB)

# cipher.encrypt
# cipher.decrypt