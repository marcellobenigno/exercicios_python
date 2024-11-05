# 1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

numbers = []

for i in range(5):
	n = int(input(f'Digite o {i + 1}º número: '))
	numbers.append(n)

print(numbers)