import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def phonetic_generator():
    user_input = input("Please insert your name: ").upper()
    try:
        output_list = [new_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry! only letters are allowed")
        phonetic_generator()
    else:
        print(output_list)


phonetic_generator()
