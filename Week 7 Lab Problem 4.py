#Name of File: Week 7 Lab Problem 4

#Jesus Navarrete
#11/12/2020

#This program implements that you have 10 arrows and takes your score and adds
#them to a score card

#Program works find but is missing a way to add all the scores together from
#score but DOES add them up on score card. Not sure if this is what we had to do.


import random
import math

score = 0
arrows = 10
SC = []

count = 0
while count < 10:
    count += 1
    arrows -= 1
    score = (random.randint(0,10))
    SC.append(score)
    
    if score == 0:
        count -= 1
        arrows += 1
        
    if score == 10:
        SC.remove(10)
        SC.append(20)
    
    print(score)
print(SC)


print("Your final Score were: ")
print("This is your Score Card: ", sum(SC))
