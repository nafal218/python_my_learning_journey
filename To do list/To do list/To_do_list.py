
# جزء اضافه المهام


tasks_list=[]

def add_task (tasks_list):
    Current_task = input('Please Enter Your Task : ')
    task_id = len(tasks_list)+1
    task_ad ={task_id:Current_task}
    tasks_list.append(task_ad)
    #print('TASKS : ',tasks_list)

# جزء حذف المهام
def delete_task (tasks_list):
    task_num = int(input('Please enter task number: '))
    for num in tasks_list:# "لكل قاموس في ليست "يبحث
        key1 = next(iter(num)) # نكست واتر يدخلوني داخل قاموس ويرجعون لي فيي هاذي الحاله قيمه المفتاح
        if key1 == task_num:# لو المفتاح حق القاموس يساوي القيمه المدخله
         Answer = input('Are you sure you wont delete this task ?...(yes/no)').lower()
         if Answer =='yes':
          tasks_list.remove(num)# احذف القاموس
         else:
            print('')

# عرض قائمه المهام
def show_tasks (tasks_list):
    for t in tasks_list:
        for task_iD ,task_name in t.items():
         print('TASK : ', task_iD,':',task_name,'\n')

#خروج من البرنامج
def Exit ():
  Answer_exit = input(' Are you sure you wanna exit ?...(yes/no) ').lower()
  if Answer_exit == 'yes':
   return True
  else:
   return False


while True:
   main_list ={ 
        1:add_task,
        2:delete_task,
        3:show_tasks,
        4:Exit
        }

   print (' WELCOME TO DO LIST ')                
   print('--- Options ---')
   print('1:ADD TASK..')
   print('2:DELETE TASK..')
   print('3:SHOW TASKS..')
   print('4:EXIT..')
   print('---------------')
  
   user_Choice = (input('Please Select operation number :'))
   if user_Choice.isdigit():#لو القيمه الي داخل النص رقم 
    user_Choice= int(user_Choice)#حوليها الى رقم صحيح
   if user_Choice not in main_list : # لو كان النص مو موجود داخل القائمه اطبع الرساله واطلع
      print('it is not correct values (Please check the number in the list !!)')
      break
   
   if user_Choice == 4:
    action = main_list[user_Choice]()
    
    if action == True:
     break
    else:
     continue

   else:
    action = main_list[user_Choice](tasks_list)
   
   