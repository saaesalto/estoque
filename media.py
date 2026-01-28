# receber notas inteiras, calcular media e devolver situação

nota_01 = int(input('nota 1° bimestre: '))
nota_02 = int(input('nota 2° bimestre: '))
nota_03 = int(input('nota 3° bimestre: '))
nota_04 = int(input('nota 4° bimestre: '))

media = (nota_01 + nota_02 + nota_03 + nota_04) / 4

if media >= 6:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

print(f'A média é {media}') 
print(f'Aluno {situacao}')