import re
def encrypt_message(message):
  encrypted_message=''
  for char in message:
    if char in message:
      if char.isalpha():
        shifted_char=chr(ord(char)+1)
        if char.isupper():
          if shifted_char>'Z':
            shifted_char='A'
        elif char.islower():
          if shifted_char>'z':
            shifted_char='a'
        encrypted_message+=shifted_char
      elif char.isdigit():
        encrypted_message+=str(int(char)+1)
      else:
        encrypted_message+=char
  return encrypted_message
message=input("Actual message: ")
print("Encrypted message: ",encrypt_message(message))