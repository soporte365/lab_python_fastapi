"""VARIABLES Y TIPOS DE VARIABLES"""


# LAS VARIABLES SON SENSIBLES EN CUANTO AL USO DE MAYUSCULAS Y MINUSCULA
nombre_curso ="Esto es una variable"
NOMBRE_CURSO="Esto es otra variable aunque tenga el mismo nombre"
print(nombre_curso, NOMBRE_CURSO)

# TIPOS DE VARIABLES

nombre="Esta es tipo string"
"""Esto es una variable de tipo intenger"""
num1= 500
"""Esto es una variable de tipo float"""
numf = 9.8
"""Esto es una variable de tipo Boolean True o False, con la primera letra mayuscula"""
Bolen = True

print("Aqui muestro los tipo de Variables")
print("Integer: ", num1, " Float:",numf, " Boolean:",Bolen )

# STRING Y SUS USOS
NomCurso ="Python FastAPI"
DescriCur = """en este curso aprenderas a crear un API con Python"""
print("Curos ",NomCurso,":", DescriCur)

# MANERAS DE OPTENER INFORMACION DE LOS STRING
print("La cantidad de caracteres que tiene la variable NomCurso es de: ",len(NomCurso))
print("Obteniendo el segundo caracter de la variable NomCruso se recuerda que el primer caracter esta en la psoción 0 ", NomCurso[1])

# RECORTANDO UN STRING
"""El suo de [:] es para indicar desde que indice comenzar o desde que posición del carater comenxar y terminar en tomar para recortar un string"""
print(NomCurso[0:6])
print(NomCurso[7:])
print(NomCurso[:6])
print(NomCurso[:])

# FORMATEANDO EL CODIGO
"""Usando el metodo f y {} dentro de las comillas, podemos agregar las variables y datos que queramos"""
Nombre = "Carlos"
Apellido = "Torres"
NomCompl = f"{Nombre} {Apellido} {"Edad:"} {30+7}"
print(NomCompl)

# METODOS PARA USO DE STRING
# Metodos para dar estilos a string
animal = "Perrito bebe"
animal2 = " perrito viste  "
print(animal.upper())
print(animal.lower())
print(animal.capitalize())
print(animal.title())
print(animal2.strip().capitalize())
print(animal2.lstrip())
print(animal2.rstrip())
print(animal.find("rr"))
print(animal.replace("rr", "l"))
print("rr" in animal)
print("rr" not in animal)


# SECUENCIAS DE ESCAPE PARA MOSTRAR CARACTERES COMO PARTE DEL STRING
# \"
# \'
# \\
# \n

nombrecur = "Python y \nFastAPI\""
print(nombrecur)

# TRABAJANDO CON NUMEROS
imaginario = 2 + 2j

numer = 2
numer += 2 # es igual a numer = numer +2
print("numero ", numer)
print(3 + 5)
print(1 - 3)
print(2 * 3)
print(2 / 3)
print(1 // 3)
print(8  % 3)
print(2 ** 3)

# FUNCIONES DE MATEMATICA
import math
print(round(1.5))
print(round(1.2))
print(abs(-55))

print(math.ceil(1.1))
print(math.floor(1.999))
print(math.isnan(22))
print(math.pow(10, 2))
print("La raiz cuadrada de 9 es: ", math.sqrt(9))
