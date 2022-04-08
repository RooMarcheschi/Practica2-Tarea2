import string

def remove_spaces(string):
    return string.replace(" ", "")
    #return "".join(string.split())

def is_heterogram(phrase):
    phrase = [''.join(char for char in stri if char in string.ascii_letters) for stri in phrase]    #solo deja en las phrase(stri) los caracteres(char) que son letras (string.letters)
    phrase[:] = [item for item in phrase if item != ''] #elimina los elementos vacios(?) entre palabras
    #print(phrase)
    #print(set(phrase))
    if len(phrase) == len(set(phrase)):   #compara si la cantidad de letras de phrase en set (sin repetir letras) es igual a la version original (la q contiene las supestas repeticiones)
        return True
    else:
        return False

for i in range(10):
    phrase = input("Enter a word or a phrase to check if it's an heterogram: ").lower()
    print("Is the entered phras an heterogram? " , is_heterogram(phrase))