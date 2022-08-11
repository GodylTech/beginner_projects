f = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
new_word = []

def encode():
    text_encode = input("Kódolni kívánt szöveg: ")
    word = list(text_encode)
    new_word = list(text_encode)
    level = int(input("Kódolás szintje: "))
    for i, a in enumerate(word):
        for b in f:
            if b == a:
                new_level = f.index(b)+level
                if new_level > len(f):
                    new_level = new_level-len(f)
                new_word[i] = f[new_level]
            elif a == " ":
                continue

    new_text = "".join(new_word)
    print("Kódolt szöveg:", new_text)
    
def decode():
    text_encode = input("Dekódolni kívánt szöveg: ")
    word = list(text_encode)
    new_word = list(text_encode)
    level = int(input("Dekódolás szintje: "))f = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
new_word = []

def encode():
    text_encode = input("Kódolni kívánt szöveg: ")
    word = list(text_encode)
    new_word = list(text_encode)
    level = int(input("Kódolás szintje: "))
    for i, a in enumerate(word):
        for b in f:
            if b == a:
                new_level = f.index(b)+level
                if new_level > len(f):
                    new_level = new_level-len(f)
                new_word[i] = f[new_level]
            elif a == " ":
                continue

    new_text = "".join(new_word)
    print("Kódolt szöveg:", new_text)
    
def decode():
    text_encode = input("Dekódolni kívánt szöveg: ")
    word = list(text_encode)
    new_word = list(text_encode)
    level = int(input("Dekódolás szintje: "))
    for i, a in enumerate(word):
        for b in f:
            if b == a:
                new_level = f.index(b)-level
                if new_level < 0:
                    new_level = len(f)-new_level
                new_word[i] = f[new_level]
            elif a == " ":
                continue

    new_text = "".join(new_word)
    print("Dekódolt szöveg:", new_text)

print("""
1 - Kódolás
2 - Dekódolás
0 - Kilépés""")

choice = int(input("Válassz: "))

if choice == 1:
    encode()
elif choice == 2:
    decode()
else:
    print("Kilépés")



    for i, a in enumerate(word):
        for b in f:
            if b == a:
                new_level = f.index(b)-level
                if new_level < 0:
                    new_level = len(f)-new_level
                new_word[i] = f[new_level]
            elif a == " ":
                continue

    new_text = "".join(new_word)
    print("Dekódolt szöveg:", new_text)

print("""
1 - Kódolás
2 - Dekódolás
0 - Kilépés""")

choice = int(input("Válassz: "))

if choice == 1:
    encode()
elif choice == 2:
    decode()
else:
    print("Kilépés")


