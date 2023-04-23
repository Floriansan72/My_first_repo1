# Operatori_Conditionale
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.

#Exercitiul2
#2. Verifică și afișează dacă x este număr natural sau nu.
# X = 45
# if X >= 0 :
#     print("X este numar natural")
# else :
#     print("numarul nu este natural")
#
# X = int(input("Tasteaza un numar de tip integer: "))
# if X >= 0 :
#     print("X este numar natural")
# else :
#     print("numarul nu este natural")

# Exercitiul3
# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.

# X = int(input("Tasteaza un numar de tip integer: "))
# if X < 0 :
#     print("numarul X este negativ")
# elif X > 0 :
#     print("numarul X este pozitiv")
# else :
#     print("numarul X este neutru")

#Exercitiul4
# 4.Verifică și afișează dacă x este între -2 și 13.

# X = int(input("Tasteaza un numar de tip integer: "))
# if X > -2 and X < 13:
#      print(f"X = {X}")

# Exercitiul5
#5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.

# X = int(input("Tasteaza un numar de tip integer: "))
# Y = int(input("Tasteaza un alt numar de tip integer"))
# if (X-Y) < 5 :
    # print(f"Diferenta numerelor tastate este {X - Y} si este mai mica decat 5")

# Exercitiul6
# 6. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’

# X = int(input("Tasteaza un numar de tip integer: "))
# if  X < 5 :
#     print("TRUE")
# elif X < 27 :
#     print("FALSE")
# else :
#     print("TRUE")

# Exercitiul7
# x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.

# X = int(input("Tasteaza un numar de tip integer X = "))
# Y = int(input("Tasteaza un numar de tip integer Y = "))
#
# if X == Y:
#     print("X = Y")
# elif X > Y:
#     print("X este mai mare decat Y")
# else:
#     print("Y este mai mare decat X")

# Exercitiul8
# X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.

# X , Y , Z = input("tasteaza 3 numere intregi despartite de virgula : \n ").split(',')
# print(f"X= {X}\nY= {Y}\nZ= {Z}\n")
# if X == Y and Y != Z:
#     print("Triunghiul este isoscel")
# elif X != Y and Y == Z:
#     print("Triunghiul este isoscel")
# elif X != Y and X == Z:
#     print("Triunghiul este isoscel")
# elif X == Y and Y == Z:
#         print("Triunghiul este echilateral")
# else :
#     print("Triunghiul este oarecare")



# x = input("Latura1 triunghi = ")
# y = input("Latura2 triunghi = ")
# z = input("Latura3 triunghi = ")
# if x == y or x == z :
#     if y == z:
#         print("Triunghiul este echilateral")
#     else:
#         print("Triunghiul este isoscel")
# elif y == z:
#     print("Triunghiul este isoscel")
# else:
#     print("Triunghiul este oarecare")


# Exercitiul16

# 16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# Citește de la tastatură un int x
# Afișează stringul fără ultimele x caractere
# Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'

# phrase = "Coral is either the stupidest animal or the smartest rock"
# X = int(input("Tastati un numar X = "))
# Y = len(phrase)
# print(f"Lungimea stringului este Y = {Y}")
# if X > 0 and X < Y:
#     print(phrase[:Y-X])
# else:
#     print("Tasteaza un alt numar")

#Exercitiul17
# 17. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.

# phrase = "Coral is either the stupidest animal or the smartest rock"
# print(phrase[:5] + phrase[-5:])

#Exercitiul18
# 18. Același string.
# Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
# Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
# output: 'Coral is either the stupidest animal or the smartest'

phrase = "Coral is either the stupidest animal or the smartest rock"
idx = phrase.find("rock")
print(phrase[:idx])

#Exercitiul19
# 19. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# Ia numărul ghicit de la utilizator
# Verifică și afișează dacă utilizatorul a ghicit
# Vei avea 3 opțiuni
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# Ai ghicit. Felicitări! Ai ales x si zarul a fost y.


# import random
# dice_roll = random.randint(1, 6)
# dice_guess = int(input("Tasteaza numarul ghicit = "))
# if dice_guess < dice_roll:
#     print(f"Ai pierdut.Ai ales un numar mai mic.Ai ales {dice_guess} dar a fost {dice_roll}")
# elif dice_guess > dice_roll:
#     print(f"Ai ales un numar mai mare.Ai ales {dice_guess} dar a fost {dice_roll}")
# else:
#     print(f"Ai ghicit.Felicitari!Ai ales {dice_guess} si zarul a fost {dice_roll}")






