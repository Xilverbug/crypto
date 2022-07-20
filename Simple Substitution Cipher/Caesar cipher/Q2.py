def decrypt_bruteforce(text):
    output = ""

    # Modify Code... Plz
    for ch in text:
        x = ord(ch) - 65
        n = 3
        c = ((x+n) % 26)
        output = output + chr(c + 65)

    return output


ciphertext = "PFJMIBQPRYPQFQRQFLKQZFMEBO"

plaintext = decrypt_bruteforce(ciphertext)

print('Encrypt : ', ciphertext)
print('Decrypt : ', plaintext)

