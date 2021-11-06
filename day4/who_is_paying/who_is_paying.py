import random
name_people = input("insert the name of the people. separated by comma.")

names = name_people.split(",")
num_people = len(names)
random_choice = random.randint(0, num_people - 1)
person_about_to_pay = names[random_choice]
print(f"{person_about_to_pay} is going to pay today ")



