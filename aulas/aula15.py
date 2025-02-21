# função input

# utilizada para coleta de dados

# input('Qual seu nome? ') # ela não altera o código, ela apenas recebe o dado.
# os dados recebidos via input sempre serão do tipo str.

nome = input('Qual seu nome? ') # quando há uma variável antes do input o dado coletado pela função será armazenado na variável.
print(f'O seu nome é {nome}')

# como converter a string armazenada em inteiro:

num_1 = input('Digite um número: ')

int_num_1 = int(num_1)

print(type(int_num_1))
