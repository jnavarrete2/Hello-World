#This code returns some mad libs text based on the user input
#Is the code always returnin the correct input?
#What do you think I did to write this code that I shouldn't have done?

user = input("What ajective should I use: ")

def change_name(adjective):
    if adjective == 'red':
        return "The quick brown fox jumps over the red dog"
    elif adjective == 'lazy':
        return "The quick brown fox jumps over the lazy dog"
    elif adjective == 'energetic':
        return "The quick brown fox jumps over the energetic dog"
    elif adjective == 'happy':
        return "The quick brown fox jumps over the happy dog"
    elif adjective == 'sad':
        return "The quick brown fox jumps over the sad dog"
    else:
        return "No case for that adjective found!"

print(change_name(user))

#There were some bugs here like in line 17 where 'happy' was used over sad since
#it seemed to be just a normal copy and paste so I just chnaged the world to 'sad'

#I also added lines 5 and lines 21 so that the user would be asked to give an
#adjective and then print out that adjective from the set we have with them.
