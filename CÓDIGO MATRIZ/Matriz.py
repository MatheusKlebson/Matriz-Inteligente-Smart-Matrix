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

for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end=" ")
    print()
