class CriterioEmprestimo():
    def __init__(
            self,
            fator_valor_maximo_emprestimo:float = 10.0,
            percentual_valor_prestacao: float = 0.30
        ):
        self._fator_valor_total_emprestimo = fator_valor_maximo_emprestimo
        self._percentual_valor_prestacao = percentual_valor_prestacao

    @property
    def fator_valor_maximo_emprestimo(self):
        return self._fator_valor_total_emprestimo

    @property
    def percentual_valor_prestacao(self):
        return self._percentual_valor_prestacao

    @property
    def criterios_default(self):
        return {
            'fator_valor_maximo_emprestimo': self.fator_valor_maximo_emprestimo,
            'percentual_valor_prestacao': self.percentual_valor_prestacao
        }

    def setar_atributo(
        self,
        fator_valor_total_emprestimo: float = None,
        percentual_valor_prestacao: float = None,
    ):
        lista_modificacoes = [
            ('fator_valor_total_emprestimo', fator_valor_total_emprestimo),
            ('percentual_valor_prestacao', percentual_valor_prestacao)
        ]
        for modificacao in lista_modificacoes:
            if modificacao[1] != None:
                setattr(self, f'_{modificacao[0]}', modificacao[1])
                print(
                    f'Atributo: "{modificacao[0]}", alterado com sucesso!' + 
                    f'\nNovo valor = {modificacao[1]}\n'
                )

    def permitir_emprestimo(
            self,
            renda_solicitante: float,
            prestacoes:int,
            emprestimo_solicitado:float
        ):
        if renda_solicitante > (self.fator_valor_maximo_emprestimo * renda_solicitante):
            print('\nEmpréstimo RECUSADO.\n' +
                f'O valor do emprestimo solicitado, é MAIOR que {self.fator_valor_maximo_emprestimo}x renda mensal\n')
            return False

        print(f'\nEmpréstimo no valor {emprestimo_solicitado} solicitado.' + 
            f'\nTotal de parcelas: {prestacoes}')
        valor_prestacao = emprestimo_solicitado/prestacoes
        valor_MAX_prestacao = renda_solicitante * (1 + self.percentual_valor_prestacao)
        if valor_prestacao > (renda_solicitante * (1 + self.percentual_valor_prestacao)):
            print(f'\nEmpréstimo RECUSADO.\n'+
                f'Valor maior {self.percentual_valor_prestacao} da renda mensal')
            return False

        print('\nEmpréstimo APROVADO!\n' +
            f'Detalhes do empréstimo:\nValor empréstimo: {emprestimo_solicitado}' +
            f'\nValor prestação: {round(valor_prestacao, 2)}\n')
        return True

# x = CriterioEmprestimo()
# #x.setar_atributo(2.5)
# setattr(x,'_fator_valor_total_emprestimo',3)
# print(x.criterios_default)