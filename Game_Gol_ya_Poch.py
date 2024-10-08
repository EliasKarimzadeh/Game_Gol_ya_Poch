""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    | $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ |
    | $  /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\  $ |
    | $ / @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \ $ |
    | $ \ @                                                                  @ / $ |
    | $ / @                      ELIAS KARIMZADEH                            @ \ $ |
    | $ \ @                                                                  @ / $ |
    | $ / @              GitHub: github.com/EliasKarimzadeh                  @ \ $ |
    | $ \ @             Linkdin: in/elias-karimzadeh-a7a9b8283               @ / $ |
    | $ / @            Instagram : instagram.com/elyaskarymzade              @ \ $ |
    | $ \ @                                                                  @ / $ |
    | $ / @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \ $ |
    | $ \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ $ |
    | $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ |
    |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|"""
    

import random

print('Hello \n welcom to Game Gol ya poch')

while True:
    user_test = 0
    cups = []
    while True:
        try:
            user_cups = int(input('How many cups ?'))
            break
        except ValueError:
            print('Invalid input . Plese try again')
            
            
    user_chances =input('How many chances ?')
    
    for a in range(user_cups):
        cups.append(a)
        
    AI_choose = random.choice(cups)
    
    while user_test < int(user_chances):
        user_choose = input(f'Which glass is the gool in? {cups}')
        if int(user_choose) == AI_choose:
            print('good job :))')
            break
        else:
            print('Your Choise not True')
        user_test += 1
        
    print(f'Result = The gool was in glass {AI_choose}')
    
    user_q = input('Do you want to continue the game?(yes or no)')
    
    if user_q == 'no':
        break