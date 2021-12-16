NAMEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_list:
    names = name_list.readlines()

with open("Input/Letters/starting_letter.docx") as letter_file:
    letter = letter_file.read()

for name in names:
    stripped_name = name.strip()
    replaced_letter = letter.replace(NAMEHOLDER, stripped_name)
    with open(f"Output/ReadyToSend/Letter_for_{stripped_name}.docx", mode="w") as completed_letter:
        completed_letter.write(replaced_letter)
