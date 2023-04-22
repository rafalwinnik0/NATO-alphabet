# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
# for (key, value) in student_dict.items():
#     pass
# for (index, row) in student_data_frame.iterrows():
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 16
# }
#
# weather_f = {day: (temp_c*9/5) + 32 for day, temp_c in weather_c.items()}
# print(weather_f)

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:

new_dict = {row.letter: row.code for index, row in data.iterrows()}
print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter the word").upper()


