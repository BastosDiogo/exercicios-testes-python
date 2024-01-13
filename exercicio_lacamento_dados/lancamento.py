from itertools import permutations


class LancarmentoDado():
    def __init__(self, qtd_faces:int=6 , qtd_dados_lancados:int=2) -> None:
        if int(qtd_faces) < 4:
            print(
                f'{qtd_faces} Não é um valor válido para quantidade de faces.',
                'Será utilizado 4 no lugar.', sep='\n'
            )
        if int(qtd_dados_lancados) < 2:
            print('A quantidade mínima de dados deve ser 2. Esse valor será utilizado no lugar.')
        self._qtd_faces = 4 if int(qtd_faces) < 6 else int(qtd_faces)
        self._qtd_dados_lancados = int(qtd_dados_lancados) if int(qtd_dados_lancados) > 2 else 2

    @property
    def qtd_faces(self):
        return self._qtd_faces

    @property
    def dados_lancados(self):
        """Quantiddade de dados lançados"""
        return self._qtd_dados_lancados

    @property
    def combinacoes_possiveis(self):
        setp = 1
        valores_do_dado = []
        valor_dado = self.qtd_faces
        while valor_dado > 0:
            valores_do_dado.append(valor_dado)
            valor_dado -= setp

        combinacoes = list(permutations(valores_do_dado, self.dados_lancados))
        return combinacoes

    def combinacoes_possiveis_para_um_dado_valor(self, valor_alvo:int):
        if valor_alvo == 0:
            raise ValueError(self.__repr__())

        #valor_alvo = int(valor_alvo)
        #combinacoes = self.combinacoes_possiveis

        return [
            cobinacao for cobinacao in self.combinacoes_possiveis if sum(
                [cobinacao[index] for index in range(0, len(cobinacao))]
            ) == int(valor_alvo)
        ]


    def __str__(self) -> str:
        return f'Dado de {self.qtd_faces} faces.'


    def __repr__(self, tipo_mensagem:str = '0') -> str:
        erros = {'0': 'O valor alvo deve ser diferente de zero.'}
        return erros[tipo_mensagem]

x = LancarmentoDado()
print(x.combinacoes_possiveis_para_um_dado_valor(12))