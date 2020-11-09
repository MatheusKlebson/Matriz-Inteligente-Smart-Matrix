def cabeçalho(txt):
    '''
    PARAM txt: Recebe o texto que ficará no centro do cabeçalho
    '''
    tam = len(txt) + 5
    print("="*tam)
    print(txt)
    print("="*tam)


def mostraLinha(tamanho):
    '''Escreve uma linha na tela'''
    print("="*tamanho)

def menu(lista):
    cabeçalho("MENU DO SISTEMA")
    for i,opções in enumerate(lista):
        print(f"{i + 1} - {opções}")
    print(mostraLinha(52))
    opc = leiaInt("Sua opção: ")
    return opc


def leiaInt(mensagem):
    while True:
        try:
            num = int(input(mensagem))
        except (ValueError,TypeError):
            print("ERRO!! Por favor digite um valor inteiro...")
        except (KeyboardInterrupt):
            print("O usuário interropeu o programa, o valor será nulo.")
            return 0
        else:
            return num
            break


def leiaFloat(mensagem):
    while True:
        try:
            num = float(input(mensagem))
        except (ValueError,TypeError):
            print('ERRO!! Por favor escreva um valor real...')
        except (KeyboardInterrupt):
            print("O usuário interropeu o programa, o valor será nulo.")
            return 0
        else:
            return num
            break

def leiaDinheiro(msg):
    validar = False
    while validar == False:
        preço = str(input(msg)).strip().replace(",",".")
        if preço.isalpha() or preço == "":
            print(f"ERRO!! \"{preço}\" não é um valor")
        else:
            validar = True
            return float(preço)

