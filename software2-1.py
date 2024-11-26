'''
# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict) :
    # Calculate the average result for each contestant
    avg1 = (person1["result1"] + person1["result2"] + person1["result3"]) / 3
    avg2 = (person2["result1"] + person2["result2"] + person2["result3"]) / 3
    avg3 = (person3["result1"] + person3["result2"] + person3["result3"]) / 3
    
    # Find the contestant with the smallest average
    if avg1 < avg2 and avg1 < avg3:
        return person1
    elif avg2 < avg1 and avg2 < avg3:
        return person2
    else:
        return person3

# Example usage
person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

print(smallest_average(person1, person2, person3))
from datetime import date
def list_years(dates:list):
    years = []
    for item in dates:
        years.append(item.year)
    years.sort()
    return years

date1 = date(2019, 2, 3)
date2 = date(2006, 10, 10)
date3 = date(1993, 5, 9)
years = list_years([date1, date2, date3])
print(years)

# DO NOT CHANGE THE CODE OF THE CLASS
# ShoppingList. Write yous solution under it!
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]

# -------------------------
# Write your solution here:
# -------------------------
def total_units(my_list: ShoppingList):
    total = 0
    for i in range(1, my_list.number_of_items()+1):
        total += my_list.amount(i)
    return total

if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("pineapple", 1)

    print(total_units(my_list))
    print(my_list.products)

# Write your solution here:



class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        # 每次调用 tick 方法，秒数增加
        self.seconds += 1
        # 如果秒数达到60，则重置秒数并增加1分钟
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        # 如果分钟数达到60，则重置分钟数
        if self.minutes == 60:
            self.minutes = 0#(这步也可以省略)

    def __str__(self):
        # 返回格式化的分钟和秒数，确保两位数显示
        return f"{self.minutes:02}:{self.seconds:02}"


watch = Stopwatch()
for i in range(3600):
    print(watch)
    watch.tick()

class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def tick(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        if self.hour == 24:
            self.hour = 0

    def set(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.second = 0

    def __str__(self):
        # 返回格式化的hour,分钟和秒数，确保两位数显示
        return f"{self.hour}:{self.minute:02}:{self.second:02}"
clock = Clock(23, 59, 55)
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)

clock.set(12, 5)
print(clock)


class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.rates = []  # 初始化一个空列表来存储评分

    def rate(self, rating: int):
        # 将评分添加到 rates 列表中
        self.rates.append(rating)

    def __str__(self):
        genre_string = ", ".join(self.genres)
        # 如果有评分，计算平均分
        if len(self.rates) > 0:
            average_rating = sum(self.rates) / len(self.rates)
            rating_info = f"{len(self.rates)} ratings, average {average_rating:.1f} points"
        else:
            rating_info = "no ratings"

        return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\n{rating_info}"


# 示例使用
dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
dexter.rate(4)
dexter.rate(5)
dexter.rate(5)
dexter.rate(3)
dexter.rate(0)
print(dexter)

import random
import pandas as pd


class Person:
    def __init__(self, name: str, age: int,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        pass

class Student(Person):
    def __init__(self,name,age,gender,student_id):
        super().__init__(name,age,gender)
        self.student_id = student_id
    def introduce(self):
        return f"I am {self.name}, {self.age} years old. I am {self.gender}, and my id is {self.student_id}."

class Assistant(Student):
    def __init__(self,name,age,gender,student_id,salary):
        super().__init__(name,age,gender,student_id)
        self.salary = salary
    def introduce(self):
        return f"my name is {self.name}, my age is {self.age}. I am {self.gender}. my student_id is {self.student_id} and salary is {self.salary}."

class Teacher(Person):
    def __init__(self,name,age,gender,teacher_title):
        super().__init__(name,age,gender)
        self.teacher_title = teacher_title

    def introduce(self):
        return f"my name is {self.name}, I am {self.age} I am {self.gender}. I am {self.teacher_title}."

student1 = Student("Lucy",23,"female",12345)
print(student1.introduce())
assistant1 = Assistant("Lucy",23,"female",12345,2300)
print(assistant1.introduce())

teachers = []
teacher1 = Teacher("Timo",43,"male","professor")
teacher2 = Teacher("Jenni",49,"female","lectuer")
teachers.append(teacher1)
teachers.append(teacher2)
for teacher in teachers:
    print(teacher.introduce())

class Assistant(Teacher):
    def __init__(self,name,age,gender,teacher_title,salary):
        super().__init__(name,age,gender,teacher_title)
        self.salary = salary
    def introduce(self):
        return f"my name is {self.name}, I am {self.age} and I am {self.gender}, and my salary is {self.salary}."
class Partime(Teacher):
    def __init__(self,name,age,gender,teacher_title,hours):
        super().__init__(name, age, gender,teacher_title)
        self.hours = hours
    def introduce(self):
        return f"my name is {self.name}. I am {self.age}.I am {self.gender}, and my working hours is {self.hours} hour per day."
assitants=[]
assistant4 = Assistant("Lucy",33,"female","title",6300)
assistant5 = Assistant("Bob",43,"male","title",7000)
assitants.append(assistant4)
assitants.append(assistant5)
for assistant in assitants:
    print(assistant.introduce())
partimes=[]
partime1 = Partime("Jame",23,"female","title",4)
partime2 = Partime("David",30,"male","title",5)
partimes.append(partime1)
partimes.append(partime2)
for partime in partimes:
    print(partime.introduce())

import requests

keyword = input('Enter keyword: ')
request = "https://api.tvmaze.com/search/shows?q=" + keyword
response = requests.get(request).json()
print(response)

for a in response:
    print(a["show"]["name"])

import json
import requests

keyword = input("Enter keyword: ")

# Request template: https://api.tvmaze.com/search/shows?q=girls
request = "https://api.tvmaze.com/search/shows?q=" + keyword

try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()
        # print(json.dumps(json_response, indent=2))
        for a in json_response:
            print(a["show"]["name"])
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")

class Elevator:
    def __init__(self,bottom_floor,top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor = self.current_floor + 1
            print(f"elevator moved up to {self.current_floor}")
    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor = self.current_floor - 1
            print(f"elevator moved down to {self.current_floor}")
    def go_to_floor(self,destination_floor):
        if destination_floor < self.bottom_floor or destination_floor > self.top_floor:
            print(f"wrong floor number")
        while self.current_floor < destination_floor:
            self.floor_up()
        while self.current_floor > destination_floor:
            self.floor_down()
        print(f"elevator gets floor{self.current_floor}")

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
            print("invalid elevator number")

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)

building1 = Building(1,20,5)
building1.run_elevator(2,12)
building1.fire_alarm()


#Implement the following class hierarchy using Python: A publication can be either a book or a magazine.
# Each publication has a name. Each book also has an author and a page count, whereas each magazine has a chief editor.
# Also write the required initializers to both classes.
# Create a print_information method to both subclasses for printing out all information of the publication in question.
# In the main program, create publications Donald Duck (chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages).
# Print out all information of both publications using the methods you implemented.
class Publication:
    def __init__(self,name):
        self.name = name
    def print_info(self):
        return f"the name is {self.name}"
class Book(Publication):
    def __init__(self,name,author,page_count):
        Publication.__init__(self,name)
        self.author = author
        self.page_count = page_count

    def print_info(self):
        return f"the author of the book {self.name} is {self.author} and the book has {self.page_count} pages."

class Magazine(Publication):
    def __init__(self,name,chief_editor):
        Publication.__init__(self,name)
        self.chief_editor = chief_editor

    def print_info(self):
        return f"the chief editor of the magazine {self.name} is {self.chief_editor}"

book1 = Book("Compartment No.6","Rosa Liksom",192)
print(book1.print_info())
magazine1 = Magazine("Donald Duck","Aki Hyyppä")
print(magazine1.print_info())




# Write your solution after the class Car
# Do not make changes to the class!
class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"


def fastest_car(cars):
    return max(cars, key=lambda car: car.top_speed)


# WRITE YOUR SOLUTION HERE:
if __name__ == "__main__":
    cars = []
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)
    cars.extend([car1, car2, car3, car4])
    print(fastest_car(cars))


import requests

# URL of the Flask server
url = "http://127.0.0.1:5000/api/greet"

# Send a GET request with the 'name' parameter
response = requests.get(url, params={"name": "Alice"})

# Print the response from the server
print(response.json())  # Output: {'message': 'Hello, Alice!'}
'''
class Series():
  def __init__(self,title,seasons,genres):
    self.title = title
    self.seasons = seasons
    self.genres = genres
    self.rates = []

  def rate(self,rating):
    self.rates.append(rating)

  def average_rating(self):
    if len(self.rates)>0:
      average=sum(self.rates)/len(self.rates)
      return average
    return 0

  def minimum_grade(rating: float, series_list: list):
      return [series for series in series_list if series.average_rating() >= rating]

  def includes_genre(genre: str, series_list: list):
    return [series for series in series_list if genre in series.genres]

  def __str__(self):
    genre_string = ", ".join(self.genres)
    if len(self.rates) > 0:
      average_rating =self.average_rating()
      rating_info=f"{len(self.rates)} ratings, average {average_rating} points"
    else:
      rating_info="no ratings"
    return f"{self.title}({self.seasons} seasons)\ngenres:{genre_string}\n{rating_info}"


if __name__ == "__main__":
  s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
  s1.rate(5)

  s2 = Series("South Park", 24, ["Animation", "Comedy"])
  s2.rate(3)

  s3 = Series("Friends", 10, ["Romance", "Comedy"])
  s3.rate(2)

  series_list = [s1, s2, s3]

  print("a minimum grade of 4.5:")
  for series in minimum_grade(4.5, series_list):
    print(series.title)

  print("genre Comedy:")
  for series in includes_genre("Comedy", series_list):
    print(series.title)