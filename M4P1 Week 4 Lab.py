#This program takes the current time in hours between 0-23
#and the number of hours the user will wait.
#It will print what the time is in hours (between 0-23) after the user is done waiting
currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait?")



currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)
#This line of code allowed the computer to go back to 0-23 once 23 was reached.
#Meaning (23+4)%24 will be 3 and not just 26 like before
finalTimeInt = (int(waitTimeStr) + int(currentTimeStr)) % 24
print(finalTimeInt)
