import datetime

print('---Age in Days Calculator---')
user_age = int(input('Enter your Age : '))
day = datetime.date.today()
year_of_birth =(int(day.year)-user_age)
Total_days= user_age * 365
print(' From this year',year_of_birth,'you Lived',Total_days,'day')

