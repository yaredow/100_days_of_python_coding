#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to tip calculator")
bill = float(input("what was the total bill $ "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? ")
numb_people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
total_bill_per_person = total_bill / numb_people
print(f"Each person should pay: {total_bill_per_person}")
 


