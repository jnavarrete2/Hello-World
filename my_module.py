#Jesus Navarrete

#November 10 2020

#This function uses a for loop to print 10 integers  from 25 and 35 randomly

import random

for l in range(10):
    print(random.randint(25,35))
print("End of Problem 1")

#This function will take a list as a parameter and returns a random element from a list

G =[2, 3, 5, 7, 11, 13, 17]

print(random.choice(G))

print("End of Problem 2")

#This function returns a random odd interger from 0 to 100

N = range(101)

range(0, 101)

for number in N:
    if number % 2 !=0:
        print(number)

print("End of Problem 3")

#This function calculates the Pythagorean theorem using functions found in the math module

#The pythagorean theorm is can be written as A**2+B**2=C**2 so with that I came up with this
import math

def Lenght1():
    lenght = float(input("Give me A: "))
    return lenght

def Lenght2():
    lenght2 = float(input("Give me B: "))
    return lenght2

s1 = Lenght1()
s2 = Lenght2()

c = s1*s1 + s2*s2

c = math.sqrt(c)

print(c)

print("End of Problem 4")
    
