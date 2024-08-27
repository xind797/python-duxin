import math

import yes

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
'''
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

