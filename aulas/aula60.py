cpf_fornecido = '16485633766'  # CPF fornecido como string

# Pegando os primeiros 9 dígitos e convertendo para inteiros
nove_digitos_cpf = [int(d) for d in cpf_fornecido[:9]]
print(nove_digitos_cpf)

# Pesos para o primeiro dígito
contagem_regressiva = [10, 9, 8, 7, 6, 5, 4, 3, 2]

# Multiplicação dos dígitos pelo peso correspondente
lista_final = [a * b for a, b in zip(nove_digitos_cpf, contagem_regressiva)]
print(lista_final)

# Soma dos valores multiplicados
soma = sum(lista_final)
print(soma)

# Multiplicar soma por 10 e obter o resto da divisão por 11
multiplicar = soma * 10
divisao = multiplicar % 11
print(divisao)

# Definição do primeiro dígito verificador
primeiro_digito = 0 if divisao > 9 else divisao
print(f'O primeiro dígito do CPF é {primeiro_digito}')

# Adicionando o primeiro dígito ao CPF
dez_digitos_cpf = cpf_fornecido[:9] + str(primeiro_digito)

# Pegando os primeiros 10 dígitos e convertendo para inteiros
digitos_cpf_segundo = [int(d) for d in dez_digitos_cpf]
print(digitos_cpf_segundo)

# Pesos para o segundo dígito
contagem_regressiva = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

# Multiplicação dos dígitos pelo peso correspondente
lista_final_segundo = [a * b for a, b in zip(digitos_cpf_segundo, contagem_regressiva)]
print(lista_final_segundo)

# Soma dos valores multiplicados
soma_segundo = sum(lista_final_segundo)
print(soma_segundo)

# Multiplicar soma por 10 e obter o resto da divisão por 11
multiplicar_segundo = soma_segundo * 10
divisao_segundo = multiplicar_segundo % 11
print(divisao_segundo)

# Definição do segundo dígito verificador
segundo_digito = 0 if divisao_segundo > 9 else divisao_segundo
print(f'O segundo dígito do CPF é {segundo_digito}')

# CPF final gerado
cpf_gerado = dez_digitos_cpf + str(segundo_digito)
print(f'CPF gerado: {cpf_gerado}')

# Comparação com CPF fornecido
if cpf_gerado == cpf_fornecido:
    print("✅ CPF válido!")
else:
    print("❌ CPF inválido!")
