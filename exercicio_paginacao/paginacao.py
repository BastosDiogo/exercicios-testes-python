
def get_pagination(items:list, page_size:int):
    if not isinstance(items, list):
        return Exception('Erro: Dados de entrada não estão no formato de lista.')

    page_size = int(page_size) if not isinstance(page_size, int) else page_size
    max_sub = int(len(items)/page_size)
    resposta = []
    step = 0
    while len(resposta) < max_sub:
        i = step
        f = i + page_size
        e = items[i:f]
        resposta.append(e)

        step += page_size
    return resposta


items = ['a','b','c','d']
x = get_pagination(items,2)
print(x)


if __name__ == '__main__':
    lista_teste = ['a','b','c','d','e','f']
    page_size = 4
    paginacao = get_pagination(lista_teste,page_size)
    print(paginacao)