tab1 = [A, B, C]
tab2 = [D, E, F]
tab3 = [G, H, I]

cont = 0

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

	print (tab1 + \n + tab2 + \n + tab3 )
	mov = input(jug + "Donde deseas marcar? ")
	if mov == A:
		tab1[0] = mar
	elif mov == B:
		tab1[1] = mar
	elif mov == C:
		tab1[2] == mar
	if mov == D:
		tab2[0] = mar
	elif mov == E:
		tab2[1] = mar
	elif mov == F:
		tab2[2] == mar
	if mov == G:
		tab3[0] = mar
	elif mov == H:
		tab3[1] = mar
	elif mov == I:
		tab3[2] == mar
	 

	if tab1[0] and tab1[1] and tab1[2]