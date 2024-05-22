'''1. Crie um programa que receba 2 números do usuário, e que ele possa escolher um das 4 operações matemáticas
para calcular os dois números. O programa deverá exibir na tela o resultado da conta matemática. O programa deverá
dar também ao usuário uma opção para sair do programa caso deseje, e que ele possa fazer quantos cálculos desejar.'''

#Entrada de dados do Usuário
while True:
    n1= str(input('Informe o primeiro número: ')).replace(',','.')
    n2 = str(input('Informe o segundo número: ')).replace(',', '.')

#conversao para os números decimais
    n1 = float(n1)
    n2 = float(n2)

    print('Informe a operação que deseja fazer:\n')
    print('"+" Para somar.')
    print('"-" Para suntrair.')
    print('"*" Para multiplicar.')
    print('"/" Para dividir.')
    print('"%" Para Encontrar o resto da divisão.')

    op = input('Operação desejada: ')

    match op:
        case '+':
            print(f'A soma é: {n1+n2}.')
        case '-':
            print(f'A subtração é: {n1-n2}.')
        case '*':
            print(f'A multiplicação é: {n1*n2}.')
        case '/':
            print(f'A divisão é: {n1/n2}.')
        case '%':
            print(f'O resto da divisão é: {n1%n2}.')
        case _:
            print('Operação inválida')
            continue

