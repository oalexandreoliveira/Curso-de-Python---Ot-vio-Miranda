# Operadores Lógicos
# 'and' 
# and > duas verdades

entrada = input('[E]ntrar ou [S]air: ' )
senha_digitada = 123456
input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Acesso permitido')

else:
    print('Acesso negado')