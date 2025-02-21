'''

Exercício Calculadora

'''

while True:

    num_1 = input('Digite o primeiro número: ')
    num_1_int = int(num_1)

    num_2 = input('Digite o segundo número: ')
    num_2_int = int(num_2)

    operador = input('Escolha um operador aritmético [+, -, *, /]: ')

    if operador == '+':
        res = num_1_int + num_2_int
        print (res) 
    
    elif operador == '-':
        res = num_1_int + num_2_int
        print (res)

    elif operador == '*':
        res = num_1_int * num_2_int
        print (res)

    elif operador == '/':
        res = num_1_int / num_2_int
        print (res)

    else:
        print('Você não seguiu as instruções.')
        sair = input('Deseja sair? [s]im: ' ).lower().startswith('s')
        if sair == True:
            break