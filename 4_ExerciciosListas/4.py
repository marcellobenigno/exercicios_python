# Faça um Programa que leia um vetor de 10 caracteres, 
# e diga quantas consoantes foram lidas. Imprima as consoantes.

chars = []
vogals = ['a', 'e', 'i', 'o', 'u']

for i in range(10):
	char = input(f'Digite o {i+1}º caractere: ').lower()
	if char not in vogals and char.isalpha() and char not in chars:
		chars.append(char)

chars.sort()

print(f'As consoantes são: {", ".join(chars)}')

