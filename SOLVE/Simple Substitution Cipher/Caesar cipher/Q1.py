def encrypt(text):
    # Write
    output = ""

    # Write your encryption routine
    for ch in text:
        x = ord(ch) - 65
        n = 3
        c = ((x+n) % 26)
        output = output + chr(c + 65)

    return output

def decrypt(text):
    output = ""

    # Write your decryption routine
    for ch in text:
        x = ord(ch) - 65
        n = 3
        c = ((x-n) % 26)
        output = output + chr(c + 65)

    return output


text = input('ENC : ').upper()

ciphertext = encrypt(text)
plaintext = decrypt(ciphertext)

print('Encrypt : ', ciphertext)
print('Decrypt : ', plaintext)
