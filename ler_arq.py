def arq_txt():
    nome_arq = input("Nome do arquivo.txt: ")

    with open(nome_arq, "r") as arquivo:
        linhas = arquivo.readlines()

    meses = {
    "janeiro": 1,
    "fevereiro": 2,
    "março": 3,    
    "abril": 4,
    "maio": 5,
    "junho": 6,
    "julho": 7,
    "agosto": 8,
    "setembro": 9,
    "outubto": 10,
    "novembro": 11,
    "dezembro": 12,
    }
    
    # separando cada elemento das datas em strings
    datas_list = linhas[0].split("-")
    datas_list = datas_list.split(" ")
    datas_list_2 = []
    for palavras in datas_list:
        datas_list_2.append(palavras.split(" "))

    dia_inicio = datas_list_2[0][0]
    dia_fim = datas_list_2[1][0]

    mes_inicio = datas_list_2[0][2].lower()
    mes_fim = datas_list_2[1][2].lower()

    # convertendo mes para numero
    mes_inicio = meses[mes_inicio]
    mes_fim = meses[mes_fim]

    ano_inicio = datas_list_2[0][4]
    ano_fim = datas_list_2[1][4]

    
    return [dia_inicio, dia_fim, mes_inicio, mes_fim, ano_inicio, ano_fim]
        

print(arq_txt())