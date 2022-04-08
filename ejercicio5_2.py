cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !): ")
if len(cadena) < 10:
    print("Clave invalida: ingresaste alguno de estos simbolos @ !" if cadena.count("@") + cadena.count("!") > 0 else "Clave valida!") 
else:
    print("Ingresaste más de 10 caracteres.")

# Incluso se puede hacer como abajo y funciona, pero queda ilegible
#print(("Clave invalida: ingresaste alguno de estos simbolos @ !" if cadena.count("@") + cadena.count("!") > 0 else "Clave valida!") if len(cadena) < 10 else "Ingresaste más de 10 caracteres.")