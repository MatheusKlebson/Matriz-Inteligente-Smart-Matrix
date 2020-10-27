def cabeçalho(txt):
    tam = len(txt) + 5
    print("="*tam)
    print(txt)
    print("="*tam)


def mostraLinha():
    print("="*52)


cabeçalho("               MATRIZ INTELIGENTE              ")
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite o valor da casa [{linha},{coluna}]: "))
cabeçalho("                 MATRIZ FORMADA                ")
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end=" ")
    print()
'''[[1, 2, 3], [4, 5, 6], [7, 8, 9]]'''
mostraLinha()
cabeçalho("                 MENU DE OPÇÕES                ")
opção = int(input('''[1] - ANALISAR LINHA
[2] - ANALISAR COLUNA
[3] - ANALISAR NÚMERO PELA POSIÇÃO
[4] - CALCULAR NÚMEROS ESPECIFICOS
[5] - CRIAR OUTRA MATRIZ
[6] - SAIR DO PROGRAMA
Digite: '''))
mostraLinha()
if opção == 1:
    escolha = int(input("Deseja analisar qual linha? "))
    print(f"LINHA {escolha}: ",end="")
    for l in range(0,1):
        for c in range(0,3):
            if escolha == 1:
                print(f"[{matriz[0][c]}]",end=' ')
            elif escolha == 2:
                print(f"[{matriz[1][c]}]",end=' ')
            elif escolha == 3:
                print(f"[{matriz[2][c]}]",end=' ')
    if escolha > 3 or escolha <= 0:
        print(f"não existe")
elif opção == 2:
    escolha = int(input("Deseja analisar qual coluna? "))
    print(f"COLUNA {escolha}: ",end="")
    for l in range(0,3):
        for c in range(0,1):
            if escolha == 1:
                print(f"[{matriz[l][0]}]",end=' ')
            elif escolha == 2:
                print(f"[{matriz[l][1]}]",end=' ')
            elif escolha == 3:
                print(f"[{matriz[l][2]}]",end=' ')
    if escolha > 3 or escolha <= 0:
        print(f"não existe")
elif opção == 3:
    print("Deseja analisar qual posição? Exemplo: [0,0] ")
    li = int(input("["))
    co = int(input(f"[{li},"))
    for i,ma in enumerate(matriz):
        if li == i: 
            print(f"Número na posição [{li},{co}]: {matriz[li][co]}")
    print(f"POSIÇÃO: [{li},{co}]")
    if li >= 3 or li < 0:
        print(f"Linha indicada: não existe")
    if co >= 3 or co < 0: 
        print(f"Coluna indicada: não existe")
elif opção == 4:
    l1 = int(input("Qual linha se encontra o primeiro número? "))
    c1 = int(input("Qual coluna está o número? "))
    n1 = matriz[l1][c1]
    l2 = int(input("Qual linha se encontra o segundo número? "))
    c2 = int(input("Qual coluna está o número? "))
    n2 = matriz[l2][c2]
    print(f"Posição do número {n1}: [{l1},{c1}] ")
    print(f"Posição do número {n2}: [{l2},{c2}] ")
print("="*50)