NAMESPACE = "[name]"

with open("./Input/Names/invited_names.txt") as name_list:
    names = name_list.readlines()

with open("./Input/Letters/starting_letter.docx") as starting_letter:
    letter = starting_letter.read()

for name in names:
    replaced_letter = letter.replace(NAMESPACE, name)


