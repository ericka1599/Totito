tab = [[A, B, C]
[D, E, F]
[G, H, I]]

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

	print (tab)
	mov = input(jug + "Donde deseas marcar? ")
	if mov == A:
		tab[0,0] = mar
	elif mov == B:
		tab[0,1] = mar
	elif mov == C:
		tab[0,2] == mar
	if mov == D:
		tab[1,0] = mar
	elif mov == E:
		tab[1,1] = mar
	elif mov == F:
		tab[1,2] == mar
	if mov == G:
		tab[2,0] = mar
	elif mov == H:
		tab[2,1] = mar
	elif mov == I:
		tab[2,2] == mar
	turn = turn + 1
	 

	if tab[0,0] and tab[0,1] and tab[0,2] == "X" or tab[1,0] and tab[1,1] and tab[1,2] == "X" or tab[2,0] and tab[2,1] and tab[2,2] == "X" or tab[0,0] and tab[1,0] and tab[2,0] == "X" or tab[0,1] and tab[1,1] and tab[2,1] == "X" or tab[0,2] and tab[1,2] and tab[2,2] == "X" or tab[0,0] and tab[1,1] and tab[2,2] == "X" or tab[0,2] and tab[1,1] and tab[2,0] == "X" :
		gan = True
		print ("Ganador: " + jug1 )
	elif tab[0,0] and tab[0,1] and tab[0,2] == "O" or tab[1,0] and tab[1,1] and tab[1,2] == "O" or tab[2,0] and tab[2,1] and tab[2,2] == "O" or tab[0,0] and tab[1,0] and tab[2,0] == "O" or tab[0,1] and tab[1,1] and tab[2,1] == "O" or tab[0,2] and tab[1,2] and tab[2,2] == "O" or tab[0,0] and tab[1,1] and tab[2,2] == "O" or tab[0,2] and tab[1,1] and tab[2,0] == "O" :
		gan = True
		print ("Ganador: " + jug2 )

	else :

		print ("Turno #" + turn )

	if turn == 9:
		gan = True
		print ("Nadie gana")