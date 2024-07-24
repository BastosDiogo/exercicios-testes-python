from lancamento import LancarmentoDado
import pytest


class TestClass():

    def test_Faz_qtd_faces_igual_a_4_quando_numero_de_faces_do_dado_MENOR_que_4(self):
        """Testa se a quantidade de faces do dado é MENOR que 4. Se sim, retornar um Erro
        e automaticamente força a quatidade de faces do dado igual 4.
        """
        entrada = 3
        saida_esperada = 4

        "Avaliação"
        lance_teste = LancarmentoDado(entrada)
        resultado = lance_teste.qtd_faces

        assert resultado == saida_esperada


    def test_Faz_qtd_faces_igual_a_4_quando_numero_de_faces_do_dado_MENOR_que_4_VALORES_NEGATIVOS_(self):
        """Testa se a quantidade de faces do dado é MENOR que 4. Se sim, retornar um Erro
        e automaticamente força a quatidade de faces do dado igual 4.
        """
        entradas = ([valor for valor in range(0, 4)] + [-valor for valor in range(1, 4)])
        saida_esperada = 4

        "Avaliação"
        for entrada in entradas:
            lance_teste = LancarmentoDado(entrada)
            resultado = lance_teste.qtd_faces
            assert resultado == saida_esperada


    def test_Faz_qtd_dados_lancados_igual_a_2_quando_qtd_de_dados_lancados_MENOR_que_2(self):
        """Testa se a qtd de dados lançados é MENOR que 2.
        Se sim, força o valor a ser igual a 2.
        """
        entrada = 0
        saida_esperada = 2

        "Avaliação"
        lance_teste = LancarmentoDado(qtd_dados_lancados=entrada)
        resultado = lance_teste.dados_lancados

        assert resultado == saida_esperada


###OBS.:
"""
Sempre que for rodar via terminal, digitar "pytest -v" ou "pytest -m  <decoretor>"
Para ver  questão dos marks, veja:
    https://cursos.alura.com.br/course/python-tdd-explorando-testes-unitarios/task/110693

"""