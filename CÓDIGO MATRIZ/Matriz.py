def cabeçalho(txt):
    tam = len(txt) + 5
    print("="*tam)
    print(txt)
    print("="*tam)


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
print("="*52)
cabeçalho("                 MENU DE OPÇÕES                ")
opção = int(input('''[1] - ANALISAR LINHA
[2] - ANALISAR COLUNA
[3] - ANALISAR NÚMERO PELA POSIÇÃO
[4] - CALCULAR NÚMEROS ESPECIFICOS
[5] - CRIAR OUTRA MATRIZ
[6] - SAIR DO PROGRAMA
Digite: '''))