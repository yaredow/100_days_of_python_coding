students_score = input("Insert the score of students. separated by commas. ").split()
for n in range(0, len(students_score)):
    students_score[n] = int(students_score[n])
print(students_score)

highest_score = 0
for score in students_score:
    if score > highest_score:
        highest_score = score
print(highest_score)