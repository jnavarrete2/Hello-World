#This program will take a password from the user and print an appropriate message
#The 'in' keyword checks to see if a value exists somewhere in the given string.

greeting = input("Hello, possible pirate! What's the password?")
#chaning 'in' to == would make it so that anyone who is not a pirate can
#join this meeting if they don't type 'Arrr!'
if greeting == ("Arrr!"):
	print("Go away, pirate.")
else:
        print("Greetings, hater of pirates!")
