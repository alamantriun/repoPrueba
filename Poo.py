class Person:
    def __init__(self, nombre, apellido, edad, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nacionalidad = nacionalidad


class Worker(Person):
    def __init__(self, nombre, apellido, edad, nacionalidad, empresa):
        super().__init__(nombre, apellido, edad, nacionalidad)
        self.empresa = empresa

    def trabajar(self):
        print(f"{self.nombre} esta trabajando en {self.empresa}")



roberto = Worker("Roberto", "Gomez", 30, "Mexicano", "Google")
print(f"{roberto.nombre} {roberto.apellido} tiene {roberto.edad} años y es {roberto.nacionalidad}")
roberto.trabajar()

martha = Worker("Martha", "Sanchez", 25, "Mexicana", "Microsoft")
print(f"{martha.nombre} {martha.apellido} tiene {martha.edad} años y es {martha.nacionalidad}")
martha.trabajar()


william = Person("William", "Smith", 40, "Americano")
print(f"{william.nombre} {william.apellido} tiene {william.edad} años y es {william.nacionalidad}")


