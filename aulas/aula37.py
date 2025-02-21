'''
Exercício
iterando strings com while

'''

# Minha solução do exercício:
#       0123456789
nome = 'Rebeca da Cruz Ramos' #iteráveis
#       987654321

meu_nome = 0
tam_nome = len(nome)

while meu_nome < tam_nome:
    print(nome[meu_nome])

    meu_nome += 1

# Adicionando uma string com o nome todo concatenado conforme o professor:
'''
while meu_nome < tam_nome:
    letra = nome[meu_nome]
    novo_nome += letra
    meu_nome += 1

print(novo_nome)

'''
