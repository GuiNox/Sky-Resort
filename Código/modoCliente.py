def menuListaPistas():

    print("--- Lista de Pistas ---")

    file = open('./data/tabelaPistas.txt', 'r')
    filedata = file.readlines()

    nPista = 1

    for line in filedata :

        pistaList = line.split("#")
        print("Pista " + str(nPista) + ": " + str(pistaList[0]) + "  " + str(pistaList[1]) + "  " + str(pistaList[2]) + "  " + str(pistaList[3]) + "  " + str(pistaList[4]) + "  " + str(pistaList[5]))
        nPista += 1


def menuListaMeiosMecanicos():

    print("--- Lista de Meios Mecânicos ---")

    file = open('./data/tabelaMeiosMecanicos.txt', 'r')
    filedata = file.readlines()

    nMM = 1

    for line in filedata :

        MMList = line.split("#")
        print("Meio Mecânico " + str(nMM) + ": " + str(MMList[0]) + "  " + str(MMList[1]) + "  " + str(MMList[2]) + "  " + str(MMList[3]) + "  " + str(MMList[4]))
        nMM += 1


def menuListaZonas():

    print("--- Lista de Zonas ---")

    file = open('./data/tabelaZonas.txt', 'r')
    filedata = file.readlines()

    nZona = 1

    for line in filedata :

        ZonaList = line.split("#")
        print("Zona " + str(nZona) + ": " + str(ZonaList[0]) + "  " + str(ZonaList[1]) + "  " + str(ZonaList[2]) + "  " + str(ZonaList[3]) + "  " + str(ZonaList[4]) + "  " + str(ZonaList[5]))
        nZona += 1


def menuListaZonasDetalhe():

    print("--- Lista de Zonas em Detalhe ---")

    file = open('./data/tabelaZonas.txt', 'r')
    filedata = file.readlines()

    Zonas = []
    for line in filedata :
        dadosList = line.split("#")
        Zonas += [dadosList[0]]

    zona = input("Zona: ")

    fim = True
    while fim:
        
        if zona in Zonas:
            fim = False
        else:
            zona = input("Zona: ")


    file = open('./data/tabelaComodidades.txt', 'r')
    filedata = file.readlines()

    nComodidade = 1

    for line in filedata :

        comodidadesList = line.split("#")

        if comodidadesList[1] == zona:
            print(str(nComodidade) + " - " + str(comodidadesList[0]) + "  " + str(comodidadesList[2]))
            nComodidade += 1


def menuListaPistasDetalhe():

    print("--- Lista de Pistas em Detalhe ---")

    file = open('./data/tabelaPistas.txt', 'r')
    filedata = file.readlines()

    Pistas = []
    for line in filedata :
        dadosList = line.split("#")
        Pistas += [dadosList[0]]

    pista = input("Pista: ")

    fim = True
    while fim:
        
        if pista in Pistas:
            fim = False
        else:
            pista = input("Pista: ")


    file = open('./data/tabelaSeccoesEmPistas.txt', 'r')
    filedata = file.readlines()

    nSeccao = 1

    for line in filedata :

        seccoesList = line.split("#")

        if seccoesList[0] == pista:
            print( "Secção " + str(nSeccao) +": " + str(seccoesList[1]))
            nSeccao += 1


def menuProcuraPista():

    print("--- Procurar Pista ---")

    fim = True
    while fim:
        print("Tipo de Procura:")
        print("1 - Zona Inicial")
        print("2 - Dificuldade")
        print("3 - Estado")
        
        try:
            opSubMenu = int(input("Opção: "))
            fim = False
        except:
            print("Opção Inválida")

        if opSubMenu < 1 or opSubMenu > 3:
            fim = True


    if opSubMenu == 1:
        
        file = open('./data/tabelaZonas.txt', 'r')
        filedata = file.readlines()

        Zonas = []
        for line in filedata :
            dadosList = line.split("#")
            Zonas += [dadosList[0]]

        zona = input("Zona: ")

        fim = True
        while fim:
        
            if zona in Zonas:
                fim = False
            else:
                zona = input("Zona: ")


        file = open('./data/tabelaPistas.txt', 'r')
        filedata = file.readlines()

        for line in filedata :
            dadosList = line.split("#")
            
            if dadosList[2] == zona:
                print(str(dadosList[0]) + "  " + str(dadosList[1]) + "  " + str(dadosList[2]) + "  "
                + str(dadosList[3]) + "  " + str(dadosList[4]) + "  " + str(dadosList[5]))

    elif opSubMenu == 2:

        fim1 = True
        while fim1:
            print("Tipo de dificuldade:")
            print("1 - Fácil")
            print("2 - Intermédia")
            print("3 - Difícil")
            print("4 - Muito Difícil")
            
            try:
                opSubMenu1 = int(input("Opção: "))
                fim1 = False
            except:
                print("Opção Inválida")

            if opSubMenu1 < 1 or opSubMenu1 > 4:
                fim1 = True
            

            if opSubMenu1 == 1:

                file = open('./data/tabelaPistas.txt', 'r')
                filedata = file.readlines()

                for line in filedata :
                    dadosList = line.split("#")

                    if dadosList[4] == "facil":
                        print(str(dadosList[0]) + "  " + str(dadosList[1]) + "  " + str(dadosList[2]) + "  "
                        + str(dadosList[3]) + "  " + str(dadosList[4]) + "  " + str(dadosList[5]))

            elif opSubMenu1 == 2:

                file = open('./data/tabelaPistas.txt', 'r')
                filedata = file.readlines()

                for line in filedata :
                    dadosList = line.split("#")

                    if dadosList[4] == "intermedia":
                        print(str(dadosList[0]) + "  " + str(dadosList[1]) + "  " + str(dadosList[2]) + "  "
                        + str(dadosList[3]) + "  " + str(dadosList[4]) + "  " + str(dadosList[5]))

            elif opSubMenu1 == 3:

                file = open('./data/tabelaPistas.txt', 'r')
                filedata = file.readlines()

                for line in filedata :
                    dadosList = line.split("#")

                    if dadosList[4] == "dificil":
                        print(str(dadosList[0]) + "  " + str(dadosList[1]) + "  " + str(dadosList[2]) + "  "
                        + str(dadosList[3]) + "  " + str(dadosList[4]) + "  " + str(dadosList[5]))

            elif opSubMenu1 == 4:

                file = open('./data/tabelaPistas.txt', 'r')
                filedata = file.readlines()

                for line in filedata :
                    dadosList = line.split("#")

                    if dadosList[4] == "muitoDificil":
                        print(str(dadosList[0]) + "  " + str(dadosList[1]) + "  " + str(dadosList[2]) + "  "
                        + str(dadosList[3]) + "  " + str(dadosList[4]) + "  " + str(dadosList[5]))

    
    elif opSubMenu == 3:
        
        fim1 = True
        while fim1:
            print("Estado:")
            print("1 - Aberta")
            print("2 - Fechada")
            
            try:
                opSubMenu1 = int(input("Opção: "))
                fim1 = False
            except:
                print("Opção Inválida")

            if opSubMenu1 < 1 or opSubMenu1 > 2:
                fim1 = True
            

            if opSubMenu1 == 1:

                file = open('./data/tabelaPistas.txt', 'r')
                filedata = file.readlines()

                for line in filedata :
                    dadosList = line.split("#")

                    if dadosList[5] == "aberta":
                        print(str(dadosList[0]) + "  " + str(dadosList[1]) + "  " + str(dadosList[2]) + "  "
                        + str(dadosList[3]) + "  " + str(dadosList[4]) + "  " + str(dadosList[5]))

            elif opSubMenu1 == 2:

                file = open('./data/tabelaPistas.txt', 'r')
                filedata = file.readlines()

                for line in filedata :
                    dadosList = line.split("#")

                    if dadosList[5] == "fechada":
                        print(str(dadosList[0]) + "  " + str(dadosList[1]) + "  " + str(dadosList[2]) + "  "
                        + str(dadosList[3]) + "  " + str(dadosList[4]) + "  " + str(dadosList[5]))


def menuProcuraMeioMecanico():

    print("--- Procurar de Meio Mecânico ---")

    file = open('./data/tabelaZonas.txt', 'r')
    filedata = file.readlines()

    Zonas = []
    for line in filedata :
        dadosList = line.split("#")
        Zonas += [dadosList[0]]

    zona = input("Zona: ")

    fim = True
    while fim:
        
        if zona in Zonas:
            fim = False
        else:
            zona = input("Zona: ")

    
    file = open('./data/tabelaMeiosMecanicos.txt', 'r')
    filedata = file.readlines()

    listaNomes = []
    
    print("-- Ordem Ascendente --")
    for line in filedata :
        dadosList = line.split("#")

        if zona == dadosList[1] or (zona in dadosList and dadosList[4] == "bidirecional"):
            listaNomes += [dadosList[0]]


    fim = True
    while fim:
        print("Tipo de Ordenação:")
        print("1 - Ascendente")
        print("2 - Descendente")
        
        try:
            opSubMenu = int(input("Opção: "))
            fim = False
        except:
            print("Opção Inválida")

        if opSubMenu < 1 or opSubMenu > 2:
            fim = True


    if opSubMenu == 1:
        
        listaAscendente = sorted(listaNomes)

        for elem in listaAscendente:
            print(elem)
        

    elif opSubMenu == 2:

        listaDescendente = sorted(listaNomes, reverse=True)

        for elem in listaDescendente:
            print(elem)


def menu():

    print("--- Menu ---")
    print("1 - Lista de Pistas")
    print("2 - Lista de Meios Mecânicos")
    print("3 - Consultar Zonas")
    print("4 - Consultar Zona em Detalhe")
    print("5 - Consultar Pista em Detalhe")
    print("6 - Procurar Pistas")
    print("7 - Procurar Meios Mecânicos")


    try:
        opMenu = int(input("Opção: "))
    except:
        print("Opção Inválida")
        menu()

    if (opMenu < 1 or opMenu > 7):
        print("Opção Inválida")
        menu()
    else:

        if (opMenu == 1):
            menuListaPistas()
            menu()
        elif (opMenu == 2):
            menuListaMeiosMecanicos()
            menu()
        elif (opMenu == 3):
            menuListaZonas()
            menu()
        elif (opMenu == 4):
            menuListaZonasDetalhe()
            menu()
        elif (opMenu == 5):
            menuListaPistasDetalhe()
            menu()
        elif (opMenu == 6):
            menuProcuraPista()
            menu()
        elif (opMenu == 7):
            menuProcuraMeioMecanico()
            menu()


menu()
