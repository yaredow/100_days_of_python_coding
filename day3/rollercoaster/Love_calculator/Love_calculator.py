print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


combined_name = name1 + name2
lower_combined_name = combined_name.lower()

t= lower_combined_name.count('t')
r= lower_combined_name.count('r')
u= lower_combined_name.count('u')
e= lower_combined_name.count('e')

true = t + r + u + e

l= lower_combined_name.count('l')
o= lower_combined_name.count('o')
v= lower_combined_name.count('v')
e= lower_combined_name.count('e')

love = l + o + v + e

true_love = int(str(true) + str(love) )
if true_love < 10 or true_love > 90:
  print(f"Your score is {true_love}, you go together like coke and mentos") 
elif int(true_love) >= 40 and int(true_love) <= 50:
  print(f"Your score is {true_love}, you are alright together")
else:
  print(f"Your score is {true_love}")
