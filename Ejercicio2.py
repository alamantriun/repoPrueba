class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado=grado
    
    def __str__(self):
        return f"{super().__str__()}, Grado: {self.grado}"

persona1=Persona("Juan",30)
estudiante =Estudiante("Maria",20,"10° grado")


print(persona1)
print(estudiante)
