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
    if escolha == 1:
        print(f"{matriz[0]}")
    elif escolha == 2:
        print(f"{matriz[1]}")
    elif escolha == 3:
        print(f"{matriz[2]}")
    else:
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
            
        