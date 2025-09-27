def encrypt_z26(plaintext, k):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ''
    for char in plaintext.upper():
        if char.isalpha():
            p = alphabet.index(char)
            c = (p + k) % 26
            ciphertext += alphabet[c]
        else:
            ciphertext += char
    return ciphertext

plaintext = "LIEN"
k = 29  
ciphertext = encrypt_z26(plaintext, k)
print("Ciphertext:", ciphertext)
