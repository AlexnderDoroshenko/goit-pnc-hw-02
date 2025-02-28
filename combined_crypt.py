from typing import List, Tuple

from table_crypt import tabular_cipher_encrypt, tabular_cipher_decrypt
from vigenere_crypt import vigenere_encrypt, vigenere_decrypt


def combined_encryption(text: str, vigenere_key: str, tabular_key: str) -> List[Tuple[int, int, bool, bool]]:
    """
    Encrypt text using both Vigenère and tabular cipher methods in sequence.
    """
    # First, encrypt with Vigenère cipher
    vigenere_encrypted = vigenere_encrypt(text, vigenere_key)

    # Then, encrypt with Tabular cipher
    tabular_encrypted = tabular_cipher_encrypt(vigenere_encrypted, tabular_key)

    return tabular_encrypted


def combined_decryption(encrypted_text: List[Tuple[int, int, bool, bool]], vigenere_key: str, tabular_key: str) -> str:
    """
    Decrypt text using both Vigenère and tabular cipher methods in sequence.
    """
    # First, decrypt with Tabular cipher
    tabular_decrypted = tabular_cipher_decrypt(encrypted_text, tabular_key)

    # Then, decrypt with Vigenère cipher
    vigenere_decrypted = vigenere_decrypt(tabular_decrypted, vigenere_key)

    return vigenere_decrypted
