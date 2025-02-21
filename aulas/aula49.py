'''
Exercício

Faça uma lista de compras com listas
O usuário deve conseguir inserir, apagar e listar itens da lista
O programa não pode quebrar se o usuário inserir itens inexistentes na lista

'''

lista = []


print('Selecione uma opção')
opcao = input('[i]nserir [a]pagar [l]istar: ')


while True:

    if opcao == 'i':

        valor = input('Digite o nome do item que deseja adicionar: ')

        try:
            lista.append(valor)
            for indice, nome in enumerate(lista, start=1):
                print(indice, nome)
            print('Adicionar outro item?')
            escolha = input ('[S]im [N]ão: ').upper()
            if escolha == 'S':
                continue
            if escolha == 'N':
                opcao = input('[i]nserir [a]pagar [l]istar: ') 

        except: 
            print('Tente novamente')  
            continue 

    if opcao == 'a':

        print(lista)
        valor = input('Digite o nome do item que deseja remover: ')

        try:
            lista.remove(valor)
            for indice, nome in enumerate(lista, start=1):
             print(indice, nome)
            print('Remover outro item?')
            escolha = input ('[S]im [N]ão: ').upper()
            if escolha == 'S':
                continue
            if escolha == 'N':
                opcao = input('[i]nserir [a]pagar [l]istar: ') 

        except: 
            print('Tente novamente')
            continue
    
    if opcao == 'l':

        for indice, nome in enumerate(lista, start=1):
          print(indice, nome)
        opcao = input('[i]nserir [a]pagar [l]istar: ') 

