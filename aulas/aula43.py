'''

Listas em Python

List - Tipo mutável
Suporta vários valores de qualquer tipo
Podemos utilizar índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +

Create, Read, Update, Delete (CRUD)

'''

#        +01234
string = 'ABCDE'

lista = [123, True, 'Ale', 7.9, []]

# acessar elemento por indice:

print(lista[3])

# adicionando elementos:

lista.append(50)
print(lista)

# removendo elementos:

# o del vai apagar conforme o índice que você especificar
del lista[-1]
print(lista)

# por padrão, o pop removerá o último elemento da lista (-1), mas se você quiser, pode atribuir um índice
# o pop é ideal para ser usado em listas enormes, em que remover via delete pode causar estresse no processamento

lista.pop()
print(lista)

lista.pop(2)
print(lista)

# Insert: inserindo itens em qualquer índice da lista

# mesmo funcionamento do pop, mas para inserir

lista.insert(0, 5)
print(lista)

# .insert(posição, elemento)
# .insert(eu quero que nessa posição, você coloque esse elemento)
# lista.insert(coloque na posição 0, o elemento 5)

# Unindo listas 

#Via +
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b

# vai unir e te entregar o resultado

#Via extend

lista_b.extend(lista_a)

# vai unir dentro da lista b mas não vai te apresentar o resultado. nao pode ser declarado como outra variável por causa disso.

