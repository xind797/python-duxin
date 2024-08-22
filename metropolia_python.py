import math
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

