cinema = []

def inserirSala(cinema):
    filme = input("Introduza o nome do filme")
    for n in cinema:
        nlugares, vendidos, nome = n
        if nome == filme:
            print("O filme ja existe")
            menu()
    nlugares = int(input("Introduza o numero de lugares na sala"))
    vendidos = []
    cinema.append((nlugares, vendidos, filme))
    print("sala criada")
    print("Salas:", cinema)
    menu()

def removerSala(cinema):
    index = int(input("introduza o indice da sala"))
    cinema.pop(index)
    print("sala removida")
    print("Salas:", cinema)
    menu()

def listarSalas(cinema):
    print("Sala           Filme")
    print("--------------------------")
    for p in cinema:
        nlugares, vendidod, filme = p
        print("Sala{}".format(cinema.index(p)), "   ", filme)
    menu()

def lugarDisponivel(cinema, filme, lugar):
    for p in cinema:
        nlugares, vendidos, nome = p
        if filme == nome:
            if lugar in vendidos:
                res = False
            else:
                res= True
        else:
            res = False
    return res

def vendebilhete(cinema, filme, lugar):
    if lugarDisponivel(cinema, filme, lugar):
        for p in cinema:
            nlugares, vendidos, nome = p 
            if filme == nome:
                vendidos.append(lugar)
        print("O lugar foi vendido")
        print("Salas:", cinema)
    else:
        print("Lugar indisponivel")
    menu()

def listardisponibilidadesala(cinema):
    print("Sala  Filme  Lugares disponiveis")
    print("----------------------------------")
    for p in cinema:
        nlugares, vendidos, filme = p
        print("Sala{}".format(cinema.index(p)), " ", filme, " ", nlugares - len(vendidos))
    menu()

def menu():
    print("""
    -------------------
    1- Criar sala
    2- Remover sala
    3- Listar salas
    4- Lugar disponivel
    5- Vender bilhete
    6- Consultar salas
    0- Sair
    ------------------- 
    """)

    opc = int(input("Escolha a opção de 0 a 6 do menu"))
    if opc == 1:
        inserirSala(cinema)
    elif opc == 2:
        removerSala(cinema)
    elif opc == 3:
        listarSalas(cinema)
    elif opc == 4:
        filme = input("Introduza o nome do filme")
        lugar= int(input("Introduza o lugar"))
        print("Lugar disponivel", lugarDisponivel(cinema, filme, lugar))
    elif opc == 5:
        filme = input("Introduza o nome do filme")
        lugar = int(input("Introduza o lugar"))
        vendebilhete(cinema, filme, lugar)
    elif opc == 6:
        listardisponibilidadesala(cinema)
    elif opc == 0:
        print("Reset efetuado com sucesso")
        print("salas", cinema)

menu()
