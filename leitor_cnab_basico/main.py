from  leitura_cnab import LeitorCNAB

caminho_cnab = 'leitor_cnab_basico\cnab.txt'
leitor_cnab = LeitorCNAB()
#leitor_cnab.ler_cnab(caminho_cnab)
listar_empresas_cnab = leitor_cnab.listar_empresas_cnab(caminho_cnab)
print(listar_empresas_cnab)
