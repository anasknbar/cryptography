from encryption import Crypto
import pytest

def test_1_encrypt_method():
  plain_text = 'this is a plain text for testing'
  
  crypto = Crypto()
  key = crypto.key
  
  encrypted_text = crypto.encrypt(plain_text,key)
  assert encrypted_text != plain_text

def test_2_encrypt_method():
  plain_text = 'this is a plain text for testing'
  
  crypto = Crypto()
  key = crypto.key
  
  encrypted_text = crypto.encrypt(plain_text,key)
  decrypted_text = crypto.decrypt(encrypted_text,key)
  
  assert encrypted_text != decrypted_text

def test_1_decrypt_method():
  plain_text = 'this is a plain text for testing'
  
  crypto = Crypto()
  key = crypto.key
  
  encrypted_text = crypto.encrypt(plain_text,key)
  decrypted_text = crypto.decrypt(encrypted_text,key)
  
  assert decrypted_text == plain_text
  
def test_2_decrypt_method():
  plain_text = 'this is a plain text for testing'
  
  crypto = Crypto()
  key = crypto.key
  
  encrypted_text = crypto.encrypt(plain_text,key)
  decrypted_text = crypto.decrypt(encrypted_text,key)
  
  assert encrypted_text != plain_text
  

  
def test_decrypt_method_with_not_encryoted_text():
  crypto = Crypto()
  key = crypto.key
  
  with pytest.raises(ValueError):
    decrypted_text = crypto.decrypt("some plain Text",key)
