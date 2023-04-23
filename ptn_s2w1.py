#Exercitiul_1
# 1. Declară o listă note_muzicale în care să pui do re mi etc până
# la do
# Afișeaz-o.
# Inversează ordinea folosind slicing și suprascrie această listă.
# Printează varianta actuală (inversată).
# Pe această listă aplică o metodă care bănuiești că face același
# lucru, adică să îi inverseze ordinea. Nu trebuie să o suprascrii
# în acest caz, deoarece metoda face asta automat.
# Printează varianta actuală a listei. Practic ai ajuns înapoi la
# varianta inițială.
#
# Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă
# va trebui să suprascrii lista sau să o salvezi într-o listă nouă.
# Metoda găsită de tine face suprascrierea automat și permanentizează
# aceste modificări. Ambele variante își găsesc utilitatea în funcție
# de ce ne dorim în acel moment.

# note_muzicale = ["do","re","mi","fa","sol","la","si","do"]
# print(note_muzicale)
# note_muzicale = note_muzicale[::-1]
# print(note_muzicale)
# note_muzicale.reverse()
# print(note_muzicale)

#Exercitiul_2
#2. De câte ori apare ‘do’?
# note_muzicale = ["do","re","mi","fa","sol","la","si","do"]
# print(f"do apare de {note_muzicale.count('do')}")

#Exercitiul_3
# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
#    Găsește 2 variante să le unești într-o singură listă.

# l1 = [3, 1, 0, 2]
# l2 = [6, 5, 4]
# #varianta_1 de unire a celor doua liste
# l1.append(l2[0])
# l1.append(l2[1])
# l1.append(l2[2])
# print(f"l = {l}")
# #varianta_2 de unire a celor doua liste
# l1[4] = l2[0]
# l1[5] = l2[1]
# l1[6] = l2[2]
# print(f"l = {l1}")
# #varainta_3 de unire a celor doua liste
# l1 = [3, 1, 0, 2]
# l2 = [6, 5, 4]
# print(f"l = {l1 + l2}")

#Exercitiul_4
# 4.
# Sortează și afișează lista generată la exercițiul anterior.
# Sortează numărul 0 folosind o funcție.
# Afișaza iar lista.

# l1 = [3, 1, 0, 2]
# l2 = [6, 5, 4]
# l = l1 + l2
# print(l)
# l.sort()
# print(l)
# def mod1(x):
#     return x % 3
# l.sort(key = mod1)
#print(l)

#Exercitiul_5
# 5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
# Lista este goală.
# Lista nu este goală.

# l = [3, 1, 0, 2, 6, 5, 4]
# if len(l) == 0:
#     print("Lista  este goala")
# else:
#    print("Lista nu este goala")

#Exercitiul_6
#6. Folosește o funcție care să șteargă lista de la exercițiul 3.

# l = [3, 1, 0, 2, 6, 5, 4]
# l.clear()
# print(l)

#Exercitiul_7
# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.

# l = [3, 1, 0, 2, 6, 5, 4]
# l.clear()
# if len(l) != 0:
#     print("Lista  nu este goala")
# print("Lista  este goala")

#Exercitiul_8
# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# lista_elevi = list(dict1.keys())
# print(dict1.keys())
# print(f"lista_elevi : {lista_elevi}")

#Exercitiul_9
# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie

# print(f"Ana a luat nota {dict1.get('Ana')}")
# print(f"Gigel a luat nota {dict1.get('Gigel')}")
# print(f"Dorel a luat nota {dict1.get('Dorel')}")

#Exercitiul_10
# 10. Dorel a făcut contestație și a primit 6
# Modifică nota lui Dorel în 6
# Printează nota după modificare

# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# dict1['Dorel'] = 6
# print(f"Dorel a avut nota 5, iar dupa contestatie are nota {dict1['Dorel']}")

#Exerctiul_11
# 11. Gigel se transferă din clasă
# Căuta o funcție care să îl șteargă
# Vine un coleg nou. Adaugă Ionică, cu nota 9
# Printează noii elevi

# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# del dict1['Dorel']
# print(dict1)
# dict1['Ionica'] = 9
# print(dict1)

#Exercitiul_13
13.
# Set
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# Adaugă în zilele_sapt ‘luni’
# Afișează zile_sapt

# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# zile_sapt.add('luni')
# print(zile_sapt)

#Exercitiul_14
# 14.Folosește un if și verifică dacă:
# Weekend este un subset al zilelor din săptămânii.
# Weekend nu este un subset al zilelor din săptămânii.

# if (zile_sapt.intersection(weekend)) == 0:
#     print("Weekend nu este un subset al zilelor saptamanii")
# print("Weekend este un subset al zilelor saptamanii")

#Exercitiul_15
#15. Afișează diferențele dintre aceste 2 seturi.

#print(zile_sapt.difference(weekend))

#Exercitiul_16
#16. Afișează intersecția elementelor din aceste 2 seturi.

#print(zile_sapt.intersection((weekend)))

#Exercitiul_12
# 12. Ne imaginăm o echipă de fotbal pt teren sintetic.
#  3 Schimbări maxime admise:
# Declară o Listă cu 5 jucători
# Schimbari_efectuate = te joci tu cu valori diferite
# Schimbari_max = 3
#
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# Efectuează schimbarea
# Șterge jucătorul scos din listă
# Adaugă jucătorul intrat
# Afișază a intrat x, a ieșit y, mai ai z schimbări
#
# Dacă jucătorul nu e în teren:
# Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
# Afișază ‘mai ai z schimbări’
#
# Testează codul cu diferite valori

# lista_jucatori = ['Alin','Marius','Bogdan','Daniel','Andrei']
# lista_rezerve = ['Dan','Calin','Ionel']
# schimbari_efectuate = 0
# schimbari_max = 3
# schimbari_ramase = schimbari_max - schimbari_efectuate
#
#
# jucator ='Alin'
# jucator_rezerva = [lista_rezerve[0]]
# print(jucator_rezerva)
# if jucator in lista_jucatori and schimbari_efectuate <= schimbari_max:
#     lista_jucatori.remove(jucator)
#     print(lista_jucatori)
#     schimbari_efectuate +=1
#     schimbari_ramase = schimbari_max - schimbari_efectuate
#     print(f"A intrat {lista_rezerve[0]}, a iesit {jucator} mai ai {schimbari_ramase} schimbari")
#     print(lista_jucatori + jucator_rezerva)
# else :
#     print(f"Nu se poate efectua schimbarea deoarece jucatorul {jucator} nu este in teren")
#     print(f"Mai ai {schimbari_ramase} schimbari")



















