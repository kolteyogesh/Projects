from random import randint
#create list of play options
t = ['Rock','Paper','Scissors']
# assign random play to computer
computer = t[randint(0,2)]
#set player to false
player = False
while player == False:
#set player to false
    player = input("Rock,Paper,Scissors?")
    if player == computer:
        print('Tie!')
    elif player == 'Rock':
            if(computer == 'Paper'):
                print('You lose!',computer,'covers',player)
            else:
                print('You win!',player,'smashes',computer)
    elif player == 'Paper':
            if(computer == 'Scissors'):
                print('You lose!',computer,'cuts',player)
            else:
                print('You win!',player,'covers',computer)
    elif player == 'Scissors':
            if(computer == 'Rock'):
                print('You lose!',computer,'smashes',player)
            else:
                print('You win!',player,'cuts',computer)
    else:
        print('Thats not valid play..........Check spelling!')
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]          
