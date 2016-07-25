import funciones
des = 1
while des == 1:

	tab = [["A " , "B " , "C"], 
	["D " , "E " , "F"], 
	["G " , "H " , "I"]]

	jug1 = input("Ingrese el nombre del primer jugador: ")
	jug2 = input("Ingrese el nombre del segundo jugador: ")

	print (funciones.tablero(tab))
	
	print (jug1)

	mov = input("Donde deseas marcar? ")
	print(funciones.jug1(tab))
	print(funciones.ganador(tab))

	cont = 4
	while cont > 0:


		if funciones.ganador(tab) != jug2 :
						print(jug1)
						mov = input("Donde vas a marcar? ")
						print(funciones.jug1(tab))
						print(funciones.ganador(tab))
					
		cont = cont - 1 		
		
			print("Si desea jugar de nuevo presione 1.")
			print("Si desea salir presione 2.")
			des = int(input("Presiona: "))		

		elif des == 2:
			print("Gracias por jugar!")		

		else:
			print("No se vale.")
			print("Si desea jugar de nuevo presione 1.")
			print("Si desea salir presione 2.")
			des = int(input("Presiona: "))