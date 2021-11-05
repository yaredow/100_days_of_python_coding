print('''
*******************************************************************************

      __________________
    .-'  \ _.-''-._ /  '-.
  .-/\   .'.      .'.   /\-.
 _'/  \.'   '.  .'   './  \'_
:======:======::======:======:  
 '. '.  \     ''     /  .' .'
   '. .  \   :  :   /  . .'
     '.'  \  '  '  /  '.'
       ':  \:    :/  :'
         '. \    / .'
           '.\  /.'   
             '\/'

*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

movement = input("You are at a crossroad. where do you want to go? type left or right? ").lower()

if movement == "left":
  wait_swim = input("There is an island in the middle of the lake. Type wait to wait for a boat or swim. ").lower()
  if wait_swim == "wait":
    door_to_open = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
    if door_to_open == "red":
      print("It's a room full of fire. Game Over.")
    elif door_to_open == "blue":
      print("You enter a room of beasts. Game Over.")
    elif door_to_open == "yellow":
      print("You found the treasure! You Win!")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("Game over! attacked by a trout")

else:
  print("Game Over! fall into a hole")

