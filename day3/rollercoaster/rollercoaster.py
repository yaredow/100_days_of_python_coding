print("Welcome to the roalercoaster")
height = int(input("what is your height in cm? "))

if height >= 120:
	print("You can ride the rollercoaster.")
	age = int(input("What is your age? "))
	if age <= 12:
		print("please pay $5")
	elif age <= 18:
		print("please pay $7")
	else: 
		print("please pay $12")
else:
	print("Sorry you should come back when you are a little taller")

