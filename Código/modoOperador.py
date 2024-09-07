import random
import datetime
import math
import pyqrcode

def consultarBilhetes(referencia):

    try:
        tabelaBilhetes = open("./data/tabelaBilhetes.txt", "r", encoding="utf-8")
    except:
        print("O arquivo tabelaBilhete.txt não foi encontrado ou não pode ser aberto.")
        return

    linhas = tabelaBilhetes.readlines()
    for linha in linhas:
        dadosBilhetes = linha.replace("\n", " ").split("#")

        if dadosBilhetes[0] == referencia:
            validade = f"{dadosBilhetes[-4]}/{dadosBilhetes[-3]}/{dadosBilhetes[-2]}"
            qr_data = f"{referencia} {validade}"
            qr = pyqrcode.create(qr_data)

            qr.png(f"qr_code_{referencia}.png", scale=8)
            print(
                f"QR Code para a referência {referencia} gerado e salvo em qr_code_{referencia}.png")
            break
    else:
        print(
            f"Não foi encontrado nenhum bilhete com a referência {referencia}.")

    tabelaBilhetes.close()


def menuCriarZona():

    print("--- Criar Zona ---")

    fim = True
    while fim:

        fim = False
        codigoZona = input("Código da zona: ")
        numeros= ['0','1','2','3','4','5','6','7','8','9']
        for digito in codigoZona:
            if digito in numeros:
                fim = True

        if len(codigoZona) != 4:
            fim = True

    nome = input("Nome da zona: ")


    fim = True
    while fim:

        fim = False
        
        try:
            latitude = int(input("Latitude da zona: "))
        except:
            fim = True


    fim = True
    while fim:

        fim = False
        
        try:
            longitude = int(input("Longitude da zona: "))
        except:
            fim = True


    fim = True
    while fim:

        fim = False
        
        try:
            altitude = int(input("Altitude da zona: "))
        except:
            fim = True
    

    descricao = input("Descrição da zona: ")
    
    data = str(codigoZona) + '#' + str(nome) + '#' + str(latitude) + '#' + str(longitude) + '#' + str(altitude) + '#' + str(descricao) + '#'

    file = open('./data/tabelaZonas.txt', 'a')
    file.write(str(data) + '\n')
    file.close


def menuAdicionarComodidade():

    print("--- Adicionar Comodidade ---")
    nome = input("Nome da comodidade: ")
    zona = input("Zona da associada: ")

    file = open('./data/tabelaZonas.txt', 'r')
    filedata = file.readlines()

    codigosZonas = []
    for line in filedata :
        dadosList = line.split("#")
        codigosZonas += [dadosList[0]]

    fim = True
    while fim:
        
        if zona in codigosZonas:
            fim = False
        else:
            zona = input("Zona da associada: ")
    
    descricao = input("Descrição da comodidade: ")

    dataInsert = str(nome) + '#' + str(zona) + '#' + str(descricao) + '#'

    file = open('./data/tabelaComodidades.txt', 'a')
    file.writelines(str(dataInsert) + '\n')
    file.close


def menuAdicionarSeccao():

    print("--- Adicionar Secção ---")
    
    file = open('./data/tabelaZonas.txt', 'r')
    filedata = file.readlines()

    codigosZonas = []
    for line in filedata :
        dadosList = line.split("#")
        codigosZonas += [dadosList[0]]

    zonaInicio = input("Início da secção: ")

    fim = True
    while fim:
        
        if zonaInicio in codigosZonas:
            fim = False
        else:
            zonaInicio = input("Início da secção: ")

    zonaFim = input("Fim da secção: ")

    fim = True
    while fim:
        
        if zonaFim in codigosZonas and zonaFim != zonaInicio:
            fim = False
        else:
            zonaFim = input("Fim da secção: ")

    
    for line in filedata :
        dadosList = line.split("#")

        if dadosList[0] == zonaInicio:
            latitudeA = int(dadosList[2])
            longitudeA = int(dadosList[3])
            altitudeA = int(dadosList[4])

        if dadosList[0] == zonaFim:
            latitudeB = int(dadosList[2])
            longitudeB = int(dadosList[3])
            altitudeB = int(dadosList[4])

    
    distancia = ( math.sqrt( (latitudeB - latitudeA)**2 + (longitudeB - longitudeA)**2 + (altitudeB - altitudeA)**2) )

    dataInsert = str(zonaInicio) + "-" + str(zonaFim) + '#' + str(zonaInicio) + '#' + str(zonaFim) + '#' + str(round(distancia,2)) + '#'

    file = open('./data/tabelaSeccoes.txt', 'a')
    file.writelines(str(dataInsert) + '\n')
    file.close


def menuAdicionarMeioMecanico():

    print("--- Adicionar Meio Mecânico ---")
    nome = input("Nome do meio mecânico: ")

    zonaPartida = input("Zona de partida: ")

    file = open('./data/tabelaZonas.txt', 'r')
    filedata = file.readlines()

    codigosZonas = []
    for line in filedata :
        dadosList = line.split("#")
        codigosZonas += [dadosList[0]]

    fim = True
    while fim:
        
        if zonaPartida in codigosZonas:
            fim = False
        else:
            zonaPartida = input("Zona de partida: ")

    
    zonaChegada = input("Zona de chegada: ")

    fim = True
    while fim:
        
        if zonaChegada in codigosZonas and zonaChegada != zonaPartida:
            fim = False
        else:
            zonaChegada = input("Zona de chegada: ")
    

    fim = True
    while fim:
        print("Estado do meio mecânico:")
        print("1 - aberto")
        print("2 - fechado")
        
        try:
            opSubMenu = int(input("Opção: "))
            estado = opSubMenu
            fim = False
        except:
            print("Opção Inválida")

        if opSubMenu < 1 or opSubMenu > 2:
            fim = True
    

    fim = True
    while fim:
        print("Tipo do meio mecânico:")
        print("1 - ascendente")
        print("2 - descendente")
        print("3 - bidirecional")
        
        try:
            opSubMenu = int(input("Opção: "))
            tipo = opSubMenu
            fim = False
        except:
            print("Opção Inválida")

        if opSubMenu < 1 or opSubMenu > 3:
            fim = True


    if estado == 1:
        estado = "aberto"
    elif estado == 2:
        estado = "fechado"


    if tipo == 1:
        tipo = "ascendente"
    elif tipo == 2:
        tipo = "descendente"
    elif tipo == 3:
        tipo = "bidirecional"
    
    
    dataInsert = str(nome) + '#' + str(zonaPartida) + '#' + str(zonaChegada) + '#' + str(estado) + '#' + str(tipo) + '#'

    file = open('./data/tabelaMeiosMecanicos.txt', 'a')
    file.writelines(str(dataInsert) + '\n')
    file.close


def menuAdicionarPista():

    print("--- Adicionar Pistas ---")
    
    nome = input("Nome da pista: ")
    
    file = open('./data/tabelaZonas.txt', 'r')
    filedata = file.readlines()

    codigosZonas = []
    for line in filedata :
        dadosList = line.split("#")
        codigosZonas += [dadosList[0]]

    zonaInicio = input("Zona de Início: ")

    fim = True
    while fim:
        
        if zonaInicio in codigosZonas:
            fim = False
        else:
            zonaInicio = input("Zona de Início: ")

    zonaFim = input("Zona de Fim: ")

    fim = True
    while fim:
        
        if zonaFim in codigosZonas and zonaFim != zonaInicio:
            fim = False
        else:
            zonaFim = input("Zona de Fim: ")

    codigoPista = "P" + str(zonaInicio) + "-" + str(zonaFim)


    fim = True
    while fim:
        print("Dificuldade da pista:")
        print("1 - fácil")
        print("2 - intermedia")
        print("3 - difícil")
        print("4 - muito difícil")
        
        try:
            opSubMenu = int(input("Opção: "))
            dificuldade = opSubMenu
            fim = False
        except:
            print("Opção Inválida")

        if opSubMenu < 1 or opSubMenu > 4:
            fim = True


    fim = True
    while fim:
        print("Estado da Pista:")
        print("1 - aberta")
        print("2 - fechada")
        
        try:
            opSubMenu = int(input("Opção: "))
            estado = opSubMenu
            fim = False
        except:
            print("Opção Inválida")

        if opSubMenu < 1 or opSubMenu > 2:
            fim = True
    

    if dificuldade == 1:
        dificuldade = "facil"
    elif dificuldade == 2:
        dificuldade = "intermedia"
    elif dificuldade == 3:
        dificuldade = "dificil"
    elif dificuldade == 4:
        dificuldade = "muitoDificil"


    if estado == 1:
        estado = "aberta"
    elif estado == 2:
        estado = "fechada"

    dataInsert = str(codigoPista) + '#' + str(nome) + '#' + str(zonaInicio) + '#' + str(zonaFim) + '#' + str(dificuldade) + '#' + str(estado) + '#'

    file = open('./data/tabelaPistas.txt', 'a')
    file.writelines(str(dataInsert) + '\n')
    file.close


    file = open('./data/tabelaSeccoes.txt', 'r')
    filedata = file.readlines()

    nSeccao = 1
    seccoesAssoc = []
    seccoes = []

    for line in filedata :
        dadosList = line.split("#")
        seccoes += [dadosList[0]]

    while True:

        if nSeccao > 1:
            seccaoAssociada = input("Secção " + str(nSeccao) + " ('fim' para sair): ")
            
            if (seccaoAssociada == "fim"):
                break
        else:
            seccaoAssociada = input("Secção " + str(nSeccao) + ": ")

        fim = True
        while fim:
            
            if seccaoAssociada in seccoes:
                fim = False
                seccoesAssoc += [seccaoAssociada]
            else:

                if nSeccao > 1:
                    seccaoAssociada = input("Secção " + str(nSeccao) + " ('fim' para sair): ")

                    if (seccaoAssociada == "fim"):
                        break
                else:
                    seccaoAssociada = input("Secção " + str(nSeccao) + ": ")

        if nSeccao > 1:
            if (seccaoAssociada == "fim"):
                break

        nSeccao += 1


    file = open('./data/tabelaSeccoesEmPistas.txt', 'a')
    
    for elem in seccoesAssoc:
        file.writelines(str(codigoPista) + "#" + str(elem) + "#" + '\n')

    file.close


def menuAlterarEstado():

    print("--- Mudar Estado ---")

    fim = True
    while fim:
        print("Alterar estado de:")
        print("1 - pista")
        print("2 - meio mecânico")
        
        try:
            opSubMenu = int(input("Opção: "))
            estadoDe = opSubMenu
            fim = False
        except:
            print("Opção Inválida")


    if opSubMenu < 1 or opSubMenu > 2:
        print("Opção Inválida")
        fim = True


    if estadoDe == 1:

        file = open('./data/tabelaPistas.txt', 'r')
        filedata = file.readlines()

        codigosPistas = []
        dadosList = ""
        for line in filedata :
            dadosList = line.split("#")
            codigosPistas += [dadosList[0]]

        codigo = input("Código da pista: ")

        fim = True
        while fim:
            
            if codigo in codigosPistas:
                fim = False
            else:
                codigo = input("Código da pista: ")


        lista = []
        dataInsert = ""

        for line in filedata :

            lista = line.split("#")

            if lista[0] == codigo:

                fim = True
                while fim:
                    print("Estado:")
                    print("1 - aberta")
                    print("2 - fechada")
                    
                    try:
                        opSubMenu = int(input("Opção: "))
                        estado = opSubMenu
                        fim = False
                    except:
                        print("Opção Inválida")

                    if opSubMenu < 1 or opSubMenu > 2:
                        fim = True

                if estado == 1:
                    estado = "aberta"
                elif estado == 2:
                    estado = "fechada"
                
                dataInsert += str(lista[0]) + "#" + str(lista[1]) + "#" + str(lista[2]) + "#" + str(lista[3]) + "#" + str(lista[4]) + "#" + str(estado) + "# \n"

            else:
                dataInsert += str(lista[0]) + "#" + str(lista[1]) + "#" + str(lista[2]) + "#" + str(lista[3]) + "#" + str(lista[4]) + "#" + str(lista[5]) + "# \n"


            file = open('./data/tabelaPistas.txt', 'w')
            file.writelines(dataInsert)
            file.close


    elif estadoDe == 2:

        file = open('./data/tabelaMeiosMecanicos.txt', 'r')
        filedata = file.readlines()

        NomeMM = []
        dadosList = ""
        for line in filedata :
            dadosList = line.split("#")
            NomeMM += [dadosList[0]]

        codigo = input("Nome do Meio Mecânico: ")

        fim = True
        while fim:
            
            if codigo in NomeMM:
                fim = False
            else:
                codigo = input("Nome do Meio Mecânico: ")


        lista = []
        dataInsert = ""

        for line in filedata :

            lista = line.split("#")

            if lista[0] == codigo:

                fim = True
                while fim:
                    print("Estado:")
                    print("1 - aberto")
                    print("2 - fechado")
                    
                    try:
                        opSubMenu = int(input("Opção: "))
                        estado = opSubMenu
                        fim = False
                    except:
                        print("Opção Inválida")

                    if opSubMenu < 1 or opSubMenu > 2:
                        fim = True

                if estado == 1:
                    estado = "aberto"
                elif estado == 2:
                    estado = "fechado"
                
                dataInsert += str(lista[0]) + "#" + str(lista[1]) + "#" + str(lista[2]) + "#" + str(estado) + "#" + str(lista[4]) + "# \n"

            else:
                dataInsert += str(lista[0]) + "#" + str(lista[1]) + "#" + str(lista[2]) + "#" + str(lista[3]) + "#" + str(lista[4]) + "# \n"
    

            file = open('./data/tabelaMeiosMecanicos.txt', 'w')
            file.writelines(dataInsert)
            file.close


def menuEmitirBilhete():

    print("--- Emitir Bilhete ---")
    
    def ref():

        caracteres = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",0,1,2,3,4,5,6,7,8,9]
        referencia = ""
        i = 0

        while i <= 9:
            referencia += str(caracteres[int(random.randint(0,35))])

            i += 1

        return referencia


    fim = True
    while fim:

        fim = False
        nomeCliente = input("Nome Cliente: ")
        numeros= ['0','1','2','3','4','5','6','7','8','9']
        for digito in nomeCliente:
            if digito in numeros:
                fim = True


    fim = True
    while fim:

        fim = False
        nacionalidade = input("Nacionalidade: ")
        numeros= ['0','1','2','3','4','5','6','7','8','9']
        for digito in nacionalidade:
            if digito in numeros:
                fim = True

    file = open('./data/tabelaTipoBilhete.txt', 'r')
    filedata = file.readlines()

    tiposBilhetes = []
    dadosList = ""
    for line in filedata :
        dadosList = line.split("#")
        tiposBilhetes += [dadosList[0]]

    tipoBilhete = input("Tipo Bilhete: ")

    fim = True
    while fim:
        
        if tipoBilhete in tiposBilhetes:
            fim = False
        else:
            tipoBilhete = input("Tipo Bilhete: ")


    fim = True
    while fim:

        date = datetime.datetime.now()
        
        try:
            dia = int(input("Dia: "))
            mes = int(input("Mês: "))
            ano = int(input("Ano: "))            
            fim = False
        except:
            print("Data invalida")

        if fim == False:
            if dia < 1 and dia > 31:
                fim = True

            if mes < 1 and mes > 12:
                fim = True

            if ano < 2023:
                fim = True

        if fim == True:
            print("Data invalida")
            
        if fim == False:

            if tipoBilhete == "d":

                diaFim = str(dia)
                mesFim = str(mes)
                anoFim = str(ano)

            elif tipoBilhete == "s":

                dateFim = str((datetime.datetime(ano, mes, dia) + datetime.timedelta(days=7)).date())
                dateFimSplit = []
                dateFimSplit = dateFim.split("-")
                diaFim = str(dateFimSplit[2])
                mesFim = str(dateFimSplit[1])
                anoFim = str(dateFimSplit[0])
                    
            elif tipoBilhete == "m":

                if int(mes + 1) == 13:
                    mes = 1

                diaFim = str(dia)
                mesFim = str(mes)
                anoFim = str(ano)

            elif tipoBilhete == "a":

                diaFim = str(dia)
                mesFim = str(mes)
                anoFim = str(ano + 1)


    dataInsert = str(ref()) + '#' + str(nomeCliente) + '#' + str(nacionalidade) + '#' + str(tipoBilhete) + '#' + str(dia) + '#' + str(mes) + '#' + str(ano) + '#' + str(diaFim) + '#' + str(mesFim) + '#' + str(anoFim) + '#'

    file = open('./data/tabelaBilhetes.txt', 'a')
    file.writelines(str(dataInsert) + '\n')
    file.close


def menuListagemBilhetes():

    print("--- Lista de Bilhetes Emitidos ---")

    file = open('./data/tabelaBilhetes.txt', 'r')
    filedata = file.readlines()

    nBilhete = 1

    for line in filedata :
        dadosList = line.split("#")

        print("Bilhete " + str(nBilhete) + ": " + str(dadosList[0]) + "  " + str(dadosList[1]) + "  " + str(dadosList[2]) + "  " + str(dadosList[3]) + 
        "   Valido de " + str(dadosList[4]) + "-" + str(dadosList[5]) + "-" + dadosList[6] + " até " + 
        str(dadosList[7]) + "-" + str(dadosList[8]) + "-" + str(dadosList[9]))
        
        nBilhete += 1


def menuListaBilheteDiaPeriodo():

    print("--- Lista de Bilhetes Emitidos por Periodo ---")

    print("Por favor, insira o período de dias para o qual deseja listar os bilhetes emitidos")
    print("Exemplo de formato: dd/mm/yyyy-dd/mm/yyyy")
    # período = input()

    fim1 = True
    while fim1:

        fim1 = False
        fim = True

        while fim:
            fim = False
            try:
                diaI = int(input("Dia Início: "))
            except:
                fim = True
                print("Dia invalido")

            if diaI > 31 or diaI < 1:
                fim = True

        fim = True
        while fim:
            fim = False
            try:
                mesI = int(input("Mes Início: "))
            except:
                fim = True
                print("Mes invalido")

            if mesI > 12 or mesI < 1:
                fim = True

        fim = True
        while fim:
            fim = False
            try:
                anoI = int(input("Ano Início: "))
            except:
                fim = True
                print("Ano invalido")

            if anoI < 2000 or anoI > 3000:
                fim = True

        fim = True
        while fim:
            fim = False
            try:
                diaF = int(input("Dia Início: "))
            except:
                fim = True
                print("Dia invalido")

            if diaF > 31 or diaF < 1:
                fim = True

        fim = True
        while fim:
            fim = False
            try:
                mesF = int(input("Mes Início: "))
            except:
                fim = True
                print("Mes invalido")

            if mesF > 12 or mesF < 1:
                fim = True

        fim = True
        while fim:
            fim = False
            try:
                anoF = int(input("Ano Início: "))
            except:
                fim = True
                print("Ano invalido")

            if anoF < 2000 or anoF > 3000:
                fim = True


    período = str(diaI) + "/" + str(mesI) + "/" + str(anoI) + "-" + str(diaF) + "/" + str(mesF) + "/" + str(anoF)


    data_início = período.split("-")[0]
    data_fim = período.split("-")[1]


    dia_início = data_início.split("/")[0]
    mês_início = data_início.split("/")[1]
    ano_início = data_início.split("/")[2]


    dia_fim = data_fim.split("/")[0]
    mês_fim = data_fim.split("/")[1]
    ano_fim = data_fim.split("/")[2]


    dia_início = int(dia_início)
    mês_início = int(mês_início)
    ano_início = int(ano_início)
    dia_fim = int(dia_fim)
    mês_fim = int(mês_fim)
    ano_fim = int(ano_fim)


    with open("./data/tabelaBilhetes.txt", "r") as bilhetes:
        for linha in bilhetes:
            elementos = linha.split("#")

            dia_início_bilhete = int(elementos[4])
            mês_início_bilhete = int(elementos[5])
            ano_início_bilhete = int(elementos[6])
            dia_fim_bilhete = int(elementos[7])
            mês_fim_bilhete = int(elementos[8])
            ano_fim_bilhete = int(elementos[9])

            if ano_início_bilhete > ano_início or (ano_início_bilhete == ano_início and mês_início_bilhete > mês_início) or (ano_início_bilhete == ano_início and mês_início_bilhete == mês_início and dia_início_bilhete >= dia_início):
                if ano_fim_bilhete < ano_fim or (ano_fim_bilhete == ano_fim and mês_fim_bilhete < mês_fim) or (ano_fim_bilhete == ano_fim and mês_fim_bilhete == mês_fim and dia_fim_bilhete <= dia_fim):

                    print("---------------------")
                    print("Referência do bilhete:", elementos[0])
                    print("Nome da pessoa:", elementos[1])
                    print("Nacionalidade:", elementos[2])
                    print("Tipo de bilhete:", elementos[3])
                    print("Data de início:",
                        elementos[4] + "/" + elementos[5] + "/" + elementos[6])
                    print("Data de fim:",
                        elementos[7] + "/" + elementos[8] + "/" + elementos[9])
        
    
def menuProcuraBilheteReferencia():

    print("--- Procura de Bilhetes por Referência ---")

    file = open('./data/tabelaBilhetes.txt', 'r')
    filedata = file.readlines()

    referencia = input("Referência Bilhete: ")

    encontrado = False
    
    for line in filedata:
        dadosList = line.split("#")
        if dadosList[0] == referencia:
            encontrado = True
            
            print("Referência: " + str(dadosList[0])) 
            print("Nome: " + str(dadosList[1]))
            print("Nacionalidade: " + str(dadosList[2]))
            print("Tipo: " + str(dadosList[3]))
            print("Data Início: " + str(dadosList[4]) + "-" + str(dadosList[5]) + "-" + str(dadosList[6]))
            print("Data Fim: " + str(dadosList[7]) + "-" + str(dadosList[8]) + "-" + str(dadosList[9]))

            consultarBilhetes(referencia)

    if encontrado == False:
        print("Bilhete não encontrado")


def menu():

    print("--- Menu ---")
    print("1 - Criar Zona")
    print("2 - Criar Comodidades")
    print("3 - Criar Secção")
    print("4 - Criar Meio Mecânico")
    print("5 - Criar Pista")
    print("6 - Alterar estado pistas/meio mecânico")
    print("7 - Emitir Bilhete")
    print("8 - Bilhetes Emitidos")
    print("9 - Procura Bilhete por periodo")
    print("10 - Procura Bilhete por referência")


    try:
        opMenu = int(input("Opção: "))
    except:
        print("\033[31mOpção Inválida!\033[m")
        menu()

    if (opMenu < 1 or opMenu > 10):
        print("\033[31mOpção Inválida!\033[m")
        menu()
    else:

        if (opMenu == 1):
            menuCriarZona()
            menu()
        elif (opMenu == 2):
            menuAdicionarComodidade()
            menu()
        elif (opMenu == 3):
            menuAdicionarSeccao()
            menu()
        elif (opMenu == 4):
            menuAdicionarMeioMecanico()
            menu()
        elif (opMenu == 5):
            menuAdicionarPista()
            menu()
        elif (opMenu == 6):
            menuAlterarEstado()
            menu()
        elif (opMenu == 7):
            menuEmitirBilhete()
            menu()
        elif (opMenu == 8):
            menuListagemBilhetes()
            menu()
        elif (opMenu == 9):
            menuListaBilheteDiaPeriodo()
            menu()
        elif (opMenu == 10):
            menuProcuraBilheteReferencia()
            menu()


menu()
