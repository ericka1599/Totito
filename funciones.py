def tablero(tab):
	resultado = ""
	for i in tab:
		for j in i:
			resultado += j + " "
		resultado += '\n'
	return resultado 

def jug1(mov,tab):
		mov_val = ord(mov) - 65
		tab[mov_val // 3][mov_val % 3] = "X"
		return tablero(tab)

def jug2(mov,tab):
		mov_val = ord(mov) - 65
		tab[mov_val // 3][mov_val % 3] = "O"
		return tablero(tab)

def ganador(tab):
	lista2= []
	suma= []
	for i in tab:
		suma_fila= []
		for j in i:
			if j == "X":
				suma_fila.append(1)
			elif j == "O":
				suma_fila.append(-1)	
			else:
				suma_fila.append(0)	
		suma.append(suma_fila)				

	suma_d1= 0
	suma_d2 = 0			
	
	for i in suma:
		lista2.append(sum(i))
	for i in range (3):
		lista2.append(suma[0][i] + suma[1][i] + suma[2][i])
	for i in range (3):
		suma_d1+= suma[i][i]
		suma_d2+= suma[i][2 - i] 
		lista2.append(suma_d1)
		lista2.append(suma_d2)

	if 3 in lista2:
		print ("Ganaste!")
	elif -3 in lista2:
		print ("Ganaste!")
	else:
		return " "	