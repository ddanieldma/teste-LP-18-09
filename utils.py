def recebe_data(datas: str) -> list:
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
    datas_list = datas.split("-")
    datas_list = datas_list.split(" ")
    datas_list_2 = []
    for data in datas_list:
        datas_list_2.append(data.split(" "))

    dia_inicio = datas_list_2[0][0]
    dia_fim = datas_list_2[1][0]

    mes_inicio = datas_list_2[0][2].lower()
    mes_fim = datas_list_2[1][2].lower()

    # verificando se o mes existe
    if not any((mes in mes_inicio for mes in meses.keys) or (mes in mes_fim for mes in meses)):
        raise TypeError

    # convertendo mes para numero
    mes_inicio = meses[mes_inicio]
    mes_fim = meses[mes_fim]

    ano_inicio = datas_list_2[0][4]
    ano_fim = datas_list_2[1][4]

    if((dia_inicio < 0 or dia_inicio > 31) or 
       (dia_fim < 0 or dia_inicio > 31) ):
        raise TypeError
    elif((mes_inicio < 0 or mes_inicio > 12) or 
       (mes_fim < 0 or mes_inicio > 12) ):
        raise TypeError
    elif((ano_inicio < 0) or 
       (ano_fim < 0)):
        raise TypeError
    
    return [dia_inicio, dia_fim, mes_inicio, mes_fim, ano_inicio, ano_fim]
        
    
