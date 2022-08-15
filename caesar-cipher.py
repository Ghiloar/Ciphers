from string import ascii_lowercase

key = int(input('key: '))
plain_text = list(input('plaintext: '))
cipher_text = []

plain_alphabet = list(ascii_lowercase)
# plain_alphabet length isn't given for granted
# so that symbols and numbers can be added to
# plain_alphabet
length = len(plain_alphabet)
cipher_alphabet = [plain_alphabet[(i+key)%length] for i in range(length)]

for i in plain_text:
    cipher_text.append(cipher_alphabet[plain_alphabet.index(i)])

print(''.join(cipher_text))