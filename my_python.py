class Car:
    def __init__(self, vin, make, model, price, color='BLUE', state='NEW'):
        self.vin = vin  # vehicle identification number
        self.make = make
        self.model = model
        self.color = color
        self.state = state
        self.price = price
        self.is_available = True
        self.selling_price = 0

    def describe(self):
        print('=' * 20, f'{self.make} {self.model}', '=' * 20)
        print(f'Color: {self.color}')
        if self.is_available:
            print(f'Price:  {self.price}')
        else:
            print(f'Selling price: {self.selling_price}')

    def sell(self, discount=0):
        self.is_available = False
        self.selling_price = self.price * (100 - discount) // 100

car1 = Car(1, 'Renault', 'Duster', 5000)
car2 = Car(2, 'Renault', 'Spring', 4000, 'rosu')

car1.sell()
car1.describe()
print()
car2.sell(23)
car2.describe()
print()

#from ptn_s3w2 import Circle

radius = int(input("Raza cercului este = "))
length = int(input("Lungimea dreptunghiului este = "))
color = input("Culoarea este : ")

circle = Circle(radius, color)
diameter = circle.get_diameter()
print(f"Diametrul cercului este: {diameter}")
print(f"Culoarea cercului este: {circle.get_color()}")

