from collections import Counter


# Function for encrypting text using the Vigenère cipher
def vigenere_encrypt(plaintext: str, key: str) -> str:
    ciphertext = []
    key = key.upper()
    plaintext = plaintext
    key_length = len(key)
    
    for i, char in enumerate(plaintext.upper()):
        if char.isalpha():  # Encrypt only alphabetic characters
            shift = ord(key[i % key_length]) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(char)  # If it's not a letter (e.g., space), leave it unchanged
    return ''.join(ciphertext)

# Function for decrypting text using the Vigenère cipher
def vigenere_decrypt(ciphertext: str, key: str) -> str:
    decrypted_text = []
    key = key.upper()
    ciphertext = ciphertext
    key_length = len(key)
    
    for i, char in enumerate(ciphertext.upper()):
        if char.isalpha():  # Decrypt only alphabetic characters
            shift = ord(key[i % key_length]) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)  # If it's not a letter, leave it unchanged
    return ''.join(decrypted_text)
