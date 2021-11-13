alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def Caeser(Start_text, shift_amount, cipher_direction):
  end_text = ""
  for letter in Start_text:
    position = alphabet.index(letter)
    if cipher_direction == "encode":
      new_position = position + shift_amount
    else:
      new_position = new_position = position - shift_amount
    end_text += alphabet[new_position]  
  print(f"The {cipher_direction}d text is {end_text}")

Caeser(Start_text=text, shift_amount=shift, cipher_direction=direction)