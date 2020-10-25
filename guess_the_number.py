#First of all I ask the player with which range of number 
#from 0 he/she want's to play:
def range_of_num():
    range_num=0
    print("Hi!! Can you guess the number I'm thinking of?\nLet's play!!")        
    while range_num ==0:   
        try:
            print("Choose the range of numbers from 0, you want to play with")
            range_num=int(input())
        except:
            print("Please check your spelling.\nYou should enter an integer number")
            range_num=0
    return range_num

#Here I give the player the chance to choose the number of oportunities he/she wants:
def chances():
    chan=0
    while chan==0:
        try:
            print("How many oportunities would you need?")
            chan=int(input())
        except:
            print("Please check your spelling.\nYou should enter an integer number")
            chan=0
    return chan


#Then I define a function to make the program get a random number 
#from the range. This is why I have to import randint from random:
from random import randint
def random_number():
    rand_num=randint(0,range_num)
    return rand_num

#This is the function to ask the player for a guessed number:
def player_input():
    print("Guess a number from 0 to",range_num)
    player=int(input())
    return player

#Then I create the development of the game:
def game():
    if player < rand_num:
        print("Oops almost!\nThe correct number is higher.")
        return 0
    elif player > rand_num:
        print("Oops almost!\nThe correct number is lower.")
        return 0
    else:
        print("That is correct!! Congratulation!!")
        return 1


#And last but not least the ejecution of the game:

rounds=0
range_num=range_of_num()
chan=chances()
rand_num=random_number()
while rounds < chan:
    player=player_input()
    playing=game()
    if playing == 0:
        fails=+1
        rounds+=1
    else:
        break
percentage_succ=(chan/(range_num+1))+100
rate_succ=(fails/rounds)*100
if rounds == chan:
    print("Ooohh! You lost the game!")

#I have taken the liberty of adding a little joke for the end of the game:

print("Your success rate was:",percentage_succ,"%. Would you like to try again, yes or not?")
again=str(input())
if again == "yes":
    print("Don't be lazy and get to work now!")
else:
    print("Well done! Don't waste your time!")

        