import math
import random
from ctypes import pythonapi
from random import randint

from babel.numbers import number_re
from docutils.nodes import header
from nose.pyversion import sort_list
'''
#MODULE2. Variables and interactive programs
#1
print("Hello, World!")
print("hello,duxin")
print("hello,杜鑫")
name=input("my name is:")
print(f"hello,{name}")
#2
rds=float(input("input radius:"))
area=math.pi*rds*rds
print(f"area={area:.2f}")
#3
length=float(input("input length:"))
width=float(input("input width:"))
perimeter=2*length+2*width
area=length*width
print(f"perimeter={perimeter:.2f}")
print(f"area={area:.2f}")
#4
num1=float(input("input num1:"))
num2=float(input("input num2:"))
num3=float(input("input num3:"))
sum=num1+num2+num3
product=num1*num2*num3
average=sum/3
print(f"sum={sum:.1f}, product={product:.1f}, average={average:.1f}")
#5
talents=float(input("input talent:"))
pounds=float(input("input pounds:"))
lots=float(input("input lots:"))
mass1=lots*13.3+pounds*32*13.3+talents*20*32*13.3
mass2=(mass1//1000)
mass3=(mass1%1000)
print(f"The weight in modern units:{mass2}kilograms and {mass3:2f} grams.")
#6
import random
num1=[random.randint(0,9),random.randint(0,9),random.randint(0,9)]
num2=[random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
print(num1)
print(num2)
num3=[random.randint(0,9),random.randint(0,9),random.randint(0,9)]
num4=[random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
print(num3)
print(num4)

#INCLASS EXERCISE
#2708-1
money=float(input("input money:"))
if money>=5:
  print("you can buy a latte")

#2708-2
age=int(input("age:"))
if 15<=age<18:
    weight=float(input("weight(kg):"))
elif (age>=18 or ( 15<=age<18 and weight>=55) ):
    print("medicine can be used ")
else:
    print("medicine can not be used ")


#2708-2
score=int(input("score:"))
if score>=90:
    print("your grade is A1")
elif score>=80:
    print("your grade is A2")
elif score>=70:
    print("your grade is B1")
elif score>=60:
    print("your grade is B2")
elif score>=50:
    print("your grade is C1")
elif score>=35:
    print("your grade is C2")
elif score<35:
    print("fail")

#2708-3
wheels = int(input("enter the number of wheels:"))
if wheels==2:
    baterry=input("is there baterry :y or n: ")
    if baterry =="y":
        print("ebike")
    elif baterry=="n" :
        print("bike")
elif wheels==3:
    print("tricycle")
elif wheels==4:
    print("car")
else:
    print("input wrong")

#2708-4
age=int(input("age:"))
if age>=65:
    print("you are retired ")
elif age>=18:
    print("you are working  ")
elif age>=7:
    print("you are studying ")
elif age>0:
    print("you are a child ")


#2908-example-1
sum = 0
counter = 1
while counter < 10:
    sum=sum+counter
    print(f"the counter is {counter},and sum of the the counter with is {sum}")
    counter=counter+1


#2908-example-2
i = 1
n=int(input("enter the number:"))
while i<=n:
    if i % 2 == 0:
        print(f" the even number {i}")
    else:
        print(f" {i} is the odd number ")
    i=i+1

#2908-excercise 1
import random
target_number = random.randint(1,9)
number=1
while True:
    user_number = int(input("enter a guessing number between 1 and 9:"))
    if user_number == target_number:
        print(("well tried"))
        break
    else:
        print(("try again"))
        number=number+1
print("tried",number,"times")

#2908-excercise 2
user_input=""
while user_input != "exit":
    user_input = input("type something (or type exit to quit):")
    print("you typed:" ,user_input)

#2908-excercise 2
import random
flipcoin = random.choice(["head","tail"])
while flipcoin != "head":
    print("flipped:",flipcoin)
    flipcoin = random.choice(["head","tail"])
    print("you flipped",flipcoin)
    

#MODULE3. Conditional structures (if)
#problem 1
length = float(input("enter the length of a zander(cm):"))
if length < 42 :
    print("release the fish back into the lake")
    print("the caught fish is shorter than the size limit:",str(42-length))
else:
    print("the caught fish is within the size limit",)

#problem 2
cabin_class = input("enter the cabin class:")
LUX = "upper-deck cabin with a balcony"
A= "above the car deck, equipped with a window"
B= "windowless cabin above the car deck"
C= "windowless cabin above the car deck"
if cabin_class == "LUX":
    print (LUX)
elif cabin_class == "A":
    print (A)
elif cabin_class == "B":
    print (B)
elif cabin_class == "C":
    print (C)

#problem 3
gender = str(input("the biological gender is :" ))
hemoglobin_value = int(input("enter hemoglobin value(g/l):"))
if gender == "female":
    if hemoglobin_value < 117:
        print("the hemoglobin value is low")
    elif 117 <= hemoglobin_value <= 155:
        print("the hemoglobin value is normal")
    elif hemoglobin_value > 155:
        print("the hemoglobin value is high")
elif gender == "male":
    if hemoglobin_value < 134:
        print("the hemoglobin value is low")
    elif 134 <= hemoglobin_value <= 167:
        print("the hemoglobin value is normal")
    elif hemoglobin_value >=167:
        print("the hemoglobin value is high")

#peoblem4
year = int(input("enter year:"))
if year % 100 !=0 and year % 4 == 0:
    print(f"year {year}  is a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print(f"year {year} is a leap year")
else:
    print(f"year {year} is not a leap year")
    

num= int(input("Enter the number: "))
for n in range(1,num+1):
    if n%2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

names = []
name = input('enter your name or quit by entrting "": ')
while name != '':
    names.append(name)
    name = input('enter your name or quit by entering "":' )
print(names)


#MODULE4. While loops (while)
#1
num1 = 1
while num1 < 1000:
    if num1 % 3 == 0:
        print(num1)
    num1 = num1 + 1
for num1 in range(1,1001):
    if num1 % 3 == 0:
        print(num1)

#2
length = float(input("enter the length (inch): "))
converted = float(length * 2.54)
while length >= 0:
    print(f"coverted into centimeters is,{converted}","centimeters")
    length = float(input("enter the length (inch): "))

#3
numbers = [ ]
number = input("enter a number: ")
while number != "":
    numbers.append(number)
    number= input("enter a number: ")
if numbers:
    smallest = min(numbers)
    largest = max(numbers)
    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")
else:
    print("No numbers were entered.")

#4
import random
right_number = random.randint(1,10)
guess = int(input("enter a guess number: "))
while guess != right_number:
    if guess > right_number:
        print("too high")
    elif guess < right_number:
        print("too low")
    guess= int(input("enter a guess number: "))
print("correct")

#5
correct_name = "python"
correct_password = "rules"
n = 0
while n < 5:
    username = input("enter your username:")
    password = input("enter your password:")
    if username == correct_name and password == correct_password:
        print("welcome!")
        break
    else:
        print("wrong username or password")
        n=n+1
if n==5:
    print("access denied")
    
#6
import random
def pi(num_points):
    points_in_A = 0
    for _ in range(num_points):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if x**2 + y**2 < 1:
            points_in_A += 1
    pi = 4 * points_in_A / num_points
    return pi
num_points = int(input("enter the number of random points to generate: "))
approximation_pi = pi(num_points)
print(f"approximation of pi: {approximation_pi}")

#MODULE5.List structures and iterative loops (for)
#1
dice = int(input("how many dice to roll: "))
total = 0
for _ in range(dice):
    total += random.randint(1,6)
print(f"the sum of the numbers: {total}")

#2
list = []
num = input('enter a number or quit by entering"": ')
while num !="":
    list.append(int(num))
    num = input('enter a number or quit by entering"": ')
if  list :
    sorted_list = sorted(list,reverse = True)
    top5 = sorted_list[:5]
    print(top5)
else:
    print("No numbers were entered.")

#3
number = int(input('enter a number: '))
if number > 1:
    for i in range(2,number-1):
        if number % i == 0:
            print(f"{number} is not a prime number")
            break
    else:
            print(f"{number} a prime number")
else:
    print("number should be greater than one")

#4
city_list = []
for i in range(5):
    city_name = input(f"enter your name {i + 1}: ")
    city_list.append(city_name)
for city in city_list:
    print(city)


#MODULE6.Functions

#1
def dice_roll():
    return random.randint(1,6)
def main():
    while True:
        dice_result = dice_roll()
        print(f"rolled:{dice_result}")
        if dice_result == 6:
            print("rolled a 6, stop!")
            break
main()

#2
side = int(input("how many sides do you want: "))
def dice_roll(side):
    return random.randint(1,side)
def main():
    while True:
        dice_result = dice_roll(side)
        print(f"rolled:{dice_result}")
        if dice_result == side:
            print("rolled a largest number, stop!")
            break
main()

#3
def convert(gallon):
    return  0.2642*gallon
def main():
    while True:
        gallon = int(input("how many gallons : "))
        if gallon < 0:
            break
        volume_in_liters=convert(gallon)
        print(f"volume in liters: {volume_in_liters}")
main()

#4
def calc_sum(list):
    return sum(list)
def main():
        list = [56,87,9,45,1]
        sum_in_list = calc_sum(list)
        print(f"the sum of the numbers: {sum_in_list}")
main()

#5
def remove_uneven(list):
    new_list = []
    for num in list:
        if num % 2 == 0:
            new_list.append(num)
    return new_list
def main():
    list = [12,13,14,15,16,17,18,19,20]
    new_list = remove_uneven(list)
    print(f"the original list: {list}")
    print(f"the new list: {new_list}")
main()

#6
def unit_price(diameter,price):
    area = 3.14*(diameter/2)**2
    result = (price*10000)/area
    return result
diameter1 = int(input("enter the diameter of the first pizza(cm): "))
diameter2 = int(input("enter the diameter of the second pizza(cm): "))
price1 = float(input("enter the price of the first pizza(euros): "))
price2 = float(input("enter the price of the second pizza(euros): "))
unit_price1 = unit_price(diameter1,price1)
unit_price2 = unit_price(diameter2,price2)
if unit_price1 > unit_price2:
    print(f"the second pizza has better value")
else:
    print(f"the first pizza has better value")

#MODULE7.Tuple, set, and dictionary
#1
seasons = ("winter","spring", "summer", "fall")
def  find_season(month):
    if month in [12,1,2]:
        return seasons[0]
    elif month in [3,4,5]:
        return seasons[1]
    elif month in [6,7,8]:
        return seasons[2]
    elif month in [9,10,11]:
        return seasons[3]
    else:
        print("input a valid month")
try:
    month = int(input("enter the month: "))
    season = find_season(month)
    print(f"the season is:{season}")
except ValueError:
    print("input a valid month")

#2
names_set = set()
while True:
    name = input("Enter a name (or press Enter to stop): ")
    if name == "":
        break
    if name in names_set:
        print("Existing name")
    else:
        print("New name")
        names_set.add(name)
print("The entered names are:")
for name in names_set:
    print(name)

#3
airport_data = {}
while True:
    print("\nWhat would you like to do?")
    print("1. Enter a new airport")
    print("2. Fetch an existing airport's information")
    print("3. Quit")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == '1':
        icao_code = input("Enter the ICAO code of the airport: ").upper()
        airport_name = input("Enter the name of the airport: ")
        airport_data[icao_code] = airport_name
        print(f"Airport {airport_name} with ICAO code {icao_code} added.")
    elif choice == "2":
        icao_code = input("Enter the ICAO code of the airport to fetch: ").upper()
        if icao_code in airport_data:
            print(f"The name of the airport with ICAO code {icao_code} is {airport_data[icao_code]}.")
        else:
            print(f"No airport found with ICAO code {icao_code}.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1, 2, or 3.")


#MODULE8.Using relational databases
#1
import mysql.connector

def get_info_by_icao(ident):
    sql = f"SELECT ident, name, iso_country FROM airport WHERE ident='{ident}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:
            print(f"The name of {row[0]} is {row[1]} located at {row[2]}.")
    return

# Main program
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    password="123456",
    user="root",
    autocommit=True,
    charset='utf8mb4',
    collation='utf8mb4_general_ci'
    )

ident = input("Enter ident: ")
get_info_by_icao(ident)


#2

def get_type_by_areacode(iso_country):
    sql = (f"SELECT type,count(*) as count FROM airport WHERE iso_country='{iso_country}' group by type order by type")
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        print(f"Airports in {iso_country}:")
        for row in result:
            print(f"{row[0]}: {row[1]}")
    else:
        print(f"No airports found for the area code: {iso_country}")
    return
# Main program
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    password="123456",
    user="root",
    autocommit=True,
    charset='utf8mb4',
    collation='utf8mb4_general_ci'
    )
iso_country = input("Enter the area code: ")
get_type_by_areacode(iso_country)


#3
import mysql.connector
from geopy.distance import geodesic

def coordinates(cursor, ident):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{ident}'"
    cursor.execute(sql)
    return cursor.fetchall()

def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

def main():
    airport1_icao = input("Enter the ICAO code of the first airport: ").upper()
    airport2_icao = input("Enter the ICAO code of the second airport: ").upper()

    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        database="flight_game",
        password="123456",
        user="root",
        autocommit=True,
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )

    cursor = connection.cursor()
    airport1_coords = coordinates(cursor, airport1_icao)
    airport2_coords = coordinates(cursor, airport2_icao)

    if airport1_coords is None or airport2_coords is None:
        print("One or both airports not found in the database.")
    else:
        distance = calculate_distance(airport1_coords, airport2_coords)
        print(f"The distance between {airport1_icao} and {airport2_icao} is {distance:.3f} kilometers.")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
'''
#MODULE9.Fundamentals of object-oriented programming

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def __str__(self):
        return (f"Registration Number: {self.registration_number}\n"
                f"Maximum Speed: {self.max_speed} km/h\n"
                f"Current Speed: {self.current_speed} km/h\n"
                f"Traveled Distance: {self.travelled_distance} km")

    def drive(self, time):
        self.travelled_distance += self.current_speed * time


car1 = Car("ABC-123", 142)
print(car1)

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print(f"after acceleration, current_speed: {car1.current_speed} km/h")
car1.accelerate(-200)
print(f"after emergency brake, current_speed: {car1.current_speed} km/h")

car2 = Car("ABC-123", 142)
car2.current_speed = 60
car2.travelled_distance = 2000
car2.drive(1.5)
print("\nAfter driving for 1.5 hours:")
print(f"the car has travelled: {car2.travelled_distance} km")

def main():
    cars = []
    for i in range(1, 11):
        registration_number = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        car = Car(registration_number, max_speed)
        cars.append(car)

    race_ongoing = True
    while race_ongoing:
        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

            if car.travelled_distance >= 10000:
                race_ongoing = False
                break

    print("\nFinal results of the car race:")
    print(f"{'Registration number':10} | {'Max Speed':12} | {'Current Speed':12} | {'Travelled Distance':15}")
    print("-" * 60)

    for car in cars:
        print(
            f"{car.registration_number:<15} | {car.max_speed:<15} | {car.current_speed:<20} | {car.travelled_distance:<20.2f}")
if __name__ == "__main__":
    main()

#10-4
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"{'Registration number':<15} | {'Max Speed':<12} | {'Current Speed':<12} | {'Travelled Distance':<15}")
        print("-" * 60)
        for car in self.cars:
            print(f"{car.registration_number:<15} | {car.max_speed:<15} | {car.current_speed:<20} | {car.travelled_distance:<20.2f}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)

def main():
    cars = []
    for i in range(1, 11):
        registration_number = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        car = Car(registration_number, max_speed)
        cars.append(car)

    race = Race("Grand Demolition Derby", 8000, cars)
    hours_passed = 0
    while not race.race_finished():
        race.hour_passes()
        hours_passed += 1
        if hours_passed % 10 == 0:
            print(f"\n The new race has passed:{hours_passed} hours")
            race.print_status()
    print(f"\nThe new race is over and the total time is {hours_passed} hours.")
    race.print_status()

if __name__ == "__main__":
    main()

#11-2
class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, volum_of_tank):
        super().__init__(registration_number, max_speed)
        self.volum_of_tank = volum_of_tank

electric_car1 = ElectricCar("ABC-15", 180, 52.5)
gasoline_car1 = GasolineCar("ACD-123",165, 32.3)

electric_car1.current_speed = 120
electric_car1.drive(3)
print("After driving for 3 hours:")
print(f"Electric car has travelled: {electric_car1.travelled_distance} km")

gasoline_car1.current_speed = 129
gasoline_car1.drive(3)
print("After driving for 3 hours:")
print(f"Gasoline car has travelled : {gasoline_car1.travelled_distance} km")


#MODULE10.Association
class Elevator:
    def __init__(self,bottom_floor,top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor = self.current_floor + 1
            print(f"The elevator moved up to {self.current_floor}")
    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor = self.current_floor - 1
            print(f"The elevator moved down to {self.current_floor}")
    def go_to_floor(self,destination_floor):
        if destination_floor < self.bottom_floor or destination_floor > self.top_floor:
            print(f"Invalid floor number")
        while self.current_floor < destination_floor:
            self.floor_up()
        while self.current_floor > destination_floor:
            self.floor_down()
        print(f"The elevator gets floor{self.current_floor}")

h = Elevator(1,20)
h.go_to_floor(5)
h.go_to_floor(1)

class Building:
    def __init__(self,bottom_floor,top_floor,number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(number_of_elevators)]

    def run_elevator(self,elevator_number,destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            elevator = self.elevators[elevator_number]
            elevator.go_to_floor(destination_floor)
        else:
            print("Invalid elevator number")

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)

building1 = Building(1,20,5)
building1.run_elevator(2,12)
building1.fire_alarm()

#MODULE 11:
class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        Publication.__init__(self, name)
        self.author = author
        self.page_count = page_count

    def print_info(self):
        return f"the author of the book {self.name} is {self.author} and the book has {self.page_count} pages."


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        Publication.__init__(self, name)
        self.chief_editor = chief_editor

    def print_info(self):
        return f"the chief editor of the magazine {self.name} is {self.chief_editor}"


book1 = Book("Compartment No.6", "Rosa Liksom", 192)
print(book1.print_info())
magazine1 = Magazine("Donald Duck", "Aki Hyyppä.")
print(magazine1.print_info())


