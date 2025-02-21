'''
Laço de repetição FOR
Iteração para coisas finitas


texto = 'Rebeca da Cruz Ramos'

for letra in texto:
    print(letra)

'''

# For + Range
# range -> range(start, stop, step)

'''
numeros = range (5, 25, 5)

for numero in numeros:
    print(numero)
'''

'''
Iterável -> str, range, etc. Ex: 'Nome'
Iterador -> quem entrega um valor por vez
next -> me entrega o próximo valor
    sempre irá retornar o próximo valor disponível
    se esgotarem os valores retornará erro
iter -> me entrega o iterador

não se pode usar _next_ sem o iter.
'''

texto = iter('Alexandre') 
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())