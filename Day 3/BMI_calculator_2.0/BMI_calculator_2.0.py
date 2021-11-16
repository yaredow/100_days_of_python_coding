print("Welcome to BMI 2.0")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round(weight / height ** 2)

if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are unerweight")
elif (BMI < 25):
  print(f"Your BMI is {BMI}, you have normal weight")
elif (BMI < 30): 
    print(f"Your BMI is {BMI}, you are slightly overweight")
elif (BMI < 35):
  print("Your BMI is {BMI}, you are obese")
else:
  print(f"Your BMI is {BMI}, You are clincally obese") 


