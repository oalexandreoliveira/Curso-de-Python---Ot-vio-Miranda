'''

Enumerate = enumera iteráveis

Faz o trabalho da aula anterior com mais agilidade

'''

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# lista_enumerada = enumerate(lista)
# print(lista_enumerada)

# dessa maneira irá me retorna um objeto estranho, para contornar, pode converter em lista normal:

# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada) 

# retornando o indice e o nome:

for indice, nome in enumerate(lista):
    print(indice, nome)