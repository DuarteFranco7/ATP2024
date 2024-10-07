import random

def escolha():
    print("1. Começa o utilizador.")
    print("2. Começa o computador.")
    print("3. Sair.")
    opcao = input("Escolha uma opção: ")
    return opcao

def utilizador(): #utilizador começa 
    fosforos = 21
    jogo_ativo = 1
    while fosforos > 1 and jogo_ativo == 1:
        jog = int(input("Começas a tirar os fósforos, quantos queres tirar? "))
        fosforos -= jog
        print(f"Retiraste {jog} fósforos. Ficaram {fosforos} fósforos.")
        if fosforos <= 1:
            print("Perdeste! Agora és tu e sobra apenas 1 fósforo!")
            jogo_ativo = 0
        if jogo_ativo == 1:
            comp = 5 - jog
            fosforos -= comp
            print(f"Retirei {comp} fósforos. Ficaram {fosforos} fósforos.")
            if fosforos <= 1:
                print("Ganhei! Sobra apenas 1 fósforo.")
                jogo_ativo = 0

def pc(): #pc começa 
    fosforos = 21
    jogo_ativo = 1
    while fosforos > 1 and jogo_ativo == 1:
        comp = random.randint(1, 4)
        fosforos -= comp
        print(f"Retirei {comp} fósforos. Ficaram {fosforos} fósforos.")
        if fosforos <= 1:
            print("Ganhei! Sobra apenas 1 fósforo.")
            jogo_ativo = 0
        if jogo_ativo == 1:
            jog = int(input("É a tua vez, quantos fósforos queres tirar? "))
            fosforos -= jog
            print(f"Retiraste {jog} fósforos. Ficaram {fosforos} fósforos.")
            if fosforos <= 1:
                print("Ganhaste. Agora sou eu e sobra apenas 1 fósforo.")
                jogo_ativo = 0

def main():
    opcao = ""
    while opcao != "3":
        opcao = escolha()
        if opcao == "1":
            utilizador()
        elif opcao == "2":
            pc()
        elif opcao == "3":
            print("ok!")
        else:
            print("Opção desconhecida")

main()