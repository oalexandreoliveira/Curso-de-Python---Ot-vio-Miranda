# Try e Except

# try - tentar executar
# except - ocorreu um erro ao tentar executar

numero_str = input('Vou triplicar o número que você digitar: ')

try:
    """
    A intenção é fazer um teste logo no início do código para validar a lógica, 
    se o usuário quebrar a lógica do fluxo do código, ao invés de percorrer todo o código e dar erro, 
    pula direto pro except para encerrar o programa.
    """
    numero_float = float(numero_str)
    print('Float: ', numero_float)
    print(f'O triplo desse número é: {numero_float * 3:.2f}')

except:
    print('Você não digitou um número')