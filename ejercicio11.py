with open('nombres1.txt', 'r') as name1:
    names1 = name1.read().split(',')
with open('nombres2.txt', 'r') as name2:
    names2 = name2.read().split(',')

namess1 = [i.strip() for i in names1]
namess2 = [i.strip() for i in names2]

merge = [name for name in namess1 if name in namess2]
print("Nombres que aparecen en los archivos nombres1 y nombres2: ")
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

print("Impresion de notas de los alumnos en nombres1: ")
print(f"{'ID':<5}{'Nombre':<20}{'Eval1':<8}{'Eval2':<8}{'Total':<8}")
print('-------------------------------------------------------')
for i in range(len(namess1)):
    print(f"{i:<5}{namess1[i]:<20}{int(grades1[i]):<8}{int(grades2[i]):<8}{int(totals[i]):<8}")
