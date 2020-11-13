from matdef.matheus_texto import *
from matdef.matheus_calculo import * 
from time import sleep

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
"TRABALHAR COM NÚMEROS ESPECIFICOS",
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


elif opção == 4:  #Executa a quarta opção do menu
    posições = [] #Lista para guardar as posições
    numeros = []  #Lista para guardar os valores
    try:
        total = leiaInt("Quantos números deseja calcular? ")
        mostraLinha(52)
        if total > 1:
            for cont in range(1,total+1):
                l = leiaInt(f"Qual linha se encontra o {cont}º número? ")
                c = leiaInt(f"Qual coluna está o número que deseja? ")
                posições.append([l,c])
                num = matriz[l][c]
                numeros.append(num)

            '''[1num,2num,3num]'''
            cabeçalho("POSIÇÕES ESCOLHIDAS")
            for i,tabela in enumerate(numeros):
                print(f"{i + 1}º - ({tabela}): [{posições[i][0]},{posições[i][1]}]")
        
            cabeçalho("O QUE DESEJA? ")
            calcular_numeros = menu(["SOMAR",
            "MAIOR NÚMERO SELECIONADO",
            "MENOR NÚMERO SELECIONADO",
            "MOSTRAR TODOS OS PARES",
            "MOSTRAR TODOS OS ÍMPARES",
            "MOSTRAR DUAS LISTAS, UMA DE PARES E OUTRA DE ÍMPARES"])
            if calcular_numeros == 1:
                print(f"A soma de todos os números: {sum(numeros)}")
            elif calcular_numeros == 2:
                print(f"O maior número: {max(numeros)}")
            elif calcular_numeros == 3:
                print(f"O menor número: {min(numeros)}")
            elif calcular_numeros == 4: 
                pares = []
                for cont in range(0,len(numeros)):
                    if numeros[cont] % 2 == 0:
                        pares.append(numeros[cont])
                print(f"Lista dos pares: {pares}")
            elif calcular_numeros == 5: 
                ímpares = []
                for cont in range(0,len(numeros)):
                    if numeros[cont] % 2 == 0:
                        num = 0
                    else:
                        ímpares.append(numeros[cont])
                print(f"Lista dos ímpares: {ímpares}")
            elif calcular_numeros == 6:
                pares = []
                ímpares = []
                for cont in range(0,len(numeros)):
                    if numeros[cont] % 2 == 0:
                        pares.append(numeros[cont])
                    else:
                        ímpares.append(numeros[cont])
                print(f"Lista dos pares: {pares}")
                print(f"Lista dos ímpares: {ímpares}")
        elif total == 1:
            l = leiaInt(f"Qual linha se encontra o número? ")
            c = leiaInt(f"Qual coluna está o número que deseja? ")
            posições.append([l,c])
            num = matriz[l][c]
            numeros.append(num)
            cabeçalho("POSIÇÃO ESCOLHIDA")
            for i,tabela in enumerate(numeros):
                print(f"{i + 1}º - ({tabela}): [{posições[i][0]},{posições[i][1]}]")
            cabeçalho("O QUE DESEJA? ")
            analisar_numero = menu(["Dobro",
            "Triplo",
            "Raiz Quadrada",
            "Raiz Cubica",
            "FATORIAL",
            "BINÁRIO", 
            "HEXADECIMAL",
            "OCTAL"])
            if analisar_numero == 1:
                dobro = num * 2
                print(f"O dobro de {num}: {dobro}")
            elif analisar_numero == 2:
                triplo = num * 3
                print(f"O triplo de {num}: {triplo}")
            elif analisar_numero == 3:
                raiz_quadrada = num**(1/2)
                print(f"A raiz quadrada de {num}: {raiz_quadrada}")
            elif analisar_numero == 4:
                raiz_cubica = num**(1/3)
                print(f"A raiz cubida de {num}: {raiz_cubica}")
            elif analisar_numero == 5:
                print(f"Fatorial de {num}")
                print(factorial(num))
            elif analisar_numero == 6:
                print(f"Binário de {num}: {bin(num)[2:]}")
            elif analisar_numero == 7:
                print(f"Hexadecimal de {num}: {hex(num)[2:]}")
            elif analisar_numero == 8:
                print(f"Octal de {num}: {oct(num)[2:]}")
        else:
            print("Número não encontrado")
    except (IndexError):
        mostraLinha(52)
        print("Você digitou um valor inválido")
        sleep(2)
        print("O programa não pode continuar...")
        
cabeçalho("<<<ENCERRADO>>>".center(47))