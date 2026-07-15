print('welcome to my calculus\n')

Number_one=input('Enter your first Number : ')
Operation =input('enter your first Operation( * , / , + , - , % ) : ')
Number_two =input('Enter your second Number :')

print('----------------------------------')

if Operation == '+' :
    print('The reslut of ',Number_one,' + ',Number_two,' = ',Number_one + Number_two)

     
elif Operation == '-' :
    print('The reslut of ',Number_one,' - ',Number_two,' = ',Number_one - Number_two)

     
elif Operation == '*' :
    print('The reslut of ',Number_one,' * ',Number_two,' = ',Number_one * Number_two)

    
elif Operation == '%' :
   print('The reslut of ',Number_one,' % ',Number_two,' = ',Number_one % Number_two)

elif Operation == '/' :

    if Number_two != 0:

     print('The reslut of ',Number_one,' / ',Number_two,' = ',Number_one / Number_two)

    else:
        print('can not divid by zero')
         
else:
    print('value is not viold')


