print('Bem-vindo à Calculadora de Média!')

n1 = int(input("Digite a nota 1:"))
n2 = int(input("Digite a nota 2:"))
n3 = int(input("Digite a nota 3:"))

media = float(n1+n2+n3)/3

print(f'A media é: {media}')

if media >= 7:
    print('Aluno aprovado!')
else:
    print('Aluno Reprovado!')