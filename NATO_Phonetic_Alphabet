import pandas as pd
import numpy as np
from pyrfc3339 import generate

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetics = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetics():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetics[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in english alphabet please.")
        generate_phonetics()
    else:
        print(output_list)
        
generate_phonetics()
