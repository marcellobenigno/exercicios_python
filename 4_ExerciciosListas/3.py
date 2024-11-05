# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notes = []

for i in range(4):
	input_ = float(input(f'Digite a {i + 1}º nota: '))
	notes.append(input_)

note_avg = sum(notes) / len(notes)

print(f'A média das notas é: {note_avg:.2f}')