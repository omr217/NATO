import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
user_name = input("What is your name?:\n").upper()
output_list = [new_dict[letter] for letter in user_name]
print(output_list)