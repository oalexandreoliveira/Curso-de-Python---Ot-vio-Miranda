'''
While + Continue

'''

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Pula o 6')
        continue

    if contador >= 10 and contador <= 27:
        print('Pula o', contador)
        continue

    print(contador)

    if contador == 40:
        break