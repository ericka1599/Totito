tab1 = ["A" , "B" , "C"]
tab2 = ["D" , "E" , "F"]
tab3 = ["G" , "H" , "I"]

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

	print (tab1)
	print (tab2)
	print (tab3)

	mov = input(jug + " donde deseas marcar? ")
	if mov == "A":
		tab1[0] = mar
	elif mov == "B":
		tab1[1] = mar
	elif mov == "C":
		tab1[2] == mar
	if mov == "D":
		tab2[0] = mar
	elif mov == "E":
		tab2[1] = mar
	elif mov == "F":
		tab2[2] == mar
	if mov == "G":
		tab3[0] = mar
	elif mov == "H":
		tab3[1] = mar
	elif mov == "I":
		tab3[2] == mar
	turn = turn + 1
	 

	if tab1[0] and tab1[1] and tab1[2] == "X" or tab2[0] and tab2[1] and tab2[2] == "X" or tab3[0] and tab3[1] and tab3[2] == "X" or tab1[0] and tab2[0] and tab3[0] == "X" or tab1[1] and tab2[1] and tab3[1] == "X" or tab1[2] and tab2[2] and tab3[2] == "X" or tab1[0] and tab2[1] and tab3[2] == "X" or tab1[2] and tab2[1] and tab3[0] == "X" :
		gan = True
		print ("Ganador: " + jug1 )
	elif tab1[0] and tab1[1] and tab1[2] == "O" or tab2[0] and tab2[1] and tab2[2] == "O" or tab3[0] and tab3[1] and tab3[2] == "O" or tab1[0] and tab2[0] and tab3[0] == "O" or tab1[1] and tab2[1] and tab3[1] == "O" or tab1[2] and tab2[2] and tab3[2] == "O" or tab1[0] and tab2[1] and tab3[2] == "O" or tab1[2] and tab2[1] and tab3[0] == "O" :
		gan = True
		print ("Ganador: " + jug2 )

	else :

		print ("Turno #" + turn )

	if turn == 10:
		gan = True
		print ("Nadie gana")