import string
import funcionesEjercicio2 as func

with open('NumPyREADME.md.txt', 'r') as file:
    text = file.read()  # Es necesario hacer esto xq file es de un tipo usado para los archivos de texto
                        #y hacer file.read() convierte al archivo en tipo str, lo q nos permite luego hacer...
#print(type(text))
#print(text.lower().split())    # ESTO!!! ;) --> un set con TODAS las palabras q aparecen en text
                                    # o esto, si no queremos q las palabras se repitan set(text.lower().split())

all = text.lower().split()
just_words = func.remove_not_words(all)
#print(type(all_words))
print(f"The word that appears the most in the file is {func.most_frequent(just_words)}")
file.close()