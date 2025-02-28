from collections import Counter


# Function for encrypting text using the Vigenère cipher
def vigenere_encrypt(plaintext: str, key: str) -> str:
    ciphertext = []
    key = key.upper()
    key_length = len(key)
    
    for i, char in enumerate(plaintext):
        if char.isalpha():  # Encrypt only alphabetic characters
            shift = ord(key[i % key_length]) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(char)  # If it's not a letter (e.g., space), leave it unchanged
    return ''.join(ciphertext)

# Function for decrypting text using the Vigenère cipher
def vigenere_decrypt(ciphertext: str, key: str) -> str:
    decrypted_text = []
    key = key.upper()
    key_length = len(key)
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():  # Decrypt only alphabetic characters
            shift = ord(key[i % key_length]) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)  # If it's not a letter, leave it unchanged
    return ''.join(decrypted_text)
