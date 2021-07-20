class Persona:

    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def mostrar_persona(self):
        print('Hola {} tu edad es {} y tu genero {}'
              .format(self.nombre, self.edad, self.genero))

persona = Persona('Sago', 19, 'Masculino')

persona.mostrar_persona()

