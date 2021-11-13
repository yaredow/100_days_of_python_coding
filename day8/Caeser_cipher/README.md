## Caeser Cipher 
According to wikipedia a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

<b>Steps of creating the caeser cipher</b>
### step one: encryption 
* Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
* Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
* Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
### Step two: decryption
* Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
* Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
* Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
* 