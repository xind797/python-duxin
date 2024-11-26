import random
from http.client import responses

'''
#module9
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

def main():
    cars_list = []
    for i in range(1,11):     #注意这个range范围
        registration_number = f"ABC_{i}"
        max_speed = random.randint(100,200) #random取之间的数的格式
        car = Car(registration_number, max_speed)
        cars_list.append(car)

    racing_going = True
    while racing_going:
        change = random.randint(-10,15)
        for car in cars_list:
            car.accelerate(change)
            car.drive(1)

            if car.travelled_distance >= 10000:
                racing_going = False
                break

    print("Final results of the car race:")
    print(f"{'Registration number':12}|{'Max Speed':12}|{'Current Speed':12}|{'Travelled Distance':15}")
    print("-" * 60)

    for car in cars_list:
        print(f"{car.registration_number} | {car.max_speed} | {car.current_speed} | {car.travelled_distance}")

if __name__ == "__main__":
    main()

class Race:
    def __init__(self,name,distance,cars_list):
        self.name = name
        self.distance = distance
        self.cars_list = cars_list

    def hour_passes(self):
        for car in self.cars_list:
            change = random.randint(-10,15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"{'Registration number':12}|{'Max Speed':12}|{'Current Speed':12}|{'Travelled Distance':15}")
        print("-" * 60)
        for car in self.cars_list:
            print(f"{car.registration_number:<25}|{car.max_speed:12}|{car.current_speed:<12}|{car.travelled_distance:<20.2f}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars_list)
    #any函数，有任何一个travelled distance 大于比赛的距离，self distance 就是8000. 函数返回True

def main():
    cars_list = []
    for i in range(1,11):
        registration_number = f"ABC_{i}"
        max_speed = random.randint(100,200)
        car = Car(registration_number, max_speed)
        cars_list.append(car)

    race =Race("Grand Demolition Derby",8000,cars_list)
    hour_passed = 0
    while not race.race_finished():#while not True 就继续比赛，一旦True 达到比赛距离，比赛就结束
        race.hour_passes()
        hour_passed = hour_passed + 1
        if hour_passed % 10 == 0:
            print(f"Hour Passed: {hour_passed}")
            race.print_status()
    print(f"the race is over and time has passed {hour_passed} hours")
    print("-" * 60)
    race.print_status()

if __name__ == "__main__":
    main()

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed,battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed,volume_tank):
        super().__init__(registration_number, max_speed)
        self.volume_tank = volume_tank
def main():
    e_car = ElectricCar("ABC_15",180,52.5)
    g_car = GasolineCar("ABC_123",165,32.3)
    e_car.current_speed=160
    e_car.drive(3)
    print("the electric car has travelled 3 hours and distance is", e_car.travelled_distance)
    g_car.current_speed=145
    g_car.drive(3)
    print("the gasiline car has travelled 3 hours and distance is", g_car.travelled_distance)
if __name__ == "__main__":
    main()

#module10
class Elevator:
    def __init__(self,bottom_floor,top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        # new elevator is always at the bottom floor.
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor <= self.top_floor:
            self.current_floor += 1
        print(f"the elevator now moved up to {self.current_floor}")

    def floor_down(self):
        if self.current_floor >= self.bottom_floor:
            self.current_floor -= 1
        print(f"the elevator now moved down to {self.current_floor}")

    def go_to_floor(self,destination_floor):
        if destination_floor < self.bottom_floor or destination_floor > self.top_floor:
            print("invalid floor number")
        while destination_floor > self.current_floor:
            self.floor_up()
        while destination_floor < self.current_floor:
            self.floor_down()
        print(f"the elevator now moved to {self.current_floor}")


class Building:
    def __init__(self,bottom_floor,top_floor,number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor,top_floor) for _ in range(number_of_elevators)]

    def run_elevators(self,elevator_number,destination_floor):
        if 0<=elevator_number < len(self.elevators):
            self.elevators[elevator_number].go_to_floor(destination_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)

building = Building(1,15,4)
building.run_elevators(3,12)
building.fire_alarm()

#11\inheritance
class Publication:
    def __init__(self,name):
        self.name = name

class Book(Publication):
    def __init__(self,name,author,page_count):
        Publication.__init__(self,name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        return f"The author of the book {self.name} is {self.author} , and the book has {self.page_count} pages"

class Magazine(Publication):
    def __init__(self,name,chief_editor):
        Publication.__init__(self,name)
        self.chief_editor = chief_editor

    def print_information(self):
        return f"The chief editor of the magazine {self.name} is {self.chief_editor}"

book = Book("Compartment No. 6","Rosa Liksom", 192)
print(book.print_information())
magazine = Magazine( "Donald Duck "," Aki Hyyppä")
print(magazine.print_information())


#12 using external interfaces
import requests
def get_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json().get('value')
        print(joke)
    else:
        print("get joke failed")
get_joke()

def get_weather(city_name):
    api_key = "457738d7dd71b9a371ca30d6d34fa8e4"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_discription = data['weather'][0]['description']
        temperature = data['main']['temp']
        print(f"weather in {city_name} is {weather_discription.capitalize()}")
        print(f"temperature is {temperature}")
    else:
        print("get weather failed")
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)



#module13 setting up a backend service with an interface
from flask import Flask, jsonify
import math
app = Flask(__name__)
def check_prime(number):
    if number<=1:
        return False
    for i in range(2,int(math.sqrt(number))+1):
        if number%i == 0:
            return False
    return True

@app.route("/prime_number/<int:number>")
def is_prime(number):
    number_is_prime = check_prime(number)
    response = {
        "Number": number,
        "is_prime": number_is_prime}

    return jsonify(response)
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

#13-2
from flask import Flask, jsonify
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_simulator",
    user="root",
    password="123456",
    autocommit=True,
    charset='utf8mb4',
    collation='utf8mb4_general_ci'
)
app = Flask(__name__)
@app.route("/airport/<icao>")
def get_airport(icao):
    try:
        with connection.cursor(dictionary=True) as cursor:  # Use dictionary=True for row mapping
            sql = "SELECT ident AS ICAO, name AS Name, municipality AS Location FROM airport WHERE ident = %s"
            cursor.execute(sql, (icao,))
            result = cursor.fetchone()

            if result:
                return jsonify(result)
            else:
                return jsonify({"error": "No airport found"}), 404
    except mysql.connector.Error as err:
        return jsonify({"error": f"Database error: {err}"}), 500

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
'''
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/airport/<icao>')
def airport(icao):

  # add database query here
  return {'ICAO': icao, 'Name': 'Airport name'}