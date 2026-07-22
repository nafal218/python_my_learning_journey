print('----Phone book----')

users_info = [
{ 'username': 'Amal','PhoneNumber': '1111111111'},    
{ 'username': 'Mohammed','PhoneNumber': '2222222222'},    
{ 'username': 'khadijah','PhoneNumber': '3333333333'}, 
{ 'username': 'Adbullah','PhoneNumber': '4444444444'},    
{ 'username': 'Rawan','PhoneNumber': '5555555555'},    
{ 'username': 'Faisal','PhoneNumber': '6666666666'},    
{ 'username': 'layla','PhoneNumber': '7777777777'}    
    ]

#+++++++++++++++++++++++++++++++++++++++++++++++
# يتحقق من الرقم 
def Check_Ph_number(Ph_Number):
    if len(Ph_Number) == 10 and Ph_Number.isdigit():
        return True
    else:
       print('It must be 10 numbers and without special Characters or letters ')
       return False
         
#+++++++++++++++++++++++++++++++++++++++++++++++
#  داله تتحقق من الرقم والاسم وتطبعه وفي نفس الوقت ترجع قيمعه البحث
def Search_for_phone_number(Ph_Number): 
    for i in users_info:
        if Ph_Number == i['PhoneNumber']:
         print(f"This is you name{i['username'] }And this is your Phone number{i['PhoneNumber']}")
        
         return True
    return False
#+++++++++++++++++++++++++++++++++++++++++++++++

while True:
   Ph_Number = input('Enter your phone Number : ')

   if  Check_Ph_number(Ph_Number) == True:
    if not  Search_for_phone_number(Ph_Number): 
      print('This number doesnt exist!')

      answer = input('Do you wanna save this number (yes/no)?').lower()
      if answer =='yes':
         newPhonenum = Ph_Number
         newName = input('Enter your new name : ')
         newUser = {'username':newName ,'PhoneNumber':newPhonenum }
         users_info.append(newUser)
      else:
        print('GOOOD BYE <3')
        
   else:
     continue
     