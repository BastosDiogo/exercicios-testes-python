class LeitorCNAB():

    def ler_cnab(self, caminho_cnab:str, criar_copia_cnab: bool = False):
        try:
            with open(caminho_cnab, mode='r') as leitura:
                # if len(leitura) == 0:
                #     print('O CNAB não contém nenhum informação')
                #     return False

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

    # def listar_empresas_cnab(self, caminho_cnab:str):
    #     linhas_arquivo_cnab = self.ler_cnab(caminho_cnab)
    #     if len(linhas_arquivo_cnab) == 0:
    #         return []

    #     operacoes = linhas_arquivo_cnab[1:-1]
    #     return [operacao[34:45] for operacao in operacoes]

    def lista_operacoes_cnab(self, caminho_cnab:str):
        linhas_arquivo_cnab = self.ler_cnab(caminho_cnab)
        if len(linhas_arquivo_cnab) == 0:
            return []

        operacoes = linhas_arquivo_cnab[1:-1]
        return [operacao[34:45] for operacao in operacoes]