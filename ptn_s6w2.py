import sqlite3


conexiune = sqlite3.connect('geografie.db')     # stabilim o conexiune cu baza de date ca sa putem interactiona cu ea
cursor = conexiune.cursor()     # ne ajuta sa interactionam in  baza de data cand avem mai multe queries
# cursor.execute("""CREATE TABLE IF NOT EXISTS continents (
#                     continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     continent_name TEXT NOT NULL,
#                     continent_code CHAR(2) NOT NULL
#                     )""")

#conexiune.commit()
# res = cursor.execute(" SELECT name FROM sqlite_master")
# print(res.fetchall())

continente = [('Africa', 'AF'), ('North America', 'NA'), ('South America', 'SA'),
              ('Antarctica', 'AN'), ('Australia', 'OC'), ('Asia', 'AS'), ('Europe', 'EU')]
sql_query = 'INSERT INTO continents(continent_name, continent_code) VALUES(?,?)'
cursor.executemany(sql_query, continente)
#conexiune.commit()  # ca sa se salveze modificarile aduse la baza de date

# cursor.execute("""CREATE TABLE countries(
#                     country_code CHAR(2) NOT NULL,
#                     country_name TEXT NOT NULL,
#                     continent_id INTEGER FOREIGNKEY,
#                     population TEXT NOT NULL
#                     )""")

# cursor.execute("""INSERT INTO countries VALUES
#                     ('RO', 'Romania', 6, '19 mil'),
# 		            ('ES', 'Spain', 6, '46 mil'),
#                     ('MX', 'Mexico', 2, '128 mil'),
#                     ('HT', 'Haiti', 2, '11 mil'),
#                     ('BZ', 'Brazil', 7, '215 mil'),
#                     ('AR', 'Argentina', 7, '45 mil'),
#                     ('EG', 'Egypt', 1, '115 mil'),
#                     ('MA', 'Morocco', 1, '45 mil'),
#                     ('JP', 'Japan', 5, '123 mil'),
#                     ('TR', 'Turkey', 5, '73 mil'),
#                     ('AU', 'Australia', 3, '25 mil'),
#                     ('FJ', 'Fiji', 3, '1 mil')
#                     """)

#conexiune.commit()
res = cursor.execute("SELECT name FROM sqlite_master")
print(res.fetchmany())

# Write a SQL statement to select all countries, ordered by name. Write another statement
# to count them all.

# res = cursor.execute("DELETE FROM countries")
# print(res.fetchmany())

res = cursor.execute("SELECT * FROM countries ORDER BY(country_name)")
lista = res.fetchall()
for line in lista:
    print(line)

print('country_code ' + ' country_name ' + ' continent_id ' + ' population')
print('_' * 54)
for line in lista:
    print(f"{line[0]:^12} | {line[1]:^12} | {line[2]:^10} | {line[3]:>10}")
    print('.' * 54)

res = cursor.execute("SELECT COUNT(country_name) FROM countries")
print(f"Total country = {res.fetchone()[0]}")

# Write a SQL statement to select only countries with a population greater than 20 millions.

res= cursor.execute("SELECT * FROM countries WHERE populatiom > '20 mil'")
lista = res.fetchall()
for line in lista:
    print(line)

print('country_code ' + ' country_name ' + ' continent_id ' + ' population')
print('_' * 54)
for line in lista:
    print(f"{line[0]:^12} | {line[1]:^12} | {line[2]:^10} | {line[3]:>10}")
    print('.' * 54)

#Write a SQL statement to select only countries that start with a certain letter

res = cursor.execute("SELECT * FROM countries WHERE country_name LIKE 'A%'")
lista = res.fetchall()
for line in lista:
    print(line)

#Write a SQL statement that groups all countries by continents, and counts them.

res = cursor.execute("SELECT COUNT(country_name), continent_id FROM countries GROUP BY continent_id")
lista = res.fetchall()
for line in lista:
    print(line)

# Write a SQL statement that groups all countries by continent,
# and computes the total population per continent (SUM).
print('*' * 55)
res = cursor.execute("SELECT SUM(populatiom), continent_id FROM countries GROUP BY continent_id ")
lista = res.fetchmany(7)
for line in lista:
    print(line)

conexiune.close()