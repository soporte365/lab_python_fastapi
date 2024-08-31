"""VARIABLES Y TIPOS DE VARIABLES"""


"""LAS VARIABLES SON SENSIBLES EN CUANTO AL USO DE MAYUSCULAS Y MINUSCULA"""
nombre_curso ="Esto es una variable"
NOMBRE_CURSO="Esto es otra variable aunque tenga el mismo nombre"
print(nombre_curso, NOMBRE_CURSO)

"""TIPOS DE VARIABLES"""

nombre="Esta es tipo string"
"""Esto es una variable de tipo intenger"""
num1= 500
"""Esto es una variable de tipo float"""
numf = 9.8
"""Esto es una variable de tipo Boolean True o False, con la primera letra mayuscula"""
Bolen = True

print("Aqui muestro los tipo de Variables")
print("Integer: ", num1, " Float:",numf, " Boolean:",Bolen )

"""STRING Y SUS USOS"""
NomCurso ="Python FastAPI"
DescriCur = """en este curso aprenderas a crear un API con Python"""
print("Curos ",NomCurso,":", DescriCur)

"""MANERAS DE OPTENER INFORMACION DE LOS STRING"""
print("La cantidad de caracteres que tiene la variable NomCurso es de: ",len(NomCurso))
print("Obteniendo el segundo caracter de la variable NomCruso se recuerda que el primer caracter esta en la psoción 0 ", NomCurso[1])

"""RECORTANDO UN STRING"""
"""El suo de [:] es para indicar desde que indice comenzar o desde que posición del carater comenxar y terminar en tomar para recortar un string"""
print(NomCurso[0:6])
print(NomCurso[7:])
print(NomCurso[:6])
print(NomCurso[:])

"""FORMATEANDO EL CODIGO"""
"""Usando el metodo f y {} dentro de las comillas, podemos agregar las variables y datos que queramos"""
Nombre = "Carlos"
Apellido = "Torres"
NomCompl = f"{Nombre} {Apellido} {"Edad:"} {30+7}"
print(NomCompl)
