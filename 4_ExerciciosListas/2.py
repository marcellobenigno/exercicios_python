# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numbers = []

for i in range(10):
	n = int(input(f'Digite o {i + 1}º número: '))
	numbers.append(n)

print(sorted(numbers, reverse=True))