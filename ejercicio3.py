import string
text = """Dado un texto solicite por teclado una letra e imprima las palabras que comienzan con dicha letra.
En caso que no se haya ingresado una letra, indique el error.
Ver: módulo string"""

char = input("Enter a letter: ").lower()

if char in string.ascii_letters:
    words = set(text.lower().split(" "))
    # print (words)
    # print(type(words))
    print(f"Words that start with {char}")
    for word in words:
        #print(word + "      " + char + "      " , word.startswith(char))
        if word.startswith(char):                                           # texto.lower().split()[0].startswith(caracter))
            print(word)                                                     # print(text.lower().split()[0].startswith(char))
else:
    print("ERROR: The character entered is not a letter!")