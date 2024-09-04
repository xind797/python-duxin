import math
from ctypes import pythonapi
from random import randint

from babel.numbers import number_re
from docutils.nodes import header




'''
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

#2708-1
money=float(input("input money:"))
if money>=5:
  print("you can buy a latte")

#2708-2
age=int(input("age:"))
if 15<=age<18:
    weight=float(input("weight(kg):"))
if (age>=18 or ( 15<=age<18 and weight>=55) ):
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
number=0
while True:
    user_number = int(input("enter a guessing number between 1 and 9:"))
    if user_number == target_number:
        print(("well tried"))
        break
    else:
        print(("try again"))
        number=number+1
    print("tried",number)

#2908-excercise 2
user_input=""
while user_input != "exit":
    user_input = input("type something (or exit to quit):")
    print("you typed:" ,user_input)

#2908-excercise 2
import random
flipcoin = random.choice(["head","tail"])
while flipcoin != "head":
    print("flipped:",flipcoin)
    flipcoin = random.choice(["head","tail"])
    print("you flipped",flipcoin)
    

#conditional (if)
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
name = input('enter your name or quit by entrting "": ' )
while name != '':
    names.append(name)
    name = input('enter your name or quit by entering "":' )
print(names)


#while loop-assignment
#1
#Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
num1 = 1
while num1 < 1000:
    if num1 % 3 == 0:
        print(num1)
    num1 = num1 + 1

#2
#Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
length = float(input("enter the length (inch): "))
converted = float(length * 2.54)
while length >= 0:
    print(f"coverted into centimeters is,{converted}","centimeters")
    length = float(input("enter the length (inch): "))

#3
#Write a program that asks the user to enter numbers until they enter an empty string to quit.
#Finally, the program prints out the smallest and largest number from the numbers it received.

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
#Write a game where the computer draws a random integer between 1 and 10.
#The user tries to guess the number until they guess the right number.
#After each guess the program prints out a text: Too high, Too low or Correct.
#Notice that the computer must not change the number between guesses.
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
#Write a program that asks the user for a username and password.
# If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times.
# If the information is correct, the program prints out Welcome.
# After five failed attempts the program prints out Access denied. The correct username is python and password rules.
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
    
'''

#Let's generate a large number of random points, such as one million, inside square B.
# Let N be the total number of random points. Each point inside the square is tested for whether it resides inside circle A.
#Let n be the total number of points that fall inside circle A. Now we have n/N≈π/4, and from that we get π≈4n/N.
# Write a program that asks the user how many random points to generate,and then calculates the approximate value of pi using the method explained above.
# At the end, the program prints out the approximation of pi to the user.
# (Notice that it is easy to test if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).
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

