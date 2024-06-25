import random
import string
from uuid import uuid4


class Crypto:
  
  
  def __init__(self):
    self.uuid = str(uuid4())
    
 
    self.chars = list(" " + string.punctuation + string.ascii_letters + string.digits)
    self.key =   self.chars[:] 
    random.shuffle(self.key)
  
  
  def encrypt(self,text_to_encrypt,key):
    '''encrypt method requires plan text to encrypt and key'''
    
    cipher_text = ""
    for letter in text_to_encrypt:
      index = (self.chars.index(letter))
      cipher_text += key[index]
    return((self.uuid)[:18] + cipher_text + (self.uuid)[18:])
    
    
  def decrypt(self,text_to_decrypt,key):
    '''encrypt method requires cipher text to decrypt and key'''
    if self.uuid[:18] in text_to_decrypt and self.uuid[18:]  in text_to_decrypt:
      
      text_to_decrypt_length = len(text_to_decrypt)
      plain_text = ""
      text_to_decrypt = text_to_decrypt[18:text_to_decrypt_length-18]  
      for letter in text_to_decrypt:
        index = (key.index(letter))
        plain_text += self.chars[index]
      return(plain_text)
    else:
      raise ValueError("Enter Cipher Text")
  


def main():
  
  ### Try The Following Code ###
  plain_text = 'My Name is Anas Knbar, I am a software developer'
  
  # make instance from the Crypto class
  crypto = Crypto()
  # generate key 
  key = crypto.key
  
  encrypted_text = crypto.encrypt(plain_text,key)
  decrypted_text = crypto.decrypt(encrypted_text,key)
  
  print("\nOriginal Text: "+plain_text+"\n\nencrypted text: "+encrypted_text+"\n\ndecrypted text: "+decrypted_text+"\n")
  
  


if __name__ == "__main__":
  main()