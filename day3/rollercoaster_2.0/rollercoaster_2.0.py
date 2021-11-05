print("Welcome to the roalercoaster")
height = int(input("what is your height in cm? "))

bill = 0

if height >= 120:
	print("You can ride the rollercoaster.")
	age = int(input("What is your age? "))
	if age <= 12:
        bill = 5
		print("Child thickets are $5")
        
	elif age <= 18:
        bill = 7
		print("Youth thickets are $7")
	else: 
        bill = 12
		print("Adult thicket are $12")

    photo = input("Do you want to take photo? Press Y for yes and N for no")
    if photo = "Y":
        bill += 3 
        print(f"The totall bill would be {bill}")
    else:
        print

else:
	print("Sorry you should come back when you are a little taller")


