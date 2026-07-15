grades =[38,89,99,67,82,34,47,73,90,22,58,57,79,80,99,41,62,86,100,30,15,54,63,24,89,79,25,64,83]
passed_student=[]
number_of_pass =0
failled_student=[]
number_of_fail=0

for i in (grades):
    if i>=50:
     passed_student.append(i)
     number_of_pass+=1

    else:
        failled_student.append(i)
        number_of_fail+=1


print("passed student : ", passed_student,'The total -> (',number_of_pass,')')
print("failled student : ", failled_student,'The total -> (',number_of_fail,')')
