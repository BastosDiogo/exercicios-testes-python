def string_balanceada(string:str):
    gabarito = {
        'parentenses':{'aberto': '(', 'fechado':')'},
        'chaves':{'aberto': '{', 'fechado':'}'},
        'colchetes':{'aberto': '[', 'fechado':']'},
    }    
    elementos = {chave: {'aberto': [], 'fechado':[]} for chave in gabarito}

    for elemento in string:
        for chave in elementos.keys():
            if elemento == gabarito[chave]['aberto']:
                elementos[chave]['aberto'].append(elemento)

            if elemento == gabarito[chave]['fechado']:
                elementos[chave]['fechado'].append(elemento)

    avaliacao = []
    for _elemento in elementos:
        if len(elementos[_elemento]['aberto']) == len(elementos[_elemento]['fechado']):
            avaliacao_elemento = True
        else:
            avaliacao_elemento = False
        avaliacao.append(avaliacao_elemento)

    return False if False in avaliacao else True