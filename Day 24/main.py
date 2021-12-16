NAMESPACE = "[name]"

with open("./Input/Names/invited_names.txt") as name_list:
    names = name_list.readlines()


with open("./Input/Letters/starting_letter.docx") as starting_letter:
    letter = starting_letter.read()


for name in names:
    striped_name = name.strip()
    replaced_letter = letter.replace(NAMESPACE, striped_name)
    with open(f"./Output/ReadyToSend/letter_for_{striped_name}.docx", mode="w") as completed_letter:
        completed_letter.write(letter)




