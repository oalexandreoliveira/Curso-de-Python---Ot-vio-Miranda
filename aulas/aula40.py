frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

print(frase)

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    contar_letra = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < contar_letra:
        qtd_apareceu_mais_vezes = contar_letra
        letra_apareceu_mais_vezes = letra_atual


    print(letra_atual, contar_letra)

    i += 1