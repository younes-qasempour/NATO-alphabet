import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row['letter']:row['code'] for (index, row) in df.iterrows()}

# while True:
#     user_input = input("Enter a word: ").upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in user_input]
#     except KeyError:
#         print("Invalid input")
#     else:
#         print(output_list)
#         break

def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Invalid input")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()