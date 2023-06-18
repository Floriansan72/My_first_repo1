# OOP - advance
#
# Exerciții - studiu în workshopul de weekend
#
# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’

from abc import ABC, abstractmethod
class  Geometric_Form(ABC):
    PI = 3.14
    @abstractmethod
    def area(self):
        raise NotImplementedError

    def description(self):
        return print("Cel mai probabil am colturi")

# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură

class  Square(Geometric_Form):
    def __init__ (self, side ):
        self.side = side

    def area(self):
        return self.side ** 2

p1 = Square(5)
p1.description()
p1.area()
print(p1.side)
print(f"Square area = {p1.area()}")

# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional,
# doar dacă ai ales să implementezi metoda abstractă aria)

class  SquareP(Geometric_Form):
    def __init__ (self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    @property
    def side(self):
        print("Acesta este un getter")
        return self.__side
    @side.getter
    def side(self):
        print(f"Acesta este un getter: Side = {self.__side}")
        return self.__side

    @side.setter
    def side(self, new_side):
        self.__side = new_side
        print(f"Acesta este un setter: side = {self.__side}")

    @side.deleter
    def side(self):
        print("Not possible delete side")



p2 = SquareP(6)
p2.side
p2.area()
print(f"Square area = {p2.area()}")
p2.side = 7
p2.side
print(f"Square area = {p2.area()}")
del p2.side


# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul
# folosește field PI mostenit din clasa părinte
# (opțional, doar dacă ai ales să implementezi
# metoda abstractă aria)

class Circle(Geometric_Form):
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.getter
    def radius(self):
        print(f"Acesta este un getter: radius = {self.__radius}")
        return self.__radius
    @radius.setter
    def radius(self, new_radius):
        self.__radius = new_radius
        print(f"Acesta este un setter: new_radius = {self.__radius}")
        return self.__radius

    @radius.deleter
    def radius(self):
        self.__radius = None
        print(f"Acesta este un deleter: radius = {self.__radius}:.()")

    def area(self):
        circle_area = Geometric_Form.PI * self.__radius **2
        print(f"Circle area este: {circle_area}")

    def description(self):
        print("Eu nu am colturi")

c1 = Circle(5)
c1.radius
c1.area()
c1.radius = 7
c1.radius
c1.area()
del c1.radius
c1.description()