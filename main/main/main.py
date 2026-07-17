from login_system import login_system_Home
from login_system import main_menu
from login_system import about

print('====LOGIN SYSTEM====')

def LOGIN_SYSTEM():

    Uname = input('Enter your name : ').lower()
    UpassWord = input('Enter Your password : ')
#========================================================================
    if Uname == 'anfal' and UpassWord == '2003':
      login_system_Home(Uname)
      main_menu()

      choice = input('Enter Your choice.. ')
      if choice == '1':
        print('Your name is :',Uname)
        print('Your age is : 23')

      elif choice =='2':
        newPassword = input('Enter your new password :')
        UpassWord = newPassword
        print(' password changed successfully ')

      elif choice =='3':
        print('Login out...')

      elif choice =='4':
          about()

      else:
        print('Incorrect information')
    
    elif Uname == 'sara' and UpassWord == '2003' .lower():
      print('The username is wrong !!')

    else:
         print('The username and Password are incorrect !!')
#========================================================================
i=0
while i <= 4 :
  LOGIN_SYSTEM()
  i+=1
  if i==3:
   print('Sorry try later ')
   break
  answer= input('Do you want to try again? (yes/no)')
  
  if answer=='no':
     print('EXIT')
     break  
#=======================================================================

