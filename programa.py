import os
import time
import math
lista = []
paginaActiva = 0

def agregarTarea(nom):
	lista.append({
		"nom":nom,
		"completado": False
	})

def menu(pagina):
	print(" [1] Pagina anterior [2] Siguiente pagina")
	print(" [3] Nueva tarea	[4] Seleccionar Tarea")
	# Mostrar en que pagina esta
	print(f"\tPagina: [{pagina+1} de {int(math.ceil(len(lista)/5))}]\n")

	if len(lista) - (5*pagina) <= 0:
		print("\n\tEsta pagina esta vacia" + ("\n"*2))
	
	try:
		for i in range(5):
			item = lista[i + (5 * pagina)]
			if item["completado"] == True:
				print("\t[" +str(i + (5 * pagina))+ "] "+ str(item["nom"]) + " | COMPLETADO")
			else:
				print("\t[" +str(i + (5 * pagina))+ "] "+ str(item["nom"]))
	except:
		pass

while True:
	os.system('cls') # Limpiar pantalla
	menu(paginaActiva)
	print()
	opcion = input('=> ')

	match str(opcion):
		case '1': # Ir a la pagina anterior
			if paginaActiva > 0:
				paginaActiva -= 1
		case '2': # Ir a la pagina siguiente
			if (paginaActiva+1) < len(lista)/5:
				paginaActiva = paginaActiva + 1
		case '3': # Crear una nueva tarea
			while True:
				os.system('cls') # Limpiar pantalla
				print("Inserte el nombre de la tarea:")
				nomtarea = input("=> ")
				if not nomtarea.isspace():
					agregarTarea(nomtarea)
					break;
		case '4':
			looping = True
			while looping:
				print("-"*20)
				print("[X] para salir.")
				print("Inserta el indice de la tarea que quieras seleccionar")
				tarea = input("=> ")
				if str(tarea).lower() == 'x':
					break
				
				try:
					if tarea.isnumeric():
						item = lista[int(tarea)]
						while True:
							estado = "M"
							if item["completado"] == True:
								estado = "Desm"
							
							os.system('cls')
							print(f"Has seleccionado la tarea {tarea}")
							print(f"[{tarea}]", item["nom"])
							print("\n [1] Eliminar Tarea [2] "+estado+"arcar como completado")
							print(" [3] Deseleccionar")
							tareaopc = input('=> ')
							match str(tareaopc):
								case '1':
									lista.pop(int(tarea))
									looping = False
									break;
								case '2':
									item["completado"] = not item["completado"]

									estado = "m"
									if item["completado"] == False:
										estado = "desm"
									
									os.system('cls')
									print(f"[{tarea}]"+ item["nom"] +" "+ estado + "arcado como completado")
									time.sleep(0.4)
									looping = False
									break;
								case _:
									looping = False
									break;
				except:
					print("Tarea no existente o valida")
					break;
		case _:
			print("Opcion no valida")
			time.sleep(0.5)