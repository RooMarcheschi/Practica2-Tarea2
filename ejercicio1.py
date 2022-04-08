file = open('NumPyREADME.md.txt', 'r')

print("Lines of the file that contain http or https: ")

for line in file:
    if "http" in line or "https" in line:
        print (line)

file.close()