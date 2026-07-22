import time
print('Welcome To the Pomodoro Timer!!')

Time_in_minutes= int(input('Enter Time in minutes : '))
# عمليه تحويل الدقايق الى ثواني
Time_in_second=Time_in_minutes*60
#Time_in_second يبداء من 
# بهدف يوصل الى صفر 
# عدد الخطوات سالب لان مافيه خطوات
for Time_in_second in range(Time_in_second,0,-1):
  time.sleep(1)
  # احسب القسمه 
  # بدزن الكسور
  min = Time_in_second // 60
  # احسب باقي القسمه 
  sec = Time_in_second % 60

  t_format = f"{min:02d}:{sec:02d}"

  print(f"time remeaining :{t_format}")
 
print('times up!!')































