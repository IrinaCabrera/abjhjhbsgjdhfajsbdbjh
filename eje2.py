def funcion(n):
	cont = 1
	suma = 0
	while cont <= n:
		suma = suma + cont
		cont = cont + 1
	print("La suma total es:", suma)

n = int(input("Ingrese un numero natural:"))
funcion (n)