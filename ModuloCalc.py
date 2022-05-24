import time
from random import randint

def soma(entrada1, entrada2):
	startSoma = time.time()
	entrada1 = [int(a) for a in str(entrada1)]
	entrada2 = [int(a) for a in str(entrada2)]
	aux = []
	adicional = 0
	while(entrada1 != [] and entrada2 != []):
		aux.append(entrada1[-1] + entrada2[-1] + adicional)
		entrada1.pop()
		entrada2.pop()
		if(len(entrada1) == 0):
			pass
		elif(aux[-1] > 9):
			aux[-1] = aux[-1] - 10 
			adicional = 1
		else: 
			adicional = 0
	for i in reversed(aux):
		aux.append(str(i))
	for i in aux:
		aux.pop(0)
	aux = "".join(aux)
	print("\n\nO resultado da soma é: "+ str(aux) + "\n\n")
	endSoma = time.time()
	tempoSoma = endSoma - startSoma
	print("O tempo de execução dessa soma foi de : "+ str(tempoSoma)+ " segundos\n")




def multiplicacao(entrada1, entrada2):
	startMultiplicacao = time.time()
	soma = 0
	while(entrada1 >= 1):
		if(entrada1%2 != 0):
			entrada1 = entrada1 - 1
			soma = soma + entrada2
    #ajusteeeeee
		entrada1 = (entrada1/2)
		entrada2 = int(entrada2*2)
	print("\n\nO resultado da multiplicação é: "+ str(soma) + "\n\n")
	endMultiplicacao = time.time()
	tempoMultiplicacao = endMultiplicacao - startMultiplicacao
	print("O tempo de execução dessa multiplicação foi de: "+ str(tempoMultiplicacao) + " segundos\n")

def menu():
	valor = int(input("Escolha uma opção abaixo: \n\n1 -> Soma \n2 -> Multiplicação\n3 -> Sair\n\n"))
	entrada = int(input("\n1 -> Escolher um número manualmente\n2 -> Escolher um número aleatório de tamanho 'n' escolhido por você\n"))
	if(valor == 1 and entrada == 1):
		entrada1 = int(input("digite o valor do primeiro número: "))
		entrada2 = int(input("digite o valor do segundo número: "))
		soma(entrada1, entrada2)
		menu()
	elif(valor == 1 and entrada == 2):
		entrada = int(input("\nQuantos dígitos o numero deve possuir? ")) 
		entrada1 = randint(10**(entrada-1), (10**entrada)-1)
		entrada2 = randint(10**(entrada-1), (10**entrada)-1)
		print("soma entre " + str(entrada1) + " e " + str(entrada2) + "\n")
		soma(entrada1, entrada2)
		menu()
	elif(valor == 2 and entrada == 1):
		entrada1 = int(input("digite o valor do primeiro número: "))
		entrada2 = int(input("digite o valor do segundo número: "))
		multiplicacao(entrada1, entrada2)
		menu()
	elif(valor == 2 and entrada == 2):
		entrada = int(input("\nQuantos dígitos o numero deve possuir? ")) 
		entrada1 = randint(10**(entrada-1), (10**entrada)-1)
		entrada2 = randint(10**(entrada-1), (10**entrada)-1)
		print("multiplicação entre " + str(entrada1) + " e " + str(entrada2) + "\n")
		multiplicacao(entrada1, entrada2)
		menu()
	elif(valor == 3):
		pass
	else:
		print("\nValor inválido, tente de novo\n")
		menu()

