

letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''
    for char in plaintext:
        char = char.lower()
        if char != ' ':
            index = letters.find(char)
            if index == -1:
                ciphertext += char
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                ciphertext += letters[new_index]
        else:
            ciphertext += ' '
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for char in ciphertext:
        char = char.lower()
        if char != ' ':
            index = letters.find(char)
            if index == -1:
                plaintext += char
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num_letters
                plaintext += letters[new_index]
        else:
            plaintext += ' '
    return plaintext


def encrypt_decrypt(text, mode, key):
    result = ''
    letters = 'abcdefghijklmnopqrstuvwxyz'  # Assuming this was intended

    if mode == 'd':
        key = -key

    for letter in text:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = (index + key) % 26
                result += letters[new_index]
        else:
            result += ' '

    return result



print('*** CAESAR CIPHER PROGRAM (Tutorial Project)  ***')
print()

print('Do you want to encrypt or decrypt?')
user_input = input("e/d: ").lower()
print()

if user_input == 'e':
    print('Encryption mode selected.')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt_decrypt(text,user_input, key)
    print(f'CIPHERTEXT: {ciphertext}')
elif user_input == 'd':
    print('Decryption mode selected.')
    print()
    key = int(input('Enter the key  (1 through 26): '))
    text = input('Enter the text to decrypt: ')
    plaintext = encrypt_decrypt(text,user_input, key)
    print(f'PLAINTEXT: {plaintext}')
else:
    print("Invalid input. Please choose 'e' or 'd'.")
