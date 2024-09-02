class perro():
    def __init__(self, nombre, edad):
        #inicializamos los atributos de nombre y edad
        self.nombre = nombre
        self.edad = edad

    def sentarse(self):
        # Simular sentarse
        print(self.nombre.title() + " Se ha sentado.")

    def rodar(self):
        # Simula rodar
        print(self.nombre.title() + " Rodó en el piso.")

# declaramos una variable que tendrá como valor el objeto o clase pedro y le asignamos valores a los argumentos.
mi_perro = perro("pepe", 5)
tu_perro = perro("lolita", 7)

# Imprimimos los valores de la varible perro
print("Mi perro se llama:", mi_perro.nombre.title() + ".")
print("Mi perro tiene:", str(mi_perro.edad) + " años.")

# Llamamos las funciones que exiten dentro de la clase desde la variable, la cual ya cuenta con valores sus argumentos.
mi_perro.sentarse()
mi_perro.rodar()

print("\n")
print("Tu perro se llama:", tu_perro.nombre.title() + ".")
print("Tu perro tiene:", str(tu_perro.edad) + " años.")

tu_perro.sentarse()
tu_perro.rodar()
