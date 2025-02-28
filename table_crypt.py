import logging
from typing import List, Tuple

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_matrix(key: str, row_len: int = 5, col_len: int = 5) -> List[List[str]]:
    logging.debug(f"generate_matrix started with key: {key}, row_len: {row_len}, col_len: {col_len}")
    key = key.upper().replace('J', 'I')  # Handle 'J' as 'I'
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # 'J' is excluded
    matrix = []
    used = set()

    # Fill the matrix with the key characters first
    for char in key:
        if char not in used:
            used.add(char)
            matrix.append(char)

    # Fill the matrix with the rest of the alphabet
    for char in alphabet:
        if char not in used:
            used.add(char)
            matrix.append(char)

    # Ensure the matrix has the exact size defined by row_len and col_len
    if len(matrix) < row_len * col_len:
        for char in alphabet:
            if char not in used:
                used.add(char)
                matrix.append(char)

    # Create the matrix as a list of lists (2D)
    matrix_2d = [matrix[i:i+col_len] for i in range(0, row_len * col_len, col_len)]
    logging.debug(f"generate_matrix result: {matrix_2d}")
    return matrix_2d

def tabular_cipher_encrypt(text: str, key: str) -> List[Tuple[int, int, bool, bool]]:
    logging.debug(f"tabular_cipher_encrypt started with text: {text[:50]}..., key: {key}")
    matrix = generate_matrix(key)
    encrypted_text = []

    for char in text:
        if char.isalpha():  # Only encrypt alphabetic characters
            upper_char = char.upper()
            is_j = upper_char == 'J'
            upper_char = upper_char.replace('J', 'I')
            for row_idx, row in enumerate(matrix):
                if upper_char in row:
                    col_idx = row.index(upper_char)  # Get the column index
                    encrypted_text.append((row_idx, col_idx, char.islower(), is_j))  # Store row, column indices, case, and 'J' flag
                    break
        else:
            encrypted_text.append(char)  # Keep non-alphabetic characters as is

    logging.debug(f"tabular_cipher_encrypt result: {encrypted_text[:50]}...")
    return encrypted_text

def tabular_cipher_decrypt(encrypted_text: List[Tuple[int, int, bool, bool]], key: str) -> str:
    logging.debug(f"tabular_cipher_decrypt started with encrypted_text: {encrypted_text[:50]}..., key: {key}")
    matrix = generate_matrix(key)
    decrypted_text = []

    for item in encrypted_text:
        if isinstance(item, tuple):  # Only decrypt tuples
            row_idx, col_idx, is_lower, is_j = item
            char = matrix[row_idx][col_idx]
            if is_j:
                char = 'J'
            decrypted_text.append(char.lower() if is_lower else char)  # Preserve original case
        else:
            decrypted_text.append(item)  # Keep non-alphabetic characters as is

    result = ''.join(decrypted_text)
    logging.debug(f"tabular_cipher_decrypt result: {result[:50]}...")
    return result
