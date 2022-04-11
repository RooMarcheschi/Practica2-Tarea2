with open('nombres_1.txt', 'r') as name:
    names = name.read().split(',')
with open('eval1.txt', 'r') as grade1:
    grades1 = grade1.read().split(',')
with open('eval2.txt', 'r') as grade2:
    grades2 = grade2.read().split(',')

dict = {}
    #print(len(names), len(grades1), len(grades2)) --> 47
avarage = 0
x = len(names)
for student in range(x):
    dict[str(names[student])] = int(grades1[student]) + int(grades2[student])
    avarage = avarage + int(grades1[student]) + int(grades2[student])

#for student in dict:
#    print(student, dict[student])
avarage = avarage//len(names)
print("The avarage grade is ", avarage)
print("And the students with grades under the avarage are: ")
for student in dict:
    if dict[student] < avarage:
        print(student, dict[student])
