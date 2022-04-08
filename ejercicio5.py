phrase = input("Enter a phrase: ").lower().split(" ")
word = str(input("Enter a word: ").lower())

#print(phrase.count(word)) # Esta solucion no sirve xq no tiene en cuenta que algunas palabras estan seguidas de signos de puntuacion, y por ende no las cuenta cuando deberia

occurences = 0
for elem in phrase:
    if word in elem:    # De esta forma contamos todas las palabras aunque esten seguidas de un signo de puntuacion.
        occurences += 1

print(f"The number of times that the word appears in the phrase is {occurences}")