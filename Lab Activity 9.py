def greet():
    user=input("Who are you: ")
    print("Nice to meet you ", user)

greet()


#you will have to remove the comment on line 12 but do that on your own cost!
def infinite():
    while True:
        print("Hello World")
#infinite()

def even(n):
    if (n%2==0):
        return True
    else:
        return False
print(even(9))


import random

def numbers():
    n = random.randint(1,100)
    n1 = random.randint(1,100)
    n2 = random.randint(1,100)
    print(n)
    print(n1)
    print(n2)
numbers()
