def decrypt_bruteforce(text):
    output = ""

    # Modify Code... Plz

    for i in range(25):
        output = ''
        for ch in text:
            x = ord(ch) - 65
            n = i
            c = ((x-n) % 26)
            output = output + chr(c + 65)

        print(output)


ciphertext = "PFJMIBQPRYPQFQRQFLKQZFMEBO"

plaintext = decrypt_bruteforce(ciphertext)

print('Encrypt : ', ciphertext)
print('Decrypt : ', plaintext)

