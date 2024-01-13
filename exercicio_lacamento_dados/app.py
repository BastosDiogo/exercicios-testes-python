from lancamento import LancarmentoDado
import time


qtd_faces_dado = input('Digite a quantas FACES cada dado lançado possui:\n-> ')
qtd_dados_lancados = input('Digite a quantidade de DADOS lançados:\n-> ')

lancamento = LancarmentoDado(
    qtd_faces_dado.replace('-> ',''),
    qtd_dados_lancados.replace('-> ','')
)

valor_alvo = input('Ótimo!Agora digite o valor alvo desejado:\n-> ')
print('\nCalculando...')
combinacoes_possiveis = (
    lancamento.combinacoes_possiveis_para_um_dado_valor(valor_alvo.replace('-> ',''))
)
time.sleep(1)

if len(combinacoes_possiveis) == 0:
    print('Não há combinações possíveis para esse valor alvo.\n')

else:
    print('As possíveis combinações são:')
    for combinacao in combinacoes_possiveis:
        print(f'Valor de cada dado: {combinacao}. Soma = {valor_alvo}')
