import random

number = random.randint(1,10)

def main_game(number_of_Attempts):

 user_number = int(input('Enter guess number between 1 and 10 : '))
 if  user_number < number:
     print('Not Correct!')
     print('It is low guess')
 elif user_number == number:
     print('It is correct You win <3')
     print('YOU TAKE',number_of_Attempts,'TIMES TO GUESS')
     return False
         
 else:
     print('Not Correct!')
     print('It is high guess')

print('Welcomt to number guessing game!')

number_of_Attempts = 0
while True:
   number_of_Attempts +=1
   main_game(number_of_Attempts)
   if False:
     break  

