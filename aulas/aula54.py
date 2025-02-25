"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf = ('604751673')

digitos_cpf = [int(d) for d in cpf[:9]]
print(digitos_cpf)

# declarando o indice e as listas
contagem_regressiva = [10,  9,  8,  7,  6,  5,  4,  3,  2]

# agrupando todas as multiplicações
lista_final = [a * b for a, b in zip(contagem_regressiva, digitos_cpf)]
digitos_cpf = [int(d) for d in cpf[:10]]

print(lista_final)

# coletando a soma
soma = sum(lista_final)
print(soma)

# Multiplicar o resultado anterior por 10

multiplicar = soma * 10
print(multiplicar)

# Obter o resto da divisão da conta anterior por 11

divisao = multiplicar % 11
print(divisao)

# condicionais

resultado = 0 if divisao > 9 else divisao
print(f'O primeiro dígito do CPF é {resultado}')
primeiro_digito = resultado

###################### SEGUNDO DÍGITO #########################

cpf_segundo_digito = cpf + str(primeiro_digito)

digitos_cpf_segundo = [int(d) for d in cpf_segundo_digito[:10]]
print(digitos_cpf_segundo)

# declarando o indice e as listas
contagem_regressiva = [11, 10,  9,  8,  7,  6,  5,  4,  3,  2]

# agrupando todas as multiplicações
lista_final_segundo = [a * b for a, b in zip(contagem_regressiva, digitos_cpf_segundo)]
digitos_cpf_segundo = [int(d) for d in cpf[:10]]

print(lista_final_segundo)

# coletando a soma
soma_segundo = sum(lista_final_segundo)
print(soma_segundo)

# Multiplicar o resultado anterior por 10

multiplicar_segundo = soma_segundo * 10
print(multiplicar_segundo)

# Obter o resto da divisão da conta anterior por 11

divisao_segundo = multiplicar_segundo % 11
print(divisao_segundo)

# condicionais

resultado_segundo = 0 if divisao_segundo > 9 else divisao_segundo
print(f'O segundo dígito do CPF é {resultado_segundo}')
segundo_digito = resultado_segundo