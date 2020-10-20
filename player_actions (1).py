#player_actions.py


def check_play_again(user_input):
    #This first if statement allows the user to type yes so they can play again
    if user_input == "Y":
        print("Play again")
    #This next elif statement allows the user to quit the game by typing N for No
    elif user_input == "N":
        print ("Quit Game")
      #I needed this input so that the user could know that any other letter would
    # not be taken as it would mean the input is invalid
    else:
        print ("Invalid input")
    


check_play_again(input("Would you like to play again? Type Y for Yes or N for No: \n"))
