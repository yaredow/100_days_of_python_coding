print("Welcome to average heigh calculator")
heights = input("Please insert the height of students\n").split()
for n in range(0, len(heights)):
    heights[n] = int(heights[n])
total_height = 0
for height in heights:
    total_height += height
# print(total_height)

num_students = 0
for student in heights:
    num_students += 1
# print(num_students)
average = round(total_height / num_students)
print(average)