'''

Introdução ao desempacotamento + tuplas

'''

nomes = ['Maria', 'Helena', 'Luiz']

# se tentar pegar um único valor, dará erro pois tem mais de um armazenado no pacote. se apagar de dentro do pacote, dará erro se tiver variáveis declaradas fora do pacote.

# sempre que eu for pegar um único item de uma lista, devo jogar o restante dos valores numa outra variável '_'

# nome1, *_ = ['Maria', 'Helena', 'Luiz']
# print(nome1, _)

# esse _ serve para ignorar os elementos que voce não deseja retornar no print, substitua esses elementos pelo _

_, nome2, *_ = ['Maria', 'Helena', 'Luiz']
print(nome2, _)

'''
Tuplas

É uma lista imutável

'''

# para criar uma tupla, basta criar uma lista sem os colchetes []

nomes = 'Maria', 'Helena', 'Luiz'
print(nomes)