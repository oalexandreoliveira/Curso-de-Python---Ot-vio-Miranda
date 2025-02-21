nome = 'Alexandre Oliveira'
altura = 1.68
peso = 78
imc = peso / (altura * altura)

print(nome, 'tem', altura, 'pesa', peso, 'kg', 'e seu IMC é de', imc)

# f strings
# são formatações das strings que possibilitam a inserção de variáveis dentro da sua cadeia de caracteres.
# para acionar essa formatação, a cadeia de caractere deve ser iniciada com f'
# a variável poderá ser chamada dentro da string se inserida entre chaves {}

print(f'{nome} tem {altura}, pesa {peso} e seu IMC é de {imc}')

# f string também corrige o problema da visualização das casas decimais
# utilizando :.(x)f você irá mandar o python mostrar a quantidade x de casas decimais

print(f'{nome} tem {altura}, pesa {peso} e seu IMC é de {imc: .2f}')

# essa formatação de casas decimais pode ser utilizada para corrigir valores monetários, unidades de medida, etc.