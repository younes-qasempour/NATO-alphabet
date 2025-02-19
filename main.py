import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row['letter']:row['code'] for (index, row) in df.iterrows()}


user_input = input("Enter a word: ").upper()

x = [phonetic_dict[letter] for letter in user_input]
print(x)
