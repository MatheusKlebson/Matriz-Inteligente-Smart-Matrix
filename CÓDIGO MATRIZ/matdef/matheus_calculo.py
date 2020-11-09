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

