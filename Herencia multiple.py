class persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

        def hablar(self):
            print(f"Hola, mi nombre es {self.nombre} y estoy hablando")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f"Mi habilidad es {self.habilidad}")    #Metodo Habilidad de la clase Artista

class PersonaArtista(persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)           #Hereda tambien los metodos de la clase Artista
        self.salario = salario
        self.empresa = empresa

    def mostrar_informacion(self):
        return self.mostrar_habilidad()            #Llama al metodo mostrar_habilidad de la clase Artista, demostrando la herencia multiple y el orden de resolucion de metodos (MRO)


persona1 = PersonaArtista("Juan", 30, "Mexicano", "Pintura", 50000, "Galería de Arte")
persona1.mostrar_informacion() 
