# TEMA PENTRU ACASA:
# - clase pentru urmatoarele: Circle (cerc), Rectangle (dreptunghi) si Triangle (triunghi)
# - fiecare clasa va avea pe langa atributele evidente (geometrice) si un atribut de culoare optional,
#   iar ca metode, se vor cele geometrice care au sens, plus o metoda de describe.
# - din fiecare clasa, va rog sa faceti 1-3 obiecte cu care sa va jucati

class Circle:
    make = "Compas"
    color = None
    def __init__(self, radius, color="Gray"):
        self.radius = radius
        self.color = color

    def description1(self):
        print(f"Cerc cu raza : {self.radius} . Culoarea {self.color}")

    def description2(self):
        print(f"{'=' * 20} Cerc {self.color} {'=' * 20}")
        print(f"Raza = {self.radius}")

    def get_area(self):
        PI = 3.14
        return PI * self.radius**2
    def get_color(self):
        return self.color

    def get_perimeter(self):
        return 2 * PI * self.radius

    def get_diameter(self):
        return 2 * self.radius

# M-am "jucat" putin cu crearea de obiecte

radius = int(input("Raza cercului este radius = "))
color = input("Tastati o culoare pentru cerc = ")

circle0 = Circle(radius, color)
circle0.description2()
print(circle0)

circle1 = Circle(5, "Red")
circle2 = Circle(2, "Blue")
circle3 = Circle(3, "Green")
circle4 = Circle(6, "Yellow")
circle5 = Circle(4, "Pink")
print(circle1.make)

list1 =[circle1.color, circle2.color, circle3.color, circle4.color, circle5.color]
print(f"Lista de culori pentru cercuri este: {list1}")
print(f'list1 = {list1}')
list1.sort()
print(f"list1 = {list1}")
list2 = [circle1.get_color(), circle2.get_color()]
print(f"list2 = {list2}")

circle1.description2()
circle2.description2()
circle3.description2()
circle4.description2()
circle5.description2()
print()

print('*' * 70)

print(f"Diametrul cercului3 este : {circle3.get_diameter()}")
print(f"Aria cercului2 este : {circle2.get_area()}")
print(f"Culoare cercului5 este {circle5.get_color()}")

# 2.Exercitiul_2
# 2. Clasa Dreptunghi
#      Atribute: lungime, lățime, culoare
#      Constructor pentru toate atributele
#      Metode:
# descrie()
# aria()
# perimetrul()
# schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().

class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    def description(self):
        print(f"{'<' * 20} Dreptunghi {self.color} {'>' * 20}" )
        print(f"Lungime latura = {self.length}")
        print(f"Latime latura = {self.width}")

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_color(self):
        return self.color

    def get_diagonal(self):
        return (self.length**2 + self.width**2)**0.5

    def get_change_color(self):
        self.color = "Violet"


rectangle1 = Rectangle(5, 4, "Red")
rectangle2 = Rectangle(3, 2, "Pink")
rectangle3 = Rectangle(1, 4, "Blue")
rectangle4 = Rectangle(4, 6, "Gray")

print(f"Aria pentru dreptinghi1 este: {rectangle1.get_area()}")
print(f"Perimetrul pentru dreptunghi2 este: {rectangle1.get_perimeter()}")
print(f"Culoare pentru dreptunghi3 este: {rectangle3.get_color()}")
print(f"Diagonala pentru dreptunghi4 este: {rectangle4.get_diagonal()}")
rectangle2.get_change_color()
print()
rectangle2.description()
print()


# 3. Clasa Angajat
#
#      Atribute: nume, prenume, salariu
#      Constructor pentru toate atributele
#      Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)

class Employee:
    def __init__(self, name, first_name, salary):
        self.name = name
        self.first_name = first_name
        self.salary = salary

    def description(self):
        print(f"{'*' * 20} Angajat al Firmei {'*'* 20}")

    def complet_name(self):
        complet_name = self.name + ' ' + self.first_name
        print(f"Employee Name : {complet_name}")
        return complet_name

    def monthy_salary(self):
        print(f"Monthy_salary : {self.salary} RON")

    def annual_salary(self):
        annual_salary = self.salary * 12
        print(f"Annual_salary : {annual_salary} RON")

    def salary_bonus(self, bonus):
        print(f"Marirea de salariu pentru {self.complet_name()} : {bonus}% ")

employee1 = Employee("Popescu", "Ion", 5000 )
employee1.description()
employee1.complet_name()
employee1.monthy_salary()
employee1.annual_salary()
print()

employee2 = Employee("Ionescu", "Maria", 6000)
employee2.description()
employee2.complet_name()
employee2.monthy_salary()
employee2.annual_salary()
print()

employee2.salary_bonus(10)
employee1.salary_bonus(12)
print()

# 4. Clasa Cont
#    Atribute: iban, titular_cont, sold
#    Constructor pentru toate atributele
#    Metode:
# afisare_sold() - Titularul x are în contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)

class Cont:
    #suma = 0
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei")

    def debitare_cont(self, suma):
        self.sold = self.sold - suma
        return self.sold

    def creditare_cont(self, suma):
        self.sold = self.sold + suma
        return self.sold

cont1 = Cont(1234 , "Popescu Vasile", 3000)
cont2 = Cont(5678, "Ionescu Maria" , 5000)

cont1.afisare_sold()
cont2.afisare_sold()
cont1.debitare_cont(500)
cont1.afisare_sold()



# 5. Clasa Factură
#      Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile
#      vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc
#      Constructor: toate atributele, fără serie
#      Metode:
# schimbă_cantitatea(cantitate)
# schimbă_prețul(pret)
# schimbă_nume_produs(nume)
# generează_factura() - va printa tabelar dacă reușiți
#
# Factura seria x număr y
# Data: generează automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon |      7       |       700       | 49000

from datetime import date
from tabulate import tabulate
class Invoice:
    def __init__(self, number, article, quantity, price_pcs):
        self.number = number
        self.article = article
        self.quantity = quantity
        self.price_pcs = price_pcs
        self.serial_no = 'ABC'


    def change_quantity(self, new_quantity):
        self.quantity = new_quantity
        return self.quantity

    def change_price(self, new_price):
        self.price_pcs = new_price
        return self.price_pcs

    def article(self, new_article):
        self.article = new_article
        return self.article

    def date_invoice(self):
        total = self.quantity * self.price_pcs
        self.data = [ self.article, self.quantity, self.price_pcs, total]
        return self.data

    def generate_invoice(self):
        print(f"FACTURA seria {self.serial_no} numar {self.number} ")
        today = date.today()
        print(f"Data: {today}")
        print(tabulate([self.data], headers=['ARTICOL', 'CANTITATE', 'PRET_BUC', 'TOTAL']))

item1 = Invoice(1234, "telefon", 3, 300)
item2 = Invoice(1234, "casti", 5, 100)
item3 = Invoice(1234, "husa", 10, 50)
item1.change_price(500)
item2.change_quantity(35)
item1.date_invoice()
item1.generate_invoice()
item2.date_invoice()
item2.generate_invoice()
item3.date_invoice()
