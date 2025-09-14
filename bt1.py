def caesar_cipher(text, k):
    result = ""
    for char in text:
        if char.isalpha():  # nếu là chữ cái
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + k) % 26 + base)
        else:
            result += char
    return result

# Thông tin bài
k = 29  # STT
plaintext = "Lien"  # tên bạn (không dấu)

# Vì 29 % 26 = 3
ciphertext = caesar_cipher(plaintext, k)
print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext)
