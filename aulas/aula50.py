'''
Imprecisão de ponto flutuante

'''

numero1 = 0.1
numero2 = 0.7
numero3 = numero1 + numero2
print(numero3)

# dessa forma, o numero que representa a soma dos valores virá com casas decimais quebradas
# para contornar isso, usa-se a formatação, por exemplo:

print(f'{numero3:.2f}')

# uma maneira mais elegante de fazer esse ajuste é por meio da função round

# print(round(numero, numero de casas desajadas)

print(round(numero3, 2))