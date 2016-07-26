import funciones
des = 1
jugador1 = input("Ingresa el  nombre del jugador 1: ")
jugador2 = input("Ingresa el nombre del jugador 2: ")
while des != 2:

	if des == 1:
		
		tab= [["A","B","C"],
			["D","E","F"],
			["G","H","I"]]
		print(funciones.tablero(tab))
		
		print(jugador1)
		mov = input("Donde marcaras? ")
		print(funciones.jug1(mov.upper(),tab))
		print(funciones.ganador(tab))

		cont = 4
		while cont > 0:

			if funciones.ganador(tab) != jugador1 and funciones.ganador(tab) != jugador2 :
				print("Jugador " + jugador2)
				mov = input("Donde marcaras? ")
				print(funciones.jug2(mov.upper(),tab))
				print(funciones.ganador(tab))
			
				if funciones.ganador(tab) != jugador2 :
					print("Jugador " + jugador1)
					mov = input("Donde marcaras? ")
					print(funciones.jug1(mov.upper(),tab))
					print(funciones.ganador(tab))
				
			cont = cont - 1 		
	
		print("Jugar de nuevo presione 1.")
		print("Salir presione 2.")
		des = int(input("Presiona: "))		

	elif des == 2:
		print("Gracias por jugar!")		

	else:
		print("Opcion invalida.")
		print("Jugar de nuevo presione 1.")
		print("Salir presione 2.")
		des = int(input("Presiona: "))	
