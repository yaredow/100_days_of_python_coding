print("Welcome to the rollercoaster")
height = int(input("what is your height in cm? ") )
bill = 0
if height >= 120:
	print("You can ride the rollercoaster")
	age = int(input("What is your age? ") )
	if age < 12:
		bill = 5
		print("Child thicket is $5")
	elif age <= 18:
		bill = 7
		print("Youth thiket is $7")
	elif (age >= 40) and (age <= 45 ):
		bill = 0
		print("Your thicket is free")
	else:
		bill = 12
		print("adult thicket is $12")
		
		bill += 3
		print(f"Your totall bill is {bill}")  
else:
	print("You can't ride the rollercoaster")