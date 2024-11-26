import random
from functools import total_ordering
from pyexpat.errors import messages

from docutils.nodes import table

from project_flight_game import current_airport

'''
first=float(input("first: "))
second=float(input("second: "))
sum=first+second
print("sum: ", sum )

#
weight = float(input("weight: "))
unit = input("kg or lbs: ")
if unit == "kg":
    converted = weight / 0.45
    print("weight in lbs: ",converted)
elif unit == "lbs":
    converted = weight * 0.45
    print("weight in kg: ", converted)


name = input("what is your name? ")
color = input("what is your favorite color? ")
print(name,"likes", color)

#remember the variables can not be separate words, they must be connected by a line
name = input("what is your name? ")
favourite_color = input("what is your favorite color? ")
print(name + " likes " + favourite_color)
# use + to concatenate or combine two strings.
# a space after question mark
# spaces before likes and after likes


weight_lbs = float(input("what is your weight (in pounds): "))
converted = weight_lbs * 0.45
print("weight_kg ", converted)

house_price = 1000000
good_credit = True
if good_credit:
    payment1 = 0.1 * house_price
else:
    payment2 = 0.2 * house_price
print(f"down payment: ${payment1}")

#Let's write a program that asks the user how many times to greet. After that the program will print out the greetings:
greet = int(input("how many times to greet: "))
greet_times = 0
while greet_times < greet:
    print("good morning")
    greet_times += 1

from nose.twistedtools import stop_reactor

#The program asks the user to give text commands until the user enters a stop command:
command = input("enter command: ")
while command != "stop":
    print("execution command: ",command)
    command=input("enter command: ")
print("execution stopped")

#Next, we will look at a simulation example where the amount of repetitions is based on a random number generator.
#The program rolls two dice until they result to a pair of sixes.
#the number of required rolls varies between runs:
num1 = num2 = n = 0
while num1 !=6 or num2 !=6:
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    n = n+1
print("rolled: ",n,"times")

#Let's print out the multiplication table from one to five. The table includes all twenty-five possible multiplications with numbers 1, 2, 3, 4 and 5:
num1 = 1
while num1 <= 5:
    num2 = 1
    while num2 <= 5:
        print(f"{num1} times {num2} is {num1*num2}")
        num2 = num2 + 1
    num1 = num1 + 1

#Let's extend the dice rolling example so that the program prints out how many rounds on average is needed before getting a pair of sixes.
#To calculate the average, let's set the number of simulated rounds to a very large number, a hundred thousand:
rounds = 0
total_rolls = 0
while rounds < 100000:
    dice1 = dice2 = rolls = 0
    while dice1 != 6 or dice2 != 6:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        rolls += 1
    rounds += 1
    total_rolls = total_rolls + rolls
average_rolls= total_rolls / rounds
print(f"the average rounds is required: {average_rolls:6.2f}")


#In the next program the number of repetitions is not known when entering the loop structure.
# The program asks the user to give text commands until the user enters a stop command:
command = input("enter command: ")
while command != "stop":
    print("execution command: ",command)
    command = input("enter command : ")
print("execution stopped")

#Next, we will look at a simulation example where the amount of repetitions is based on a random number generator.
# The program rolls two dice until they result to a pair of sixes.
dice1 = dice2 = rolls = 0
while dice1 != 6 or dice2 != 6:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    rolls += 1
print("rolled: ",rolls,"times")


#
round = 0
total_rolls = 0
while round < 100000:
    dice1 = dice2 = rolls = 0
    while dice1 != 6 or dice2 != 6:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        rolls += 1
    round += 1
    total_rolls = total_rolls + rolls
print(f"the average rounds is required: {total_rolls/round:6.2f}")


# Example: Nested loop to print each element of a 2D matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # Newline after each row

# Example: Finding prime numbers in a range
start = 10
end = 30

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):  # Iterate over the range
    if num > 1:  # Prime numbers are greater than 1
        for i in range(2, num):  # Check for factors
            if (num % i) == 0:  # Not a prime number if divisible by any number other than 1 and itself
                break
        else:
            print(num)  # Prime number

weight = int(input("weight: "))
unit = input("lbs or kg: ")
if unit == "kg":
    converted = weight / 0.45
    print(f"The weight is {converted:.2f} lbs")
elif unit == "lbs":
    converted = weight * 0.45
    print(f"The weight is {converted:.2f} kg")

right = 9
guess_counter = 0
guess_limit = 3
while guess_counter < guess_limit:
    guess = int(input("guess: "))
    guess_counter +=1
    if guess == right:
        print("you won!")
        break
else:
    print("you failed")

command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("car started.ready to go!")
    elif command == "stop":
        print("car stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit        
        """)
    elif command == "quit":
        break
    else:
        print("sorry,i don't understand that")

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit        
        """)
    elif command == "quit":
        break
    else:
        print("sorry,i don't understand that")

price = [10,23,44,15]
total = 0
for price in price:
    total += price
print(f"total price is {total}")

for x in range(1,3):
    for y in range(1,3):
        print(f"({x},{y})")

numbers = [5,2,5,2,2]
for x_count in numbers:
    print("x" * x_count)


#if not use the number times a string(this is a feature just for python),we can use nested loop:
numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)

list = [9,4,5,7,12,4,5]
maximun = list[0]
for number in list:
    if number > maximun:
        maximun = number
print(f"the maximun number is {maximun}")

#dictionary
customers = {
    "name" : "duxin",
    "age" : 30,
    "phone number" : 23889
}
print(customers["phone number"])
print(customers["age"])
print(customers.get("gender"))#use get method,the program will not yell at us
#note that get method with parenthesis
print(customers.get("name"))
print(customers.get("gender", "female"))#we can supply the default value to dictionary
customers["gender"] = "male"#we can supply the default value to dictionary
print(customers["gender"])

phone = input("enter your phone number: ")
digit_mapping = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four"
}
output = ""
for num in phone:
    output += digit_mapping.get(num,"!") +" "
print(output)


message = input("> ")
words = message.split(" ")
emojis = {
    ":)" : "😁",
    ":(" : "🥹"
}
output = ""
for word in words:
    output += emojis.get(word,word) + " "
print(output)


def greet_user():      #define a function
    print("hello")     #those two intended lines are belonged to the function,when we call the function,those lines will be executed.
    print("welcome")


print("start")    #the first message in the terminal
greet_user()      #call the function, the lines inside the function will start
print("stop")

def greet_user(name):
    print(f"hello {name} !")
    print("welcome aboard!")

print("start")
greet_user("john")
greet_user("jane")
print("stop")


def emojis_converter():
    words = message.split(" ")
    emojis = {
        ":)": "😁",
        ":(": "🥹"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output
message = input("> ")
result = emojis_converter()
print(result)


#exception. when you type something is not numerical ,then the programming will not crash, instead of that,program will return that: invalid input
try:
    age = int(input("age: "))
    print(f"your age is {age}")
except ValueError:
    print("invalid input")

#class and constructor
class Person:                          #define a new type
    def __init__(self, name):          #constructor
        self.name = name
    def talk(self):                    #method
        print(f"hi,i am {self.name}")
john = Person("john smith")
bob = Person("bob smith")
john.talk()
bob.talk()


class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    pass                      #pass doesnt have any meaning ,just because python doesnt like empty class
class Cat(Mammal):
    pass
dog1 = Dog()        #creat an object of Dog class
dog1.walk()
cat1 = Cat()
cat1.walk()

class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    def bark(self):        #dog will have two methods. one is inherited from mammal, one is defined in this line.
        print("bark")
class Cat(Mammal):
    def be_annoying(self):
        print("annoying")
dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 = Cat()
cat1.walk()
cat1.be_annoying()

cities = []
for i in range(5):
    city = input(f"enter a city name {i + 1}: ")
    cities += [city]
print("the names of the cities are:")
for city in cities:
    print(city)
    
students_score = {}
total_score = 0
number = int(input("how many students in your class: "))
for i in range(number):
    name = input("Enter student'name: ")
    score = int(input("Enter score: "))
    students_score[name] = int(score)
    total_score += score
print(students_score)
print(f"the total score is:{total_score}")


import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="duckburg",
    password="123456",
    user="root",
    autocommit=True,
    charset='utf8mb4',
    collation='utf8mb4_general_ci'
    )
########################################################mooc
# Given number
number =float(input("enter a number: "))
# Integer part
integer_part = int(number)
# Decimal part
decimal_part = number - integer_part
# Output the results
print(f"Integer part: {integer_part}")
print(f"Decimal part: {decimal_part:.2f}")  # Format to 2 decimal places
#It first extracts the integer part using int(), and then calculates the decimal part by
# subtracting the integer part from the original number.
# The :.2f ensures the decimal part is formatted to two decimal places.


age = int(input("how old are you? : "))
if age <= 18:
    print("You are not of legal age!")
else:
    print("You are of legal age!")


# Function to compare ages and print the older person's name
def find_older_person():
    # Get the name and age of the first person
    name1 = input("Enter the name of the first person: ")
    age1 = int(input("Enter the age of the first person: "))

    # Get the name and age of the second person
    name2 = input("Enter the name of the second person: ")
    age2 = int(input("Enter the age of the second person: "))

    # Compare ages and determine who is older
    if age1 > age2:
        print(f"The older person is {name1}.")
    elif age2 > age1:
        print(f"The older person is {name2}.")
    else:
        print("Both are of the same age.")
# Call the function to execute the program
find_older_person()


# Function to compare two words and determine which comes later alphabetically
def compare_words():
    # Get two words from the user
    word1 = input("Give word 1: ").lower()
    word2 = input("Give word 2: ").lower()

    # Compare the words alphabetically
    if word1 < word2:
        print(f"{word2} comes later in the alphabet")
    elif word1 > word2:
        print(f"{word1} comes later in the alphabet")
    else:
        print("Both words are the same.")
# Call the function to execute the program
compare_words()


age = int(input("enter age: "))
if age >= 5:
    print(f"Okay, so you are {age} years old")
elif age > 0:
    print("I don't think you can write...")
else:
    print("You must have written wrong.")


name = input("Enter your name: ")
if name in ["Knatte", "Fnatte", "Tjatte"]:
    print("You are probably Donald Duck's nephew.")
elif name in ["Teddi", "Freddi"]:
    print("You are probably Mickey Mouse's nephew.")
else:
    print("I don't know whose nephew you are.")

letter1 = input("Give letter 1: ").lower()
letter2 = input("Give letter 2: ").lower()
letter3 = input("Give letter 3: ").lower()

    # Store the letters in a list and sort them alphabetically
letters = [letter1, letter2, letter3]
letters.sort()

    # Print the middle letter (the second in the sorted list)
print(f"The middle letter is {letters[1]}")

while True:
    tal = int(input("Give a number, -1 ends the program: "))
    if tal == -1:
        break
    print(tal**2)
print("thank you and hello!")

while True:
    # Get a number from the user
    number = int(input("Give a number, -1 ends the program: "))
    # Check if the number is -1 to end the program
    if number == -1:
        print("Thank you and hello!")
        break
    # Otherwise, square the number and print the result
    print(number ** 2)

while True:
    code = input("enter your code: ")
    if code == "1234":
        break
    print("error! try again enter pin again")
print("correct pin code")


while True:
    asking = input("hi,shall we continue? ")
    if asking.lower() ==  "no":
        print("not then")
        break

from math import sqrt
while True:
    number = int(input("Enter a number: "))
    if number > 0:
        print(sqrt(number))
    elif number < 0:
        print("invalid number")
    else:
        print("exiting!")
        break

number = 5
print("countdown to start!")
while True:
    print(number)
    number = number - 1
    if number <= 0:
        break
print("go!")

password = input("Password: ")
while True:
    repeat_password = input("Repeat password: ")
    if password == repeat_password:
        break
    print("Incorrect! Repeat password:")
print("account created!")

password = input("Password: ")
while True:
    repeat_password = input("Repeat password: ")
    if password == repeat_password:
        print("account created!")
        break
    print("Incorrect! Repeat password:")

times = 0
while True:
    password = input("Password: ")
    times += 1
    if password == "123":
        print("correct password!")
        break
    if times ==3:
        print("too many times!")
        break
    print("incorrect password and try again!")

tries = 0
while True:
    password = input("Pin code: ")
    tries += 1
    if password == "000":
        if tries == 1:
            print("Correct, you only needed one try!")
            break
        print(f"correct! you made {tries} attempts")
        break
    else:
        print("incorrect pin code and try again: ")


year = int(input("Year: "))
next_year = year + 1
while not ((next_year % 4 == 0 and next_year % 100 != 0) or (next_year % 400 == 0)):
    next_year += 1
print(f"The next leap year after {year} is {next_year}")



for a in range(2,31,2):
    print( a)

number = int(input("Clear? Give a number: "))
for i in range(number, 0, -1):
    print(i, end=" ")
print("Go!")

number = int(input("Give a number: "))
while number < 100 and number%5 != 0:
    print(number)
    number += 3

number = int(input("util the number: "))
for i in range(1, number):
    print(i,end="")

number = int(input("until the number: "))
i = 1
while i <= number:
    print(i,end="")
    i = i * 10

#Write a program that asks the user to enter names until he/she enters an empty string.
#After each name is read the program either prints out New name or Existing name depending on whether the name was entered for the first time.
#Finally, the program lists out the input names one by one, one below another in any order. Use the set data structure to store the names.
#Initialize an empty set to store names
names_set = set()
while True:
    name = input("Enter a name or press Enter to stop: ")
    if name == '':
        break
    if name not in names_set:
        print("New name")
        names_set.add(name)
    else:
        print("Name already in use")
print("The entered names are: ")
for name in names_set:
    print(name)

# Write a program for fetching and storing airport data.
# The program asks the user if they want to enter a new airport, fetch the information of an existing airport or quit.
# If the user chooses to enter a new airport, the program asks the user to enter the ICAO code and name of the airport.
# If the user chooses to fetch airport information instead, the program asks for the ICAO code of the airport and prints out the corresponding name.
# If the user chooses to quit, the program execution ends. The user can choose a new option as many times they want until they choose to quit.
# (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK.
# You can easily find the ICAO codes of different airports online.)
# Initialize an empty dictionary to store airport data

number = int(input("Please type in a number: "))



#Sample Exam Questions1:
#Define a class Car with attributes make, model, and year. Add a method display_info() that prints out the car’s details.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car make: {self.make}. Model: {self.model}, produced in:{self.year}")

car = Car("BMW","automatic",1980)
car.display_info()
#What is the role of the self keyword in a class?
#the role of the self keyword is the instance itself.

#Sample Exam Questions2:
#Explain the difference between aggregation and composition with examples.
#Write a class Library that contains a list of Book objects using aggregation.
#Sample Exam Questions3:
#	Explain inheritance and its benefits. Give an example.
#	Write a class Bird with a method fly(). Inherit Eagle from Bird and override the fly() method.
#Sample Exam Questions:4
#•	Write a Python program to fetch weather data from an API and display the temperature.
#•	What is the purpose of response.json() in the requests library?
#Sample Exam Questions5:
#•	Explain what Flask is and provide an example of a simple Flask route.
#•	Write a Flask route /api/greet that returns a JSON message "Hello, user!".

# Making a GET request with a query parameter
'''
