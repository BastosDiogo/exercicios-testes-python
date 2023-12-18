from itertools import combinations

def arrey_targersum(arrey:list,agrupamentos:int ,targerSum:int):
    def combinacao_elementos(lista_elementos:list, agrupamentos:int):
        comb = combinations(lista_elementos, agrupamentos)
        return list(comb)
    
    lista_resposta = []
    combinacoes_arrey = combinacao_elementos(arrey, agrupamentos)
    for combinacao in combinacoes_arrey:
        combinacao_em_lista = [elemento for elemento in combinacao]
        if sum(combinacao_em_lista) == targerSum:
            combinacao_em_lista.sort()
            lista_resposta.append(combinacao_em_lista)

    lista_resposta.sort()
    return lista_resposta

lista_teste = [12,3,1,2,-6,5,-8,6]
_agrupamentos = 3
_targerSum = 0
resutado = arrey_targersum(lista_teste, _agrupamentos, _targerSum)
print(resutado)

# Ref: https://www.uel.br/projetos/matessencial/basico/medio/combinat.html#:~:text=Combina%C3%A7%C3%A3o%20simples%3A%20N%C3%A3o%20ocorre%20a,(m%E2%88%92p)!
# Ref_combinacoes: https://www.acervolima.com.br/2020/12/permutacao-e-combinacao-em-python.html