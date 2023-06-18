# 3.Generators
#
# Implementați un generator pentru loteria 6/49 și noroc:
# Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv
# Ultima apelare va da un singur număr de “noroc” format din 7 cifre

import random
def generator_loterie():
    no_1 = random.randint(1, 49)
    yield no_1
    while True:
        no_2 = random.randint(1, 49)
        if no_2 != no_1:
            break
    yield no_2
    while True:
        no_3 = random.randint(1, 49)
        if no_3 != no_2 and no_3 != no_1:
            break
    yield no_3
    while True:
        no_4 = random.randint(1, 49)
        if no_4 != no_3 and no_4 != no_2 and no_4 != no_1:
            break
    yield no_4
    while True:
        no_5 = random.randint(1, 49)
        if no_5 != no_4 and no_5 != no_3 and no_5 != no_2 and no_5 != no_1:
            break
    yield no_5
    while True:
        no_6 = random.randint(1, 49)
        if no_6 != no_5 and no_6 != no_4 and no_6 != no_3 and no_6 != no_2 and no_6 != no_1:
            break
    yield no_6
    no_noroc = ""
    for i in range(7):
        x = str(random.randint(0, 9))
        no_noroc = no_noroc + x
        i=+1
    yield no_noroc


gen_loto = generator_loterie()

print(f'Primul numar castigator: {next(gen_loto)}')
print(f'Al 2-lea numar castigator: {next(gen_loto)}')
print(f'Al 3-lea numar castigator: {next(gen_loto)}')
print(f'Al 4-lea numar castigator: {next(gen_loto)}')
print(f'Al 5-lea numar castigator: {next(gen_loto)}')
print(f'Al 6-lea numar castigator: {next(gen_loto)}')
print(f'Numarul noroc este: {next(gen_loto)}')

print('*' * 50)

#EXEMPLUL DE EXPERIMENTAT
import random
def generator_loterie():
    nr_generate = []
    for i in range(6):
        print(i)
        numar = random.randint(1, 49)
        print(numar)
        while numar in nr_generate:
            print(nr_generate)
            numar = random.randint(1, 49)
            print(numar)
        nr_generate.append(numar)
        print(nr_generate)
        yield numar
        print(numar)

for numar in generator_loterie():
    print(numar)

# EXEMPLUL DE AVANSATI
def loto_gen():
    my_list = random.sample(range(1,50),6)
    for nr in my_list:
        yield nr
    yield random.randint(1_000_000, 9_999_999)

for nr in loto_gen():
    print(nr)

print('*'* 50)
#4.Context Managers
# Se da un fisier text hello.txt, care contine un text scurt. Deschideți fișierul și citiți conținutul, folosind urmatoarele 2 metode:
# try - finally
# Fișierul se deschide înainte de try, folosind functia open
# În interiorul try citim conținutul folosind functia read
# În finally se închide fișierul
# with (context manager)
# Se va observa ca pentru with nu mai este nevoie sa inchidem noi manual fișierul, pentru ca context managerul face asta pentru noi.

file = open('FILES/Hello.txt')
try:
    lines = file.read()
    print(lines)
finally:
    file.close()
print('*' * 50)

with open('FILES/Hello.txt') as my_file:
    #for lines in my_file:
        #print((f'{lines}'))
    print(f'{my_file.read()}')
#print(f'{my_file.read()}')

print('*' * 50)

# 5.Decorators
# Implementați următorii decoratori:
# timeit – decorator care măsoară timpul de execuție al unei funcții
# logger – decorator care printeaza argumentele de intrare, și rezultatul
# unei funcții

import time

def timeit(funct):
    def wrapper(*args, **kwargs):
        before = time.time()
        print(before)
        result = funct(*args, **kwargs)
        after = time.time()
        print(after)
        #timefunct = int(after - before)
        print("Timpul de executie al functiei", time.time() - before , "secunde" )
        return result

    return wrapper

@timeit
def function(name, age):
    time.sleep(1)
    print(f"My name is {name} and I am {age} ani")
function('Florian', 51)


def logger(funct):
    def wrapper(*args, **kwargs):
        result = funct(*args, **kwargs)
        print("argumente/parametrii numiti: ", args)
        print("argumente/parametrii numiti: ", kwargs)
        print("result: ", result)
        return result

    return wrapper
@logger
def suma(*args, **kwargs):
    pass

@logger
def suma1(a, b, c=5):
     x = a + b + c
     return x


suma(3, 4, c='mere')
suma1(3,4)

# 6.Decorators extra
# Implementați o clasă User, cu următoarele cerințe:
# – constructorul va primi nume, email, parola, și data nasterii
# – o metoda login, care va primi email și parola ca parametrii; dacă
# acestea sunt corecte, userul va fi marcat ca logat
# – o metoda get_info, care va returna toate informațiile despre user
# DOAR DACĂ acesta este logat, folosind un decorator `@require_login`
# – o metoda logout, fara params, care delogheaza userul.

class User:
    user = 'False'
    def __init__(self, name, email, password, birthday):
        self.name = name
        self.email = email
        self.password = password
        self.birthday = birthday

    def login_user(self, email, password ):
        if email == self.email and password == self.password:
            print(f'{self.name} you are logged in .')
            User.user = 'True'
            return print(User.user)
        else:
            print(f'The email or password is wrong.Please try again')

    def logout(self):
        print(f'{self.name}, you have now logget out')


    def require_login(self):
        def wrapper(*arg, **kwargs):
            if User.user == 'True':
                result = self(*arg, **kwargs)
                return result
            else:
                print("Please login")
        return wrapper

    @require_login
    def info_user(self):
       print(f'Name : {self.name}')
       print(f'Birthday : {self.birthday}')
       print(f'Email: {self.email}')

user1 = User("Florian", "florian.gabor@yahoo.com", "Andrei", "04.04.1972")
user1.login_user("florian.gabor@yahoo.com", "Andrei")
#user1.login_user("gldjfdfjd", "fdgjf")
#user1.logout()
user1.info_user()
#print(User.user)
