print('----Phone book----')
users_info = [
{ 'username': 'Amal','PhoneNumber':'1111111111'},    
{ 'username': 'Mohammed','PhoneNumber':'2222222222'},    
{ 'username': 'khadijah','PhoneNumber':'3333333333'}, 
{ 'username': 'Adbullah','PhoneNumber':'4444444444'},    
{ 'username': 'Rawan','PhoneNumber':'5555555555'},    
{ 'username': 'Faisal','PhoneNumber':'6666666666'},    
{ 'username': 'layla','PhoneNumber':'7777777777'}  ]

Ph_Number =input('Enter your phone Number : ')

for i in users_info:
    if Ph_Number == i['PhoneNumber']:
     print('This is you name',i['username'], 'And this is your Phone number' ,i['PhoneNumber'])

def Search_for_phone_number(x): 
  for i in users_info:
      if x == i['PhoneNumber']:
         return True
      
  return False

if Search_for_phone_number(Ph_Number) == False:
    print('This number doesnt exist!')

    answer = input('Do you wanna save this number (yes/no)?').lower()
    if answer =='yes':
        newPhonenum =input('Enter your new number : ')
        newName =input('Enter your new name : ')

        newUser = {'username':newName ,'PhoneNumber':newPhonenum }
        users_info.append(newUser)
        print('GOOOD BYE <3')