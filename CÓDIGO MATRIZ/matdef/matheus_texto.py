from matdef import matheus_calculo

def cabeçalho(txt):
    '''
    PARAM txt: Recebe o texto que ficará no centro do cabeçalho
    '''
    tam = len(txt) + 5
    print("="*tam)
    print(txt.center(tam))
    print("="*tam)


def mostraLinha(tamanho):
    '''Escreve uma linha na tela'''
    print("="*tamanho)

def menu(lista):
    for i,opções in enumerate(lista):
        print(f"{i + 1} - {opções}")
    mostraLinha(52)
    opc = matheus_calculo.leiaInt("Sua opção: ")
    return opc

