#Functii

#Exercitiul_1

#1.Funcție care să calculeze și să returneze suma a două numere

# def sum_number(a, b):
#     return a + b
# total = sum_number(3, 4)
# print(f"Suma numerelor este : {total}")

# def sum_number(a=5, b=-3):
#     return a + b
# print(f"Suma numerelor este : {sum_number()}")

# def sum_number(a, b=8):
#     print(f" a = {a}")
#     print(f" b = {b}")
#     return a + b
# print(f"Suma numerelor este : {sum_number(4)}")

#2.Exercitiul_2

#2.2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar

# def number(a):
#     print(f"a = {a}")
#     if a % 2 == 0:
#          return "TRUE"
#     return "IMPAR"
# print(f"a este par: {number(2)}")

#3.Exercitiul_3

#3. Funcție care returnează numărul total de caractere din numele tău complet.
#(nume, prenume, nume_mijlociu)

# def my_name(nume = "Gabor", prenume = "Florian", nume_mijlociu = "Rica"):
#     print(f"Nume: {nume}")
#     print(f"Prenume: {prenume}")
#     print(f"Nume_mijlociu: {nume_mijlociu}")
#     return len(nume + prenume + nume_mijlociu)
# print(f"Total caractere: {my_name()}")

#Exercitiul_4

# 4. Funcție care returnează aria dreptunghiului

# def rectangular_area( lungime = 3, latime = 5):
#     print(f"Lungimea = {lungime}")
#     print(f"latime = {latime}")
#     return lungime * latime
# print(f"Aria dreptunghiului este : {rectangular_area()}")

#Exercitiul_5

#5. Funcție care returnează aria cercului

# def circle_area(raza = 5):
#     print(f"Raza cercului = {raza}")
#     PI = 3.14
#     return PI*(raza**2)
# print(f"Aria cercului este : {circle_area()}")

#Exercitiul_6

#6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.

# string_name = "dfkgjssorkj"
# x = "j"
#
# def find_caracter(x):
#     if string_name.count(x) != 0:
#         return "TRUE"
#     return "FALSE"
# print(f"{find_caracter(x)}")

#Exercitiul_7

# 7. Funcție fără return, primește un string și printează pe ecran:
# Numărul de caractere lower case este x
# Numărul de caractere upper case exte y

#string_name = input("Tastati un string  :\n")

# def get_case(x):
#     uppercase = lowercase = others = 0
#     for i in x:
#         if i.isupper():
#             uppercase +=1
#         elif i.islower():
#             lowercase +=1
#         else:
#             others +=1
#     print(f"The number of upper case is : {uppercase}")
#     print(f"The number of lower case is : {lowercase}")
#     print(f"the number of others is : {lowercase}")
#
# get_case(string_name)

#Exercitiul_8

# 8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.

# print("Alegeti cate numere intregi contine lista:")
# n = int(input("n = "))
# print("Tastati numerele intregi ale listei")
# list_of_numbers = []
# list_positive = []
# for i in range(n):
#     list_of_numbers.append(input("Elementul " + str(i) + " = " ))
# print(f"list_of_number = {list_of_numbers}")
#
# def get_positiv_numbers(x):
#     for element in x :
#         if int(element) >= 0:
#             list_positive.append(element)
#         continue
#     print(f"list_positive = {list_positive}")
# get_positiv_numbers(list_of_numbers)

#Exercitiul_9

# Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
# Primul număr x este mai mare decat al doilea număr y
# Al doilea număr y este mai mare decat primul număr x
# Numerele sunt egale.

# a = input("Tasteaza primul numar x =  ")
# b = input("Tasteaza al doilea numar y = ")
#
# def compering_numbers(x, y):
#     if x > y:
#         print(f"Primul numar x = {a} este mai mare dect al doilea numar y = {b}")
#     elif x < y:
#         print(f"primul numar x = {a} este mai mic dect al doilea numar y = {b}")
#     else:
#         print("Numerele sunt egale")
#
# compering_numbers(a, b)

#Exercitiul_10

# 10. Funcție care primește un număr și un set de numere.
# Printează ‘am adaugat numărul nou în set’ + returnează True
# Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False

# a = int(input("Tastati un numar a = "))
# print("Alegeti cate numere intregi contine setul:")
# n = int(input("n = "))
#
# print("Tastati numerele intregi ale setului")
# set_of_numbers = set()
# for i in range(n):
#     set_of_numbers.add(int(input()))
# print(f"set_of_number = {set_of_numbers}")
#
# def print_info( x , y):
#     print(f"x = {x}")
#     print(f"y = {y}")
#     len1 = len(y)
#     y.add(x)
#     z = y
#     len2 = len(y)
#     if len1 != len2:
#         print(f"Am adaugat numarul nou in set : {z}")
#         return print("TRUE")
#     else:
#         print(f"Nu am adaugat numarul in set.Acesta exista deja : {y}")
#         return print("FALSE")
#
# print_info(a, set_of_numbers)
#
# #11.Exercitiul_11

#11. Funcție care primește o lună din an și returnează câte zile are acea lună.

# month = input("Tastati o luna din an \n")
# dict_month = {
#     "ianuarie" : "31 zile" ,
#     "februarie" : "28 zile" ,
#     "martie" : "31 zile" ,
#     "aprilie" : "30 zile" ,
#     "mai" : "31 zile" ,
#     "iunie" : "30 zile" ,
#     "iulie" : "31 zile" ,
#     "august" : "31 zile" ,
#     "septembrie" : "30 zile" ,
#     "octombrie" : "31 zile" ,
#     "noiembrie" : "30 zile" ,
#     "decembrie" : "31 zile" }
# def get_month_day(x):
#     print(f"Luna {x} are {dict_month[x]} zile")
# get_month_day((month))

#12.Exercitiul_12

#12. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.

# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)

# x = float(input(f"Tastati un numar x = "))
# y = float(input("Tasatati al doliea numar y ="))
# def calculator(num1, num2):
#      a = num1 + num2
#      b = num1 - num2
#      c = num1 * num2
#      d = num1 / num2
#      return a, b, c, d
# a, b, c, d = calculator(x, y)
# print(("Suma: " , a))
# print(("Diferenta: ", b))
# print(("Inmultire: ", c))
# print(("Impartire: ", d))

#13.Exercitiul_13
# 13. Funcție care primește o listă de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0

import random
list_number = []
number = 0
for i in range(9):
    number = random.randint(0, 9)
    list_number.append(number)
print(f"Lista cifra = {list_number}")
dict_num = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0}
def count_number(x):
    for i in x:
        s = 0
        for j in range(9):
            if i == x[j]:
                s+=1
            dict_num[i] = s
    #print(f"dict_num = {dict_num}")
    return dict_num
count_number(list_number)
print(f"dict_num = {dict_num}")

# 14.Exercitiul_14
# 14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
#
# a = int(input(f"Numarul a = "))
# b = int(input(f"Numarul b = "))
# c = int(input(f"Numarul c = "))
#
# list_num = [a, b, c]
# def max_num(x):
#     return max(list_num)
# print(f"Maximul celor 3 numere este : {max(list_num)}")
#
# max_num(list_num)
# maxim = 0
# def max_num(x, y, z):
#     maxim = max(x, y, z)
#     return maxim
# print(f"Maximul celor 3 numere este : {maxim}")
#
# max_num(a, b, c)

#15.Exercitiul_15
# 15. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
# Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)

# a = int(input(f"Tastati un numar a = "))
# def sum_num(x):
#     s = 0
#     for i in range(x+1):
#         s +=i
#     return print(f"Suma numerelor pana la {a} este : {s}")
# sum_num(a)


#16.Exercitiul_16
#16.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
#
# def common_numbers(x, y):
#     list3 = []
#     for i in range(len(list1)):
#         if x[i] in y:
#             list3.append(x[i])
#     return print(list3)
# common_numbers(list1, list2)

#17.Exercitiul_17
# 17. Funcție care să aplice o reducere de preț.
# Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
# Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.

# price = 100.45
# discount_proccent = 50.1
# def discount_price(x):
#     discount = discount_proccent / 100
#     if discount <= 1 or price < 0:
#         new_price = price - price * discount
#         return print(f"Noul pret cu discount de {discount_proccent} % este {new_price}")
#     else:
#         return print(f"Nu se poate acorda un discount proccent = {discount_proccent} %")
# discount_price(price)

#19.Exercitiul_19
# 19. Funcție care să afișeze câte zile mai sunt până la ziua ta
# / sau până la Crăciun dacă nu vrei să ne zici cand e ziua ta :)

birthday = int(input("Tastati ziua de nastere zn = "))
month_of_bith = int(input("Tastati luna de nastere ln = "))
this_day = int(input("Tastati ziua curenta zc  = "))
this_month = int(input("Tastati luna curenta lc = "))
dict_year = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
    }
# def count_of_birtday(zn,ln,zc,lc):
#     if ln == lc and zc > zn:
#         day_of_birth = 365 - (zc-zn)
#     elif ln == lc and zc <= zn:
#         day_of_birth = zn - zc
#         return print(f"Mai sunt {day_of_birth} pana la ziua ta")
#     else:
#         sum1 = 0
#         for i in range(ln, lc):
#             sum1 = sum1 + dict_year[i]
#             print(sum1)
#         day_of_birth = 365 - sum1 - (zc-zn)
#     return print(f"Mai sunt {day_of_birth} pana la ziua ta")
# count_of_birtday(birthday, month_of_bith, this_day, this_month)



