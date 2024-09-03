"""
Programación funcional en Python

Ejercicio en clase
"""

"""
Requisitos:
- Solicitar al usuario 4 números por consola
- Crear una función que devuelva cuál es el mayor número de los 4 ingresado por el usuario
- Finalmente elevar al cubo este resultado
"""

var1 = int(input("Ingrese el primer valor: "))
var2 = int(input("Ingrese el segundo valor: "))
var3 = int(input("Ingrese el tercero valor: "))
var4 = int(input("Ingrese el cuarto valor: "))

def mayor():
    if var1 > var2 and var1 > var3 and var1 > var4:
        return print(f"El numero mayor es: {str(var1)}."
                     f"\n Elavación al Cubo: {str(var1**3)}")
    elif var2 > var3 and var2 > var4 and var2 > var1:
        return print(f"El numero mayor es: {str(var2)}."
                     f"\n Elavación al Cubo: {str(var2 ** 3)}")
    elif var3 > var2 and var3 > var1 and var3 > var4:
        return print(f"El numero mayor es: {str(var3)}."
                     f"\n Elavación al Cubo: {str(var3 ** 3)}")
    elif var4 > var2 and var4 > var1 and var4 > var3:
        return (print(f"El numero mayor es: {str(var4)}."),
                print(f"Elevación al Cubo: {str(var4 ** 3)}"))
            #print(f"El numero mayor es: {str(var4)}."
             #        f"\n Elavación al Cubo: {str(var4 ** 3)}"))
    else:
        return print("Ninguno es Mayor")
mayor()