import random

symbols = {0: "Kő", 1: "Papír", 2: "Olló", 3: "Kilépés"}
player_s = 0
npc_s = 0

game = True
while game:
    print("--- Kő, papír, olló játék ---")
    print("""0 - Kő
    1 - Papír
    2 - Olló
    3 - Kilépés""")
    print(f"Játékos: {player_s}, NPC: {npc_s}")
    print()
    player_c = int(input("Válassz egyet: "))
    npc_c = random.randint(0,2)

    print(f"Játékos: {symbols[player_c]}")
    print(f"NPC: {symbols[npc_c]}")

    if ((player_c == 0 and npc_c == 2) or
        (player_c == 1 and npc_c == 0) or
        (player_c == 2 and npc_c == 1)):
        print("Jákékos nyert!")
        player_s += 1
    elif ((player_c == 0 and npc_c == 0) or
        (player_c == 1 and npc_c == 1) or
        (player_c == 2 and npc_c == 2)):
        print("Egyenlő!")
    elif player_c == 3:
        print("Kilépés...")
        game = False
    else:
        print("NPC nyert!")
        npc_s += 1

