def transpose_with_key(plaintext, key):
    key_length = len(key)
    # Calculate the number of rows needed, adding padding if necessary
    num_rows = len(plaintext) // key_length + (1 if len(plaintext) % key_length != 0 else 0)
    padded_plaintext = plaintext.ljust(num_rows * key_length)  # Add padding to make the plaintext fit evenly
    
    # Create the matrix column by column
    matrix = ['' for _ in range(key_length)]
    for i in range(len(padded_plaintext)):
        matrix[i % key_length] += padded_plaintext[i]
    
    # Reorder the columns based on the alphabetical order of the key
    sorted_key = sorted(range(len(key)), key=lambda k: key[k])
    ciphertext = ''.join(matrix[i] for i in sorted_key)  # Reorder columns based on key
    
    return ciphertext

def transpose_with_key_decrypt(ciphertext, key):
    key_length = len(key)
    num_rows = len(ciphertext) // key_length
    remainder = len(ciphertext) % key_length
    
    # Get column order based on the sorted key
    sorted_key = sorted(range(len(key)), key=lambda k: key[k])
    
    # Create the columns array
    columns = ['' for _ in range(key_length)]
    idx = 0
    for i in sorted_key:
        column_length = num_rows + (1 if i < remainder else 0)
        columns[i] = ciphertext[idx:idx + column_length]
        idx += column_length
    
    # Rebuild the plaintext row by row
    decrypted_text = ''.join(''.join(columns[j][i] for j in range(key_length)) for i in range(num_rows))
    
    return decrypted_text.rstrip()  # Remove padding from the original plaintext

def double_transposition_encrypt(plaintext, key1, key2):
    # First transposition with key1
    intermediate_text = transpose_with_key(plaintext, key1)
    # Second transposition with key2
    final_ciphertext = transpose_with_key(intermediate_text, key2)
    return final_ciphertext

def double_transposition_decrypt(ciphertext, key1, key2):
    # First decryption with key2
    intermediate_text = transpose_with_key_decrypt(ciphertext, key2)
    # Second decryption with key1
    final_plaintext = transpose_with_key_decrypt(intermediate_text, key1)
    return final_plaintext.rstrip()  # Remove any remaining padding after double decryption

# Example usage
plaintext = "HELLO THIS IS A SECRET MESSAGE TO ENCRYPT"
key1 = "SECRET"
key2 = "KEYWORD"

# Encryption
ciphertext_1key = transpose_with_key(plaintext, key1)
print(f"Ciphertext for key {key1}:", ciphertext_1key)

ciphertext_2key = transpose_with_key(plaintext, key2)
print(f"Ciphertext for key {key2}:", ciphertext_2key)

ciphertext_double = double_transposition_encrypt(plaintext, key1, key2)
print("Ciphertext double keys:", ciphertext_double)

# Decryption
decryptedtext_1key = transpose_with_key_decrypt(ciphertext_1key, key1)
print(f"Decrypted Text for key {key1}:", decryptedtext_1key)

decryptedtext_2key = transpose_with_key_decrypt(ciphertext_2key, key2)
print(f"Decrypted Text for key {key2}:", decryptedtext_2key)

decrypted_text = double_transposition_decrypt(ciphertext_double, key1, key2)
print("Decrypted Text double keys:", decrypted_text)
