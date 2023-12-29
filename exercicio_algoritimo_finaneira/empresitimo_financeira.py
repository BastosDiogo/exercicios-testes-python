from criterios import CriterioEmprestimo

renda_mensal_do_solicitante = 1000
prestacoes = 12
emprestimo_solicitado = 1000

emprestimo = CriterioEmprestimo()
print(f'Critérios de avaliação do empréstimo:\n{emprestimo.criterios_default}')

aprovacao_emprestimo = emprestimo.permitir_emprestimo(
    renda_mensal_do_solicitante,
    prestacoes,
    emprestimo_solicitado
)
