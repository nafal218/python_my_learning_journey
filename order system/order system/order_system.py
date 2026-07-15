
order = input('What do you want ? (Cake / Candy)').lower()

if order == 'cake':
 Cake_type = input('Do you want it with (Vanilla/Chocolate)?')

 if Cake_type =='vanilla'.lower():
     print('it costs you about 2$', end= ' ')
     print('here your order !')

 elif Cake_type =='chocolate'.lower():
     print('it costs you about 3.50$', end= ' ')
     print('here your order !')
 else:
    print('sorry')

    
if order == 'candy':
 Candy_type = input('Do you want it (sour/sweet)?')

 
 if Candy_type =='sour'.lower():
     print('it costs you about 1.09$', end= ' ')
     print('here your order !')

 elif Candy_type =='sweet'.lower():
     print('it costs you about 1,50$', end= ' ')
     print('here your order !')
 else:
    print('sorry')
