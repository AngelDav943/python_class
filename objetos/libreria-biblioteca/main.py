import os
import time
from usuario import persona
import funcs as biblioteca

if __name__ == "__main__":
    while True:
        os.system('cls') # Limpiar pantalla
        print("-- Biblioteca --")
        print("\t [1] Agregar")
        print("\t [2] Eliminar usuario")
        print("\t [3] Eliminar libro")
        print("\t [4] Buscar usuario")
        print("\t [5] Visualizar todos los usuarios")
        print("\t [X] SALIR DEL PROGRAMA")

        opcion = input("=> ")
        match str(opcion).lower():
            case "1": # Agregar
                os.system("cls") # Limpiar consola
                print(" -- Agregar --")
                print("\t - Nombre del usuario:")
                usuario = input("\t=> ")
                print("\t - Nombre del libro:")
                libro = input("\t=> ")

                persona = biblioteca.agregar(usuario, libro)
                if persona:
                    print(persona)
                else:
                    print("Error agregando.")
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
                
            case "3": # Eliminar libro
                os.system("cls") # Limpiar consola
                print(" -- Eliminar libro --")
                print("\t - Nombre del usuario:")
                usuario = input("\t=> ")
                print("\t - Nombre del libro:")
                libro = input("\t=> ")
                
                eliminado = biblioteca.eliminarlibro(usuario, libro)

                if eliminado:
                    print(libro, "fue eliminado de", usuario, ".")
                else:
                    print("El usuario o libro no existe.")
                
                time.sleep(0.4)

            case "4": # Buscar usuario
                os.system("cls") # Limpiar consola
                print(" -- Buscar usuario --")
                print("\t - Nombre del usuario:")
                nombre = input("\t=> ")
                usuario : persona = biblioteca.buscar(nombre)
                
                if usuario:
                    print("Nombre:", str(usuario.nombre).title())
                    print("Libros:")
                    print("\t", usuario.libros)
                else:
                    print("El usuario no existe.")
                
                input("Presiona enter para continuar... ")

            case "5": # Visualizar todos los usuarios
                os.system("cls") # Limpiar consola
                datos = biblioteca.visualizar()
                print("Usuarios: ", len(datos))
                for nombre in datos:
                    usuario: persona = biblioteca.buscar(str(nombre))
                    print("\t" + str(usuario).title() + ":")
                    print("\t",usuario.libros)
                input("... ")

            case "x":
                print("Saliendo del programa...")
                time.sleep(0.5)
                break

            case _:
                print("Opcion no valida, intenta de nuevo.")
                time.sleep(0.4)