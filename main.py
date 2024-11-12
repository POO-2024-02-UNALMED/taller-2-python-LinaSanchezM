class Asiento:
    def __init__ (self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
        
    def cambiarColor(self, color):
        colorespermitidos = ["rojo", "verde", "azul", "amarillo", "negro", "blanco"]
        if color in colorespermitidos:
            self.color = color

class Motor:
    def __init__ (self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
            if tipo == "electrico" or tipo == "gasolina":
                self.tipo = tipo
                

class Auto:
    cantidadCreados = 0

    def __init__ (self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        cantidadAsientos=0
        for i in self.asientos:
            if i:
                cantidadAsientos+=1
        return cantidadAsientos


    def verificarIntegridad(self):
        registroAuto= self.registro
        for i in self.asientos:
            if i and i.registro != registroAuto:
                return "Las piezas no son originales"
        if self.motor.registro != registroAuto:
            return "Las piezas no son originales"
        return "Auto original"

