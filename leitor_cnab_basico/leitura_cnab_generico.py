class LeitorCNAB():
    def __init__(
            self,
            qtd_posicoes_por_linhas:int,
            qtd_headers:int,
            qtd_trailers:int,
            caminho_cnab:str
        ):
        self._qtd_posicoes_por_linhas = int(qtd_posicoes_por_linhas)
        self._qtd_headers = int(qtd_headers)
        self._qtd_trailers = int(qtd_trailers)
        self._caminho_cnab = str(caminho_cnab)

    @property
    def posicoes_por_linhas(self):
        return self._qtd_posicoes_por_linhas

    @property
    def headers_cnab(self):
        return self._qtd_headers

    @property
    def trailers_cnab(self):
        return self._qtd_trailers

    @property
    def caminho_cnab(self):
        return self._caminho_cnab

    @property
    def configuracoes_atuais_do_leitor(self):
        return {
            'qtd_linhas': self.posicoes_por_linhas,
            'qtd_headers': self.trailers_cnab,
            'qtd_trailers':self.headers_cnab,
            'caminho_cnab': self.caminho_cnab
        }


    def ler_cnab(self, criar_copia_cnab: bool = False):
        try:
            with open(self.caminho_cnab, mode='r') as leitura:
                if criar_copia_cnab == True:
                    with open('copia_cnab.txt', 'w+') as arquivo:
                        arquivo.seek(0)
                        for linha in leitura:
                            arquivo.writelines(linha)

                linhas_arquivo_cnab = []
                for linha in leitura:
                    linhas_arquivo_cnab.append(linha.replace('\n',''))
                
            return linhas_arquivo_cnab

        except Exception as erro:
            print(f'O seguinte erro foi encontado:\n{erro}.')
            return []

    def lista_operacoes_cnab(self):
        linhas_arquivo_cnab = self.ler_cnab(self.caminho_cnab)
        if len(linhas_arquivo_cnab) == 0:
            return []

        operacoes = linhas_arquivo_cnab[self.headers_cnab:-(self.trailers_cnab)]
        return [operacao for operacao in operacoes]

    def buscar_campos_operacoes(self, posicao_inicial:int, posicao_final:int):
        posicao_inicial = 0 if (int(posicao_inicial) - 1) <= 0 else int(posicao_inicial) - 1
        posicao_final   = 0 if (int(posicao_final) - 1) <= 0 else int(posicao_final)

        lista_operacoes = self.lista_operacoes_cnab()

        return [ operacao[posicao_inicial:posicao_final] for operacao in lista_operacoes ]


    # def listar_empresas_cnab(self, caminho_cnab:str):
    #     linhas_arquivo_cnab = self.ler_cnab(caminho_cnab)
    #     if len(linhas_arquivo_cnab) == 0:
    #         return []

    #     operacoes = linhas_arquivo_cnab[1:-1]
    #     return [operacao[34:45] for operacao in operacoes]

qtd_headers = 50
qtd_headers = 1
qtd_trailers = 1
path = 'leitor_cnab_basico\cnab.txt'

x = LeitorCNAB(qtd_headers, qtd_headers, qtd_trailers,path)
x.ler_cnab(True)
operacoes = x.lista_operacoes_cnab()
campo_buscado = x.buscar_campos_operacoes(35,45)
print(f'Lista: {operacoes}\nTamanho de uma operação: {len(operacoes[0])}')
print(f'Lista campos buscado:\n{campo_buscado}')
