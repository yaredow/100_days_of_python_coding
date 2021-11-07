print("Welcome to average height calculator")
height_of_students = input("Please insert height of the students. separated by space.\n").split()
for n in range (0, len(height_of_students)):
    height_of_students[n] = int(height_of_students[n])
total_height = 0
for height in height_of_students:
    total_height += height 

num_of_students = 0
for student in height_of_students:
    num_of_students += 1  
average_height = total_height / num_of_students
print(average_height)