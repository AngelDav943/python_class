class Cuenta():
    def __init__(self, titular) -> None:
        self.titular = titular
        self.cantidad = 0
    
    def mostrar(self):
        print("Datos:")
        print("\tTitular:  ", self.titular)
        print("\tCantidad: ", self.cantidad)
    
    def ingresar(self, cantidad) -> bool:
        if cantidad > 0:
            self.cantidad = self.cantidad + cantidad
            return True
        return False
    
    def retirar(self, cantidad):
        self.cantidad = self.cantidad + abs(cantidad)

import os
juan = Cuenta("Juan")
while True:
    os.system("cls")
    opcion = input("1. Mostrar datos \n2.Ingresar cantidad \n3.Retirar cantidad \n => ")
    match str(opcion).lower():
        case "1": # Mostrar
            juan.mostrar()
            input("Presiona enter para continuar..")
        case "2": # Ingresar
            cantid = input("Ingresar cantidad a ingresar. \n => ")
            if cantid.isnumeric():
                resp = juan.ingresar(float(cantid))     
        case "3": # Retirar
            cantid = input("Ingresar cantidad a retirar. \n => ")
            if cantid.isnumeric():
                resp = juan.ingresar(float(cantid))