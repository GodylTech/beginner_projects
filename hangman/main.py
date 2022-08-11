import random

fail = [0, 0, 0, 0, 0, 0, 0, 0, 0]

fail[0] = """
    o----o
         |
         |
         |
         |
         |
         |
    -----------
"""

fail[1] = """
    o----o
    |    |
         |
         |
         |
         |
         |
    -----------
"""

fail[2] = """
    o----o
    |    |
    O    |
         |
         |
         |
         |
    -----------
"""

fail[3] = """
    o----o
    |    |
    O    |
   /     |
         |
         |
         |
    -----------
"""

fail[4] = """
    o----o
    |    |
    O    |
   /|    |
         |
         |
         |
    -----------
"""

fail[5] = """
    o----o
    |    |
    O    |
   /|\   |
         |
         |
         |
    -----------
"""

fail[6] = """
    o----o
    |    |
    O    |
   /|\   |
    |    |
         |
         |
    -----------
"""

fail[7] = """
    o----o
    |    |
    O    |
   /|\   |
    |    |
   /     |
         |
    -----------
"""

fail[8] = """
    o----o
    |    |
    O    |
   /|\   |
    |    |
   / \   |
         |
    -----------
"""

with open("hangman_words.txt", "r", encoding="utf-8") as file:
    word = file.read()
    word_list = word.split(sep=";")

the_word = []
hitted_word = []
choiched_word = random.choice(word_list)
list_choice = list(choiched_word)
hitted_word = list(choiched_word)
fail_c = 0

for i in range(len(choiched_word)):
        the_word.append("_")

game = True
while game:
    print(fail[fail_c])
    print(*the_word)

    player_word = input("Válassz egy betűt: ")
    
    if player_word not in hitted_word:
        print("Nincs benne")
        fail_c += 1
        if fail_c == 8:
            print(fail[fail_c])
            print("Vége a játéknak")
            print("A keresett szó:", choiched_word)
            break

    for i, f in enumerate(choiched_word):
        if player_word == f:
            the_word[i] = f
            hitted_word[i] = "_"
            
    if "_" not in the_word:
        print(f"Kitaláltad a szót: {choiched_word}")
        break
