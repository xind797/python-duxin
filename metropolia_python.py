import math
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
'''
#peoblem4
year = int(input("enter year:"))
if year % 100 !=0 and year % 4 == 0:
    print(f"year {year}  is a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print(f"year {year} is a leap year")
else:
    print(f"year {year} is not a leap year")