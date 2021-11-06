row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

x_direction = int(position[0])
y_direction = int(position[1])

selected_row = map[y_direction -1]
selected_row[x_direction - 1] = 'X'
# print the result
print(f"{row1}\n{row2}\n{row3}")
