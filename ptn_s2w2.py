#Exercitiul_1
# 1.Având lista:
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# Folosește un for că să iterezi prin toată lista și să afișezi;
# ‘Mașina mea preferată este x’.
# Fă același lucru cu un for each.
# Fă același lucru cu un while.

# for masina in masini:
#     print(f"Masina mea preferata este {masina}")

# idx = 0
# while idx < len(masini):
#     print(f"Masina mea preferata este {masini[idx]}")
#     idx+= 1
#
# for idx in range(len(masini)):
#     print(f"Masina mea preferata este {masini[idx]}")
# else:
#     print("AM terminat")

#Exercitiul_2py
# 2. Aceeași listă:
# Folosește un for else
# În for
# Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
# În else:
#   Printează lista.

# new_masini = []
# for idx in range(len(masini)):
#     if idx == 0:
#         continue
#     elif idx == len(masini)-1:
#         print(new_masini)
#         break
#     new_masini = new_masini + [masini[idx].upper()]
# #else:
# print([masini[0]] + new_masini + [masini[len(masini)-1]])

#Exercitiul_3
# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Iterează prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
#    Printează ‘am găsit mașina dorită de dvs’
#    Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
#    Printează ‘Am găsit mașina X. Mai căutam‘

# for masina in masini:
#     print(masina)
#     if masina == 'Mercedes':
#         print("Am gasit masina dorita de dvs")
#         break
#     else:
#         print(f"Am gasit masina {masina}. Mai cautam")

#Exercitiul_4
# 4. Aceeași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
#
# Dacă mașina e Trabant sau Lăstun:
#    Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
# Printează S-ar putea să vă placă mașina x.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina == 'Lastun' or masina == 'Trabant':
#         continue
#     print(f"S-ar putea sa va placa masina {masina}")

# idx = 0
# while idx < len(masini):
#     if masini[idx] == 'Lastun' or masini[idx] == 'Trabant':
#         idx +=1
#         continue
#     else:
#         print(f"S-ar putea sa va placa {masini[idx]}")
#         idx +=1
#         continue

#Exercitiul_5
# 5. Modernizează parcul de mașini:
#
# Crează o listă goală, masini_vechi.
# Iterează prin mașini.
# Când găsesti Lăstun sau Trabant:
# Salvează aceste mașini în masini_vechi.
# Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# Printează Modele vechi: x.
# Modele noi: x.

#masini_vechi = []
#masini_new = []
# for masina in masini:
#     if masina != 'Lastun':
#         if masina != 'Trabant':
#             masini_new = masini_new + [masina]
#         # print(masini_new)
#     if masina == 'Lastun' or masina == 'Trabant':
#         masini_vechi = masini_vechi + [masina]
#         # print(masini_vechi)
#         masini_new = masini_new + ['Tesla']
#         # print(masini_new)
# else:
#     print(f" Modele vechi : {masini_vechi}")
#     print(f" Modele noi : {masini_new}")

# masini_vechi = []
# masini_new = []
# idx = 0
# while idx in range(len(masini)):
#     if masini[idx] == 'Lastun' or masini[idx] == 'Trabant':
#         masini_vechi = masini_vechi + [masini[idx]]
#         #print(masini_vechi)
#         masini[idx] = ['Tesla']
#         masini_new = masini_new + masini[idx]
#         idx +=1
#         #print(masini_new)
#     else:
#         masini_new = masini_new + [masini[idx]]
#         #print(masini_new)
#         idx +=1
# else:
#     print(f" Modele vechi : {masini_vechi}")
#     print(f" Modele noi : {masini_new}")

# for idx in range(len(masini)):
#     if masini[idx] == 'Lastun' or masini[idx] == 'Trabant':
#         masini[idx] = 'Tesla'
#         continue
# else:
#     print(masini)

#Exercitiul_6
#6. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
# Vine un client cu un buget de 15000 euro.
# Prezintă doar mașinile care se încadrează în acest buget.
# Iterează prin dict.items() și accesează mașina și prețul.
# Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
# Iterează prin listă.
# for masina, pret in pret_masini.items():
#     if pret <= 15000:
#         print(f"Masina {masina} are pretul {pret}")

#Exercitiul_7

# 7. Având lista:
#numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterează prin ea.
# Afișează de câte ori apare 3 (nu ai voie să folosești count).

# idx = 0
# for numar in numere:
#     if numar == 3:
#         idx +=1
#     continue
# print(f"Numarul 3 apare de {idx} ori")

#Exercitul_8
# Aceeași listă:
# Iterează prin ea
# Calculează și afișează suma numerelor (nu ai voie să folosești sum).

#suma = 0
# for idx in range(len(numere)):
#     suma = suma + numere[idx]
# print(f" suma numerelor este : {suma}")

# for numar in numere:
#     suma = suma + numar
# print(f"Suma numerelor este: {suma}")

#Exercitiul_9
#9. Aceeași listă:
# Iterează prin ea.
# Afișază cel mai mare număr (nu ai voie să folosești max).

# max = 0
# for idx in range(len(numere)):
#     if numere[idx] > max:
#         max = numere[idx]
#         continue
# print(f"Numarul cel mai mare este: {max}")

#Exercitiul_10
# 10. Aceeași listă:
# Iterează prin ea.
# Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# Afișază noua listă.

# for idx in range(len(numere)):
#     if numere[idx] > 0:
#         numere[idx] = -numere[idx]
#         continue
# print(numere)

#Exercitiul_11
#alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișează cele 4 liste la final

# for numar in alte_numere:
#     if numar > 0:
#         numere_pozitive.append(numar)
#         if numar % 2 == 0:
#             numere_pare.append(numar)
#         else:
#             numere_impare.append(numar)
#     else:
#         numere_negative.append(numar)
#         continue
# print(f"Numere negative : {numere_negative}")
# print(f"Numere pozitive : {numere_pozitive}")
# print(f"Numere pare : {numere_pare}")
# print(f"Numere impare : {numere_impare}")

#Exercitiul_12
# 12. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici.
# li = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 43]
# for i in range(len(li)):
#     for j in range(i+1, len(li)):
#         print(j)
#         if li[i] > li[j]:
#             print(li)
#             print(li[i])
#             print(li[j])
#             li[i] , li[j] = li[j] , li[i]
#             print(li[i] , li[j])
            #print(li)
    #print(li)

#Exercitiu_13
# 13. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
#    User alege un număr
#    Programul îi spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitări! Ai ghicit!

#Exercitiul_14
# Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777

# x = int(input("Alege un numr : "))
# i = 1
# while i <= x :
#     j = str(i)
#     print(j * i)
#     i+=1

#Exercitiul_15
#15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)

#print(f"Lungimea listei este {len(tastatura_telefon)}")
for i in range(len(tastatura_telefon)):
    #print(tastatura_telefon[i])
    #print(len(tastatura_telefon[i]))
    for j in range(1):
        #print(j)
        print(f"Cifra curenta este : {tastatura_telefon[i][j]}")
















































