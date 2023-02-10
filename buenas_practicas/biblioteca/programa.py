import os
import time
import funciones as biblioteca

if __name__ == "__main__":
    while True:
        os.system('cls') # Limpiar pantalla
        print("-- Biblioteca --")
        print("\t [1] Agregar usuario")
        print("\t [2] Eliminar usuario")
        print("\t [3] Actualizar usuario")
        print("\t [4] Visualizar usuario (buscar)")
        print("\t [5] Visualizar todos los usuarios")
        print("\t [X] SALIR DEL PROGRAMA")

        opcion = input("=> ")
        match str(opcion).lower():
            case "1": # Agregar usuario
                os.system("cls") # Limpiar consola
                print(" -- Agregar usuario --")
                print("\t - Nombre del usuario:")
                usuario = input("\t=> ")
                print("\t - Nombre del libro:")
                libro = input("\t=> ")

                persona = biblioteca.agregar(usuario, libro)
                if persona:
                    print("Usuario:", usuario)
                    print("Libro:", libro)
                else:
                    print("El usuario ya existe en la lista.")
                time.sleep(0.4)
                
            case "2": # Eliminar usuario
                os.system("cls") # Limpiar consola
                print(" -- Eliminar usuario --")
                print("\t - Nombre del usuario:")
                usuario = input("\t=> ")
                eliminado = biblioteca.eliminar(usuario)

                if eliminado:
                    print(usuario, "fue eliminado.")
                else:
                    print("El usuario no existe.")
                
                time.sleep(0.4)


            case "3": # Actualizar usuario
                os.system("cls") # Limpiar consola
                print(" -- Actualizar usuario --")
                print("\t - Nombre del usuario:")
                usuario = input("\t=> ")
                print("\t - Nombre del libro:")
                libro = input("\t=> ")

                persona = biblioteca.actualizar(usuario, libro)
                if persona:
                    print("El usuario a sido actualizado")
                    print("Usuario:", usuario)
                    print("Libro:", libro)
                else:
                    print("El usuario no existe en la lista.")
                time.sleep(0.4)

            case "4": # Visualizar usuario
                os.system("cls") # Limpiar consola
                print(" -- Eliminar usuario --")
                print("\t - Nombre del usuario:")
                nombre = input("\t=> ")
                libro = biblioteca.buscar(nombre)

                if libro:
                    print("Nombre:", nombre)
                    print("Libro:", libro)
                else:
                    print("El usuario no existe.")
                
                input("Presiona enter para continuar... ")

            case "5":
                os.system("cls") # Limpiar consola
                datos = biblioteca.visualizar()
                print("Usuarios: ", len(datos))
                for nombre, libro in datos.items():
                    print(nombre + ":", libro)
                input("... ")

            case "x":
                print("Saliendo del programa...")
                time.sleep(0.5)
                break

            case _:
                print("Opcion no valida, intenta de nuevo.")
                time.sleep(0.4)