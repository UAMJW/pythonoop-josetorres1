class Persona(object):
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar_edad(self):
        print self.edad
    def modificar_edad(self, edad):
        if edad < 0 or edad>150:
            return false
        else:
            self.edad = edad
    
