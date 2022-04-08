values = {"A E I O U L N R S T": 1 , "D G": 2 , "B C M P": 3 , "F H V W Y": 4 , "K": 5 , "J X": 8 , "Q Z": 10 , }

word = input("Enter a word to calculate it's value: ").upper()
word_value = 0

for char in word:
    for key in values:
        if char in key:
            word_value += values[key]
            break

print(f"The word {word} value was {word_value}.")
