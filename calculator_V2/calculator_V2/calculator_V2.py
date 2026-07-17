from tools import addition
from tools import subtract
from tools import multiply
from tools import division

print('========CALCULATOR========')

   
def CALCULATOR():
        number1= int(input('Enter your first number : '))
        number2= int(input('Enter your second number : '))
        operator = input('Choose your operator (*,/,+,-) ')
        #======================================================
        if operator =='+':
            print('The Result = ',addition(number1,number2))

        elif operator =='-':
            print('The Result = ',subtract(number1,number2))

        elif operator =='*':
            print('The Result = ',multiply(number1,number2))

        elif operator =='/':
            if number2==0:
               print('It is not allowed to divide sero ')
            else:
              print('The Result = ',division(number1,number2))

        else:
            print('Invalid value: ')
        #======================================================

while True:
    CALCULATOR()
    Try_again =input('DO YOU WANT TO TRY AGINA ?...(YES/NO)').lower()  

    if Try_again =='no': 
      print('OK, GOOD BYE <3')
      break
       #======================================================
    
