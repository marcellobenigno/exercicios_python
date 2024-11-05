# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números 
# IMPARES no vetor impar. Imprima os três vetores.

numeros = []
pares = []
impares = []

for i in range(10):
    num = int(input(f'Digite o {i+1}º número: ').strip())
    numeros.append(num)
    
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

pares_unicos = sorted(set(pares))
impares_unicos = sorted(set(impares))

print(f'Todos os números: {numeros}')
print(f'Números pares: {" ".join(map(str, pares_unicos))}')
print(f'Números ímpares: {" ".join(map(str, impares_unicos))}')