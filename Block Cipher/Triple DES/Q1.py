from Crypto.Cipher import DES

key = "SANGUNIV"
cipher = DES.new(key, DES.MODE_ECB)

# cipher.encrypt
# cipher.decrypt