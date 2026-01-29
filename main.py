# Author: Dhruv
# RANDOM THAT USE TO CHOSE RANDOM NUMBER WHICH ARE GIVEN 
import random

'''
1 for snake
-1 for water 
0 for gun
'''

# COMPUTER TAKE A RANDOM NUMBER
computer = random.choice([-1 , 0 , 1])

'''THIS IS THE SECOUND WAY THAT YOU CAN USE BUT NOT FOR IMPLEMENT ITS JUST FOR EDUCATION'''
# your_choice_convert = int(input("Enter your choice :"))
# your_Dict= {1 : "s" , -1 : "w" , 0 : "g"}  
# print (f"You chose {your_Dict[your_choice_convert]}\nComputer chose {your_Dict[computer]}")

'''THIS IS THE RIGHT WAY'''
your_choice = input("Enter your choice :")

you_Dict = {"s" : 1 ,"w" : -1 ,"g" : 0}  
reverse_Dict = {1 : "s" , -1 : "w" , 0 : "g"}

your_choice_convert = you_Dict[your_choice] 

print (f"You chose {reverse_Dict[your_choice_convert]}\nComputer chose {reverse_Dict[computer]}")

# LOOP STARTS FROM HERE 
if (computer == your_choice_convert):
    print("Its a draw!")

else:
    
    if (computer == -1 and your_choice_convert == 1): 
        print("You Win!")

        '''(computer - you) = -2'''

        '''YOU CAN TAKE YOUR CHOICE CONVERT BUT THEN YOU NEED TO DO LIKE THAT
        YOUR_CHOICE_CONVERT - COMPUTER = 2'''


    elif (computer == -1 and your_choice_convert == 0):
        print("You Lose!")

        '''(computer - you) = -1'''

        '''YOU CAN TAKE YOUR CHOICE CONVERT BUT THEN YOU NEED TO DO LIKE THAT
        YOUR_CHOICE_CONVERT - COMPUTER = 1'''


    elif (computer == 1 and your_choice_convert == -1):
        print("You Lose!")

        # '''(computer - you) = 2'''

        '''YOU CAN TAKE YOUR CHOICE CONVERT BUT THEN YOU NEED TO DO LIKE THAT
        YOUR_CHOICE_CONVERT - COMPUTER = -2'''


    elif (computer == 1 and your_choice_convert == 0):
        print("You Win!")

        # '''(computer - you) = 1'''

        '''YOU CAN TAKE YOUR CHOICE CONVERT BUT THEN YOU NEED TO DO LIKE THAT
        YOUR_CHOICE_CONVERT - COMPUTER = -1'''


    elif (computer == 0 and your_choice_convert == -1):
        print("You Win!")

        # '''(computer - you) = 1'''

        '''YOU CAN TAKE YOUR CHOICE CONVERT BUT THEN YOU NEED TO DO LIKE THAT
        YOUR_CHOICE_CONVERT - COMPUTER = -1'''


    elif (computer == 0 and your_choice_convert == 1):
        print("You Lose!")

        # '''(computer - you) = -1'''

        '''YOU CAN TAKE YOUR CHOICE CONVERT BUT THEN YOU NEED TO DO LIKE THAT
        YOUR_CHOICE_CONVERT - COMPUTER = 1'''


    else:
        print("something went wrong")
        # LOOP ENDS HERE
        
    ''' BELOW IS THE ADVANCE WAY TO DO THAT BUT STILL YOU NEED
    THAT ABOVEWAY TO CALCULATE THE PROBLEM OR YOU CAN DI IT NO
    PAGE OR WHERE EVERY BUT STILL GOING ADVANCE NEED TO ABOVE
    BASIC TO UNDERSTAND WHEN YOU LOSE THE GAME AND WHEN YOU WIN
    THE GAME'''
    
    '''LOOP STRTS FROM HERE'''
    # if ((computer - your_choice_convert == -1) or (computer - your_choice_convert == 2)):
    #     print("You Lose!")

    # else:
    #     print("You Win!")
    '''LOOP ENDS HERE'''

    # '''THERE ARE TWO WAYS THAT YOU CAN MAKE THIS GAME EVEN SHORT BUT MORE COMPLEX AND REDUCE READABILITY'''

    '''LOOP STARS FROM HERE'''
    # if ((your_choice_convert - computer == -1 or your_choice_convert - computer == -2)):
    #     print("You lose!")

    '''LOOP ENDS HERE'''
    # else:
    #     print("You win!") 
