import logging
from typing import List, Tuple

from table_crypt import tabular_cipher_encrypt, tabular_cipher_decrypt
from vigenere_crypt import vigenere_encrypt, vigenere_decrypt

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def combined_encryption(text: str, vigenere_key: str, tabular_key: str) -> List[Tuple[int, int, bool, bool]]:
    logging.debug(f"combined_encryption started with text: {text[:50]}..., vigenere_key: {vigenere_key}, tabular_key: {tabular_key}")
    # First, encrypt with Vigenère cipher
    vigenere_encrypted = vigenere_encrypt(text, vigenere_key)

    # Then, encrypt with Tabular cipher
    tabular_encrypted = tabular_cipher_encrypt(vigenere_encrypted, tabular_key)

    logging.debug(f"combined_encryption result: {tabular_encrypted[:50]}...")
    return tabular_encrypted

def combined_decryption(encrypted_text: List[Tuple[int, int, bool, bool]], vigenere_key: str, tabular_key: str) -> str:
    logging.debug(f"combined_decryption started with encrypted_text: {encrypted_text[:50]}..., vigenere_key: {vigenere_key}, tabular_key: {tabular_key}")
    # First, decrypt with Tabular cipher
    tabular_decrypted = tabular_cipher_decrypt(encrypted_text, tabular_key)

    # Then, decrypt with Vigenère cipher
    vigenere_decrypted = vigenere_decrypt(tabular_decrypted, vigenere_key)

    logging.debug(f"combined_decryption result: {vigenere_decrypted[:50]}...")
    return vigenere_decrypted
