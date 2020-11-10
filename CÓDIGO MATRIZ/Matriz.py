from matdef.matheus_texto import *
from matdef.matheus_calculo import * 

'''Montando a matriz'''
cabeçalho("               MATRIZ INTELIGENTE              ")
matriz = [[0,0,0],[0,0,0],[0,0,0]]
'''[[1, 2, 3], [4, 5, 6], [7, 8, 9]]'''
cont = 1
for linha in range(0,3):
    for coluna in range(0,3):
        print(f"[{linha},{coluna}]: {cont}")
        matriz[linha][coluna] = cont
        cont += 1

'''Matriz formada e mostrada na tela'''
cabeçalho("                 MATRIZ FORMADA                ")
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end=" ")
    print()
mostraLinha(52)

'''Menu de opções, sendo mostrado na tela 
através de uma função para criar um menu através dos elementos contido dentro da lista'''

cabeçalho("                 MENU DE OPÇÕES                ")
opção = menu(["ANALISAR LINHA",
"ANALISAR COLUNA",
"ANALISAR NÚMERO PELA POSIÇÃO",
"CALCULAR NÚMEROS ESPECIFICOS",
"CRIAR OUTRA MATRIZ",
"SAIR DO PROGRAMA"])
mostraLinha(52)

'''Condicionais para executar a opção selecionada pelo usuário'''

if opção == 1: #Executa a primeira opção do menu
    escolha = int(input("Deseja analisar qual linha? ")) #Pergunta ao usuário qual linha irá pegar os valores
    '''Mostra linha escolhida na tela'''
    print(f"LINHA {escolha}: ",end="")
    '''Laço For que irá "andar" sobre toda a matriz para mostrar os valores pedidos'''
    for l in range(0,1):
        for c in range(0,3):
            if escolha == 1:
                print(f"[{matriz[0][c]}]",end=' ')
            elif escolha == 2:
                print(f"[{matriz[1][c]}]",end=' ')
            elif escolha == 3:
                print(f"[{matriz[2][c]}]",end=' ')
    '''Caso a opção digitada pelo usuário seja inválida'''
    if escolha > 3 or escolha <= 0:
        print(f"não existe")
elif opção == 2: #Executa a segunda opção do menu
    escolha = int(input("Deseja analisar qual coluna? "))  #Pergunta ao usuário qual coluna irá pegar os valores
    '''Mostra coluna escolhida na tela'''
    print(f"COLUNA {escolha}: ",end="")
    '''Laço For que irá "andar" sobre toda a matriz para mostrar os valores pedidos'''
    for l in range(0,3):
        for c in range(0,1):
            if escolha == 1:
                print(f"[{matriz[l][0]}]",end=' ')
            elif escolha == 2:
                print(f"[{matriz[l][1]}]",end=' ')
            elif escolha == 3:
                print(f"[{matriz[l][2]}]",end=' ')
    '''Caso a opção digitada pelo usuário seja inválida'''
    if escolha > 3 or escolha <= 0:
        print(f"não existe")
elif opção == 3: #Executa a terceira opção do menu
    '''O usuário poderá ver um número especifico dá matriz, 
    digitando a posição que ele se encontra'''
    print("Deseja analisar qual posição? Exemplo: [0,0] ")
    li = int(input("[")) #Primeiro pergunta qual a linha 
    co = int(input(f"[{li},")) #Pergunta a coluna
    '''Laço For que irá encontrar a posição e seu especifico número, solicitado pelo usuário'''
    for i,ma in enumerate(matriz):
        if li == i: 
            print(f"Número encontrado: {matriz[li][co]}")
    '''Posição solicitada é mostrada na tela'''
    print(f"POSIÇÃO: [{li},{co}]")
    '''Dois If para caso a coluna ou a linha seja inválida'''
    if li >= 3 or li < 0:
        print(f"Linha indicada: não existe")
    if co >= 3 or co < 0: 
        print(f"Coluna indicada: não existe")
elif opção == 4: #Executa a quarta opção do menu
    numeros = []
    total = leiaInt("Quantos números deseja calcular? ")
    for cont in range(1,total+1):
        l = leiaInt(f"Qual linha se encontra o {cont}º número? ")
        c = leiaInt(f"Qual coluna está o número que deseja? ")
        num = matriz[l][c]
        numeros.append(num)

    '''[1num,2num,3num]'''
    cabeçalho("POSIÇÕES ESCOLHIDAS")
    for indice,n in enumerate(numeros):
        print(f" - {indice + 1}º NÚMERO ({n}): [{indice[l]},{indice[c]}] ")
    
    #'''Conseguindo o primeiro valor'''
    '''l1 = leiaInt("Qual linha se encontra o primeiro número? ")
    c1 = leiaInt("Qual coluna está o número? ")
    n1 = matriz[l1][c1]

    #Conseguindo o segundo valor
    l2 = leiaInt("Qual linha se encontra o segundo número? ")
    c2 = leiaInt("Qual coluna está o número? ")
    n2 = matriz[l2][c2]
    
    print(f"PRIMEIRO NÚMERO ({n1}): [{l1},{c1}] ")
    print(f"SEGUNDO NÚMERO ({n2}): [{l2},{c2}] ")'''
    cabeçalho("O QUE DESEJA? ")
    calcular_numeros = leiaInt('''[1] - SOMAR
[2] - SUBTRAIR
[3] - MULTIPLICAR
[4] - DIVIDIR
[5] - SOMAR E TIRAR A RAIZ QUADRADA DO RESULTADO
[6] - SOMAR E EM SEGUIDA TIRAR O NÚMERO BINÁRIO, HEXADECIMAL OU OCTAL DO RESULTADO
Digite: ''')
print()
mostraLinha(52)