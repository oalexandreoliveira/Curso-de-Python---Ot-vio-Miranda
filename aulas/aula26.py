# Formatação de strings

# s - string
# d - int
# f - float

# . <número de dígitos>f
# (caractere) (><^) (quantidade)


# > - esquerda
# < - direita
# ^ - centro
# Sinal - + ou -
# Ex.: 0>-100, .1f
# Conversion flags - !r !s !a

variavel = 'ale'
print(f'{variavel}')
print(f'{variavel: <10}')
print(f'{variavel: >10}')
print(f'{variavel: ^10}')
 