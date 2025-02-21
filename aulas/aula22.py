# Operadores Lógicos
# 'or' 
# or > pelo menos uma verdade

entrada = input('[E]ntrar ou [S]air: ' )
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# agora a primeira condicional depende da vaildação desse OR antes de seguir para a validação do AND fora dos parênteses
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Acesso permitido')

else:
    print('Acesso negado')


# Avaliação de Curto Circuito
print(True or False or 0 or 'abc' or True)