"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
cpf = ('604751673')

digitos_cpf = [int(d) for d in cpf[:9]]
print(digitos_cpf)

# declarando o indice e as listas
contagem_regressiva = [10,  9,  8,  7,  6,  5,  4,  3,  2]

# agrupando todas as multiplicações
lista_final = [a * b for a, b in zip(contagem_regressiva, digitos_cpf)]
digitos_cpf = [int(d) for d in cpf[:9]]

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