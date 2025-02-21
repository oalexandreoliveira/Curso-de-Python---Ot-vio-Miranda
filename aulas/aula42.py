'''
Exercício 

Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.

'''

palavra_secreta = 'Macumba'
tentativas = 0
palpite = ''

print('Bem vindo ao jogo da palavra secreta!')

while tentativas < len(palavra_secreta):

    letra = input('Digite uma letra: ')
    print(letra)

    if letra in palavra_secreta:
        print(f'A letra {letra} está na palavra secreta')
    else:
        print('*')
    
    tentativas += 1
    print(f'Suas tentativas ({tentativas})')

    if tentativas == len(palavra_secreta):

        palpite = input('Você deseja tentar um palpite? (s)im / (n)ão: ')
        if palpite == 's':

            chute = input('Diga o seu palpite: ')
            if chute == palavra_secreta:
                print('Parabéns, você acertou!')
                break
            else:
                print('Você errou! Tente novamente.')
        
        else:
            print('Fim das tentativas. Você perdeu!')
