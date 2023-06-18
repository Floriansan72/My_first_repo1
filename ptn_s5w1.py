# 1.Singleton
# Se da următoarea clasa
class PresedinteRomania:

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'
#In momentul de fata, dacă încercăm să creăm mai multe obiecte din clasa aceasta, vom putea:

# a = PresedinteRomania()
# print(a)
# b = PresedinteRomania()
# print(b)
# a.say_hello()
# print(a.say_hello())
# print(b.say_hello())
#
# print(f'ID(a) = {id(a)}')
# print(f'ID(b) = {id(b)}')
# print(f'Acelasi obiect? {a is b}')

# Scopul acestui exercițiu este sa modificăm clasa de mai sus folosind DP Singleton
# pentru a obține mereu același obiect:
# Vom folosi functia `__new__` (adevăratul constructor din Python)
# Vom tine singurul obiect pe clasa (cls), și îl vom crea doar la prima
# apelare a lui __new__
# La orice alta apelare, vom returna obiectul deja existent

class SingletonPresedinteRomania:
    __instance = None
    def __new__(cls, *args, **kwargs):
         if cls.__instance is None:
            cls.__instance = object.__new__(cls)
         return cls.__instance

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'

P1 = SingletonPresedinteRomania()
P2 = SingletonPresedinteRomania()
P3 = SingletonPresedinteRomania()
P1.say_hello()
print(P2.say_hello())

print(P1)
print(P2)
print(P3)
print(f'ID(P1) = {id(P1)}')
print(f'ID(P2) = {id(P2)}')
print(P1 == P2 == P3)

# 2.Factory Pattern
# Acest pattern ne permite sa creăm un obiect dintr-o clasa folosind o alta clasa (fabrica).
# Fabrica are posibilitatea de a crea obiecte din mai multe clase
# (de obicei aceste clase sunt siblings, adica mostenesc de la acelasi parinte).
#
# Vom implementa următoarele clase:
# English/French/Spanish Translator – clase care știu sa traduca cuvinte din română
# în limba specificata
# translations va fi un dicționar cu acele cuvinte, exemplu `{ “masina”: “car” }` –
# se poate hardcoda în clasa localize va fi o funcție care pentru un parametru de
# intrare, ne va da traducerealui în acea limba (exemplu `input(“masina”)` returneaza “car”)
#
# TranslatorFactory – clasa care are o singura metoda (preferabil statica sau de clasa)
# numita get_translator(language) – in functie de parametrul language, returnează
# un translator object.

class English_Translator:
    def __init__(self, languege):
        self.languege = "en"
        self.translations_en = {
        'masina' : 'car',
        'culoare' : 'color',
        'curs' : 'course'
        }

    def localize(self, word):
        if word in self.translations_en:
            print(f"In limba engleza {word} este : {self.translations_en[word]}")
        else:
           print(f"Traducerea lipseste din dictionar")


class French_Translator:
     def __init__(self, languege):
         self.languege = 'fr'
         self.translations_fr = {
             'masina' : 'voiture',
             'culoare': 'couleur',
             'curs' : 'cours'
         }

     def localize(self, word):
        if word in self.translations_fr:
            print(f"In limba franceza {word} este : {self.translations_fr[word]}")
        else:
            print(f"Traducerea lipseste din dictionar")

class Spanish_Translator:

    def __init__(self, languege):
        self.languege = 'sp'
        self.translations_sp = {
            'masina' : 'auto',
            'culoare' : 'color',
            'curs' : 'corso'
        }
    def localize(self, word):
        if word in self.translations_sp:
            print(f"In limba franceza {word} este : {self.translations_sp[word]}")
        else:
            print(f"Traducerea lipseste din dictionar")


class Translator_Factory:
    def get_translator(self, languege):
        if languege == 'en':
            return English_Translator('en')
        elif languege == 'fr':
            return French_Translator('fr')
        else:
            languege == 'sp'
            return Spanish_Translator('sp')

print('*' * 50)
factory = Translator_Factory()


english_trans = factory.get_translator('en')
french_trans = factory.get_translator('fr')
spanish_trans = factory.get_translator('sp')

english_trans.localize('masina')
french_trans.localize('culoare')
spanish_trans.localize('curs')

print('*'* 50)
