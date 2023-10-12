#programa que verifica a maior idade.

idade_usuario = int(input('Digite sua idade: '))  # trabalhar o input com try/excep pra string

maioridade = 18

#mudar essa pergunta somente se o usuário for menor de 18 anos
maior_responsavel = input('você está acompanhado por uma pessoa com idade acima de 18 anos? (sim/não): ')
if maior_responsavel == 'sim':
    maior_responsavel = True
elif maior_responsavel == 'não':
    maior_responsavel = False

if idade_usuario >= maioridade:
    print('você é maior de idade, pode prosseguir...')
elif (idade_usuario < maioridade) & (maior_responsavel == True):
    print('Você está acompanhado por uma pessoa de maior, pode prosseguir...')
else:
    print('Você não tem idade suficiente para continuar')

