# UNA PEQUEÑA CALCULADORA
"""
# DECLARAMOS LAS VARIABLES COMO INPUT
n1 = input("INGRESE VALOR DE N1: ")
n2 = input("INGRESE VALOR DE N2: ")

# SE TRASNFORMAN LAS VARIABLES EN INTEGER YA QUE INPUT TRABAJA CON STRING
n1 = int(n1)
n2 = int(n2)

SUM = n1 + n2
REST = n1 - n2
MULTI = n1 * n2
Div = n1 / n2

# mensaje = f"""
from django.utils.dateparse import postgres_interval_re

# Para los numeros {n1} y {n2}.
# El resultado de la suma es: {SUM}.
# El resultado de la resta es: {REST}.
# El resultado de la multiplicacion  es: {MULTI}.
# El resultado de la división es : {Div}.
"""
print(mensaje)


# CONVERSION Y TIPOS DE DATOS
# x = input("") #INPUT SIEMPRE DEVULVE UN STRING
# int()
# float()
# str () # string
# bool()

print(bool("")) # retorna false
print(bool("0")) # retorna True
print(bool(None)) # retorna false
print(bool("0")) # retorna True
print(bool(0)) # retorna false

"""
# COMPARADORES LOGICOS, DEVUELVEN TRUE O FALSE SEGUN LA COMPARACION

# < MAYOR QUE
# > MENOR QUE
# >= MAYOR O IGUAL QUE
# <= MENOR O IGUAL QUE
# == IGUAL QUE
# != DIFERENTE DE

# USO DEL IF, ELIF Y ELSE

edad = 15

if edad > 65:
    print("Puedes ver la pelicula con un super descuento")
elif edad >54:
    print("Puedes ver la pelicula con un descuento")
elif edad > 17:
    print("Puedes ver la pelicula")
else:
    print("No puedes ver la pelicula")
print("LISTO")
