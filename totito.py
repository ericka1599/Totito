tab = [["A " , "B " , "C"],
["D " , "E " , "F"],
["G " , "H " , "I"]]

cont = 0
turn = 1
turns = str(turn)

jug1 = input("Ingresa el nombre del jugador 1: ")
jug2 = input("Ingresa el nombre del jugador 2: ")


gan = False


while gan == False:

	if cont == 0:
		jug = jug1
		resultado = 1
		cont = cont + 1
	else :
		jug = jug2
		resultado = -1
		cont = cont - 1

	print ("Turno #" + turns)
	turn = turn + 1

	print (tab[0])
	print (tab[1])
	print (tab[2])


	mov = input(jug + " donde deseas marcar? ")
	movi = ord(mov)

	mov_valor = movi - 65
	mov_fila = mov_valor % 3
	mov_columna = mov_valor // 3

	tabs = tab [ mov_fila ] [ mov_columna ]
	print (tabs)

	celda = tabs

	for i in range (3):
		for j in range(3):
			if celda == 1:
				resultado = "X"
			elif celda == -1:
				resultado = "O"
			else:
				resultado = chr(3*i + j + 65)


	tabs = resultado

	print (tab[0])
	print (tab[1])
	print (tab[2])


	sumas = []
	for i in range(3):
		sumas.append (tab[i][0] + tab[i][1] + tab[i][2])

	for i in range(3):
		sumas.append (tab[0][i] + tab[1][i] + tab[2][i])

	sumd1 = 0
	sumd2 = 0
	for i in range (3):
		sumd1 += tabs[i][i]
		sumd2 += tabs[i][2-i]
		sumas.append (sumd1)
		sumas.append (sumd2)

	if 3 in sumas:
		gan = True
		print ("¡El jugador " + jug1 + " ha ganado!" )
	elif -3 in sumas:
		gan = True
		print ("¡El jugador " + jug2 + " ha ganado!" )
	

	if turn == 10:
		gan = True
		print ("Nadie gana")