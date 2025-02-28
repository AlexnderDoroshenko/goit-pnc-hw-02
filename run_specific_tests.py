import unittest
from test_all_crypt import TestEncryptionMethods

# Create a test suite for run tests in a specific order to get clear output logs.
suite = unittest.TestSuite()

# Add all test methods to the suite
suite.addTest(TestEncryptionMethods('test_vigenere_encryption'))
suite.addTest(TestEncryptionMethods('test_vigenere_decryption'))
suite.addTest(TestEncryptionMethods('test_simple_transposition_encryption'))
suite.addTest(TestEncryptionMethods('test_simple_transposition_decryption'))
suite.addTest(TestEncryptionMethods('test_double_transposition_encryption'))
suite.addTest(TestEncryptionMethods('test_double_transposition_decryption'))
suite.addTest(TestEncryptionMethods('test_tabular_cipher_encryption'))
suite.addTest(TestEncryptionMethods('test_tabular_cipher_decryption'))
suite.addTest(TestEncryptionMethods('test_combined_encryption'))
suite.addTest(TestEncryptionMethods('test_combined_decryption'))

# Run the test suite
runner = unittest.TextTestRunner()
runner.run(suite)
