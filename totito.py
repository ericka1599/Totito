tab = [["A" , "B" , "C"]
["D" , "E" , "F"]
["G" , "H" , "I"]]

cont = 0
turn = 1

jug1 = input("Ingresa el nombre del jugador 1: ")
jug2 = input("Ingresa el nombre del jugador 2: ")


gan = False


while gan == False:

	if cont == 0:
		jug = jug1
		mar = "X"
		cont = cont + 1
	else :
		jug = jug2
		mar = "O"
		cont = cont - 1

	print ("Turno #" + turn)
	turn = turn + 1

	print (tab[0])
	print (tab[1])
	print (tab[2])

	mov = input(jug + " donde deseas marcar? ")

	mov_valor = ord(mov) - 65
	tiro_fila = tiro_valor % 3
	tiro_columna = tiro_valor // 3

	tab [tiro_fila] [tiro_columna] = mar

	if tab [0] == 3
		gan = True
		print ("Ganador: " + jug1 )
	
		gan = True
		print ("Ganador: " + jug2 )


	if turn == 10:
		gan = True
		print ("Nadie gana")