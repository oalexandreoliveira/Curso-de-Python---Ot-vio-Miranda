# Conversão de tipo, coerção

# Type Convertion -> converter um dado de um tipo em outro

# Tipos de Dados imutáveis e primitivos: 
# Str, Int, Float, Bool

"""
print('1' + 1) # isso retorna erro

"""

# Convertendo:

print(int('1') + 1) # agora o resultado será 2.

"""
ao adicionar o 'int' antes do parenteses contendo a minha string, eu forço o python a transformar esse texto em um valor numérico.
desse modo = 1+1 = 2. vamos tirar a prova:

"""

print(type('1'))
print(type(int('1')))

# a conversão foi satisfatória.