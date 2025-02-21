'''

While / Else
Em Python temos a possibilida de de combinar while e else. O else só não será
executado caso dentro do while haja um break.

'''

string = 'abc'

i = 0

while i < len(string):
    letra = string[i]

    print(letra)
    i += 1
else:
    print('Else executado')
