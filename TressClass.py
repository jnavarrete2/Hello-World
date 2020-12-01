#Jesus Navarrete
#November 30, 2020
#Lab: Module 8
#This lab cover the item that I will make for my main game

#I have to import the random module because I will use it to make
#certain amount of the item.
import random
#I made the class for different tress in the game
#this meant that I just had to give it a name, which can be anything
#and also just set in a list which is called world since it's a class
#that will be things within the game world, not interactable.
class tree:
    name = ""
    world = []
#I defined the class and made sure to spawn a random amount of trees.
    #The reason for this is because I want to be able to change the
    #way that the battle area looks for every fight. 
def __init__(self,new_name):
    self.name = new_name
    self.spawn = random.randint(20,50)
