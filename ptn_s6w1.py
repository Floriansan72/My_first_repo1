# 1.Create a text file called “hello.txt” and add the following text inside of it:
# Python
# Java
# Javascript
# C/C++/C#
# PHP
# Node.js
# Write a short program to read and display the text file

with open('FILES/Hello1.txt') as my_file:
    for line in my_file:
        print(line)


with open('FILES/Hello.txt') as my_file:
    my_line = my_file.readlines()
    for line in my_line:
        print(line)

# 2.Write a short program to append the following lines to “hello.txt” (you will
# use a list of strings and a for-loop):
# Go
# Kotlin
# Swift
# Display the new contents of the file.

my_list = ['Go\n', 'Kotlin\n', 'Swift\n']
with open('FILES/Hello1.txt', 'a') as my_file:
    for line in my_list:
        with open('FILES/Hello1.txt') as my_file1:
            if line in my_file1:
                break
            else:
                my_file.write(line)

with open('FILES/Hello1.txt') as my_file:
    for line in my_file:
        print(line)

# 3.Write a short program that reads the “hello.txt” file and displays
# every other line (only odd lines).

with open('FILES/Hello1.txt') as my_file:
    for line in my_file:
        if line in my_list:
            print(line)

# 4.Write a program that generates 26 text files, called `A.txt`, `B.txt`, … `Z.txt`.
# Each file will contain the sentences below:
# My name is letter X.
# I am the 24th letter of the alphabet.
# Make sure you use the correct ending for the letter’s number (e.g. 1st, 2nd, 3rd, etc.)

alphabet = []
start = ord('A')
#print(start)
for i in range(26):
    alphabet.append(chr(start + i))
print(alphabet)
for letter in alphabet:
    with open(f'FILES/{letter}.txt', 'w') as new_file:
        new_file.writelines(f'My name is letter {letter}. \n')
        if letter == 'A':
            new_file.writelines('I am the 1st letter of the alphabet. \n')
        elif letter == 'B':
            new_file.writelines('I am the 2nd letter of the alphabet. \n')
        elif letter == 'C':
            new_file.writelines('I am the 3rd letter of the alphabet. \n')
        else:
            new_file.writelines(f'I am the {ord(letter)-ord("A")+1}th letter of the alphabet. \n')


for letter in alphabet:
    with open(f'FILES/{letter}.txt') as my_file:
        for line in my_file:
            print(line)




# 5.Create a csv file called “students.csv” and add the following text inside of it:
# id,fname,lname,age,grade
# 1,Maria,Popescu,31,7.5
# 2,Andrei,Ionescu,26,8.0
# 3,Adriana,Marinescu,21,7.5
# 4,Matei,Gheorghescu,42,8.5
# 5,Eusebiu,Pop,33,9.5
# 6,Ioana,Popa,29,9.0
# Read the file using Python’s `csv` standard library, and display it in the terminal as a table,
# using the options for string formatting from Python:

import csv
with open('FILES/Students.csv', "r") as read_csv:
    my_file = csv.reader(read_csv)
    print('_' * 50)
    for line in my_file:
        print(f"{line[0]:^5}| {line[1]:<10}| {line[2]:<15}|{line[3]:^8}|{line[4]:^8}")
        print('.' * 50)

6.#Read again the information from the csv file above, store it all in a list of data,
# and then write a new file, called “students.json”, which will contain a valid JSON object.
# Use the following format for each student (and use Python’s standard JSON module):

import json

with open('FILES/Students.csv', "r") as read_csv:
    my_file = csv.reader(read_csv)
    my_file_Json = list(my_file)
    for i in range(1, len(my_file_Json)):
        dict = {
            "id" : my_file_Json[i][0],
            "fname" : my_file_Json[i][1],
            "lname" : my_file_Json[i][2],
            "age" : my_file_Json[i][3],
            "grade" : my_file_Json[i][4]
        }
        with open('FILES/Student.json', "a") as new_json:
            json.dump(dict, new_json, indent=7)

# 7.Create a new PyCharm project. Make sure it has a virtualenv. Install all the following
# packages from PYPI:
# behave
# behave-html-formatter
# requests
# selenium
# webdriver-manager
# Use pip to create a `requirements.txt` file. Send your project to a colleague and ask
# them to install all dependencies using pip.

