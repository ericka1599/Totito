tab = [["A"  "B"  "C"],
["D"  "E"  "F"],
["G"  "H"  "I"]]

cont = 0
turn = 1
turns = str(turn)

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

	print ("Turno #" + turns)
	turn = turn + 1

	print (tab[0])
	print (tab[1])
	print (tab[2])

	mov = input(jug + " donde deseas marcar? ")

	mov_valor = ord(mov) - 65
	mov_fila = mov_valor % 3
	mov_columna = mov_valor // 3

	tab [mov_fila] [mov_columna] = mar

	if mar == "X" :
		tir = -1
	elif mar == "O":
		tir = 1

	lista2 = []

	

	if turn == 10:
		gan = True
		print ("Nadie gana")