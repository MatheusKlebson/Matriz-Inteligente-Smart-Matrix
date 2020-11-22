from matdef import matheus_texto

def leiaInt(mensagem):
    '''
    PARAM mensagem: Recebe a string que ficará na função leiaInt que substitui a função int(input())
    '''
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


def factorial(calculo):
    matheus_texto.mostraLinha(52)
    f = 1
    for cont in range(calculo,0,-1):
        print(f"{cont}",end="")
        if cont > 1:
            print(" X ",end="")
        else:
            print(" = ",end="")
        f *= cont
    return f
    