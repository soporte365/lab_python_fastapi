from django.db.models.expressions import result


def saludar(nombre):
    print("Hola", nombre)
saludar("Carlos")

def media (num1, num2, num3):
    resultado = num1 + num2 + num3
    resultado = resultado/3
    # OTRA MANERA DE CALCUALR LA VARIABLE EN UNA SOLA LINEA ES:
    # return  (num1 + num2 + num3)/3
    return resultado
varis = media(5, 6, 7)
print("la media de los 3 valores son:", varis)

# FORMAS EN LAS QUE USAR LOS ARGUMENTOS EN UAN FUNCION

def resta(num01 = 3, num02 = 2):
    return num01 - num02

print(f"""
Con valores por defecto: {resta()}.
Con el orden de un solo valor: {resta(5)}.
Usando el orden con otros valores: {resta(6,2)}.
Usando Keydword arguments: {resta(num02=3, num01=5)}.
Con un solo keyword argument: {resta(num02=5)}.
""")

Variable = 3
def funcion():
    global Variable
    Variable = 0
    print(Variable)
funcion()
print(Variable) #toma el ultimo valor agregado