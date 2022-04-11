with open('nombres1.txt', 'r') as name1:
    names1 = name1.read().split(',')
with open('nombres2.txt', 'r') as name2:
    names2 = name2.read().split(',')
#names1 = set(names1)
#names2 = set(names2)
#merge = names1.intersection(names2)
merge = [name for name in names1 if name in names2]
print("Nombres que aparecen en los archivos bombres1 y nombres2: ")
for name in merge:
    print(name)

#---------------------------------------

with open('eval1.txt', 'r') as grade1:
    grades1 = grade1.read().split(',')
with open('eval2.txt', 'r') as grade2:
    grades2 = grade2.read().split(',')

totals = []
for i in range(len(grades1)):
    totals.append(int(grades1[i])+int(grades2[i]))

#zipped = zip(names1, grades1, grades2, totals)
#for student in zipped:
#    print(student)

#for i, (Nombres, Eval1, Eval2, Total) in enumerate(zip(names1, grades1, grades2, totals)):
    #print(i, Nombres, Eval1, Eval2, Total)
    #print(f"{int(i)}     {str(Nombres)}   {int(Eval1)}  {int(Eval2)}  {Total}")




print("Impresion de notas de los alumnos en nombres1: ")
list = []
for student in range(len(names1)):
    #list.append([str(names1[student]),int(grades1[student]),int(grades2[student]),int(grades1[student])+int(grades2[student])])
    list.append(f"{names1[student]}   {int(grades1[student])}   {int(grades2[student])}   {int(grades1[student])+int(grades2[student])}")

for elem in list:
    print(elem)


"""
#print("      "+"Nombre  "+"    "+"Eval1   "+"Eval2   "+"Total   ")
#for i in range(len(names1)):
#    print(f"{i}     {list[i][0]}    {list[i][1]}     {list[i][2]}     {list[i][3]}")

print ("{:<8} {:<15} {:<10} {:<10}".format('Pos','Nombre','Eval1','Eval2','Total'))
for l in list:
    Nombre, Eval1, Eval2, Total = l
    print ("{:<4} {:<15} {:<10} {:<10} {:<10}".format(l, Nombre, Eval1, Eval2, Total))"""