import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def transpose_with_key(plaintext, key):
    logging.debug(f"transpose_with_key started with plaintext: {plaintext[:50]}..., key: {key}")
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
    
    logging.debug(f"transpose_with_key result: {ciphertext[:50]}...")
    return ciphertext

def transpose_with_key_decrypt(ciphertext, key, padding_clear=True):
    logging.debug(f"transpose_with_key_decrypt started with ciphertext: {ciphertext[:50]}..., key: {key}")
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
    decrypted_text = ''.join(''.join(columns[j][i] for j in range(key_length) if i < len(columns[j])) for i in range(num_rows))
    
    # Remove padding if the lengths differ
    if padding_clear:
        decrypted_text = decrypted_text.strip()
    
    logging.debug(f"transpose_with_key_decrypt result: {decrypted_text[:50]}...")
    return decrypted_text

def double_transposition_encrypt(plaintext, key1, key2):
    logging.debug(f"double_transposition_encrypt started with plaintext: {plaintext[:50]}..., key1: {key1}, key2: {key2}")
    # First transposition with key1
    intermediate_text = transpose_with_key(plaintext, key1)
    # Second transposition with key2
    final_ciphertext = transpose_with_key(intermediate_text, key2)
    logging.debug(f"double_transposition_encrypt result: {final_ciphertext[:50]}...")
    return final_ciphertext

def double_transposition_decrypt(ciphertext, key1, key2):
    logging.debug(f"double_transposition_decrypt started with ciphertext: {ciphertext[:50]}..., key1: {key1}, key2: {key2}")
    # First decryption with key2
    intermediate_text = transpose_with_key_decrypt(ciphertext, key2, False)
    # Second decryption with key1
    final_plaintext = transpose_with_key_decrypt(intermediate_text, key1)
    # Remove any remaining padding if the lengths differ
    logging.debug(f"double_transposition_decrypt result: {final_plaintext[:50]}...")
    return final_plaintext
