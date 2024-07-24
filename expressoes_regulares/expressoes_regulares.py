import re


"""Exemplo 1 - Busca padrão 'ar' e qq cois no meio porém 'ra' no fim. """
texto = 'arxYzra'
# Cada '.' representa um caracter qualquer.
padrao = re.compile('ar...ra') # Nesse caso é um '.' para o x, um para Y e um para o z
busca = padrao.findall(texto)
print('Exemplo 1:', busca)

padrao_2 = re.compile(r'.ra') # Nesse caso texto que FINALIZE com 'ra'. Podendo ser qq coisa antes.
busca_2 = padrao_2.findall(texto)
print('Exemplo 1.1:', busca_2)

"""Exemplo 2 - Busca padrão que inicie com 'ar' POUCO importanto o restante."""
texto = 'arxxxx45123///ra'
padrao = re.compile(r'^a.')
busca = padrao.findall(texto)
print('Exemplo 2:', busca)

"""Exemplo 3 - Busca padrão que NÃO TENHA 'ar' POUCO importanto o restante."""
texto = 'arxxxx45123///ra'
padrao = re.compile(r'[^ar]')
busca = padrao.findall(texto)
print('Exemplo 3:', busca)

titulo = """Exemplo 4 - Busca padrão que SEJA algarismos de 0 a 9."""
## Busca SENDO algarismos de 0 a 9:
exemplo = list(zip(re.compile(r'Exemplo 4').findall(titulo)))[0][0]
texto = 'ar/23//56ra49'
padrao = re.compile(r'\d') # Buscar algorismos de 0 a 9
busca = padrao.findall(texto)
print(exemplo + ':', busca)


"""Exemplo 5 - Busca padrão que NÃO algarismos de 0 a 9."""
texto = 'arxxxx45123///ra'
padrao = re.compile(r'\D') # Busca algorismo que NÃO sejam de 0 a 9.
busca = padrao.findall(texto)
print('Exemplo 5:', busca)


"""Exemplo 6 - Busca padrão que NÃO seja carecter vazio."""
texto = """

arara1992

"""
padrao = re.compile(r'\s') # Busca caracter que NÃO seja vazio.
busca = padrao.findall(texto)
print('Exemplo 6:', busca)


"""Exemplo 7 - Busca padrão que SEJA carecter vazio."""
texto = """

arara 1992

"""
padrao = re.compile(r'\S') # Busca caracter que SEJA vazio.
busca = padrao.findall(texto)
print('Exemplo 7:', busca)


"""Exemplo 8 - Busca padrão que SEJA alfanumérico"""
texto = """

@arara_1992@

"""
padrao = re.compile(r'\w') # Busca caracter que SEJA alfanumerico
busca = padrao.findall(texto)
print('Exemplo 8:', busca)


"""Exemplo 9 - Busca padrão que NÃO seja alfanumérico"""
texto = """

@arara_1992@

"""
padrao = re.compile(r'\W') # Busca caracter que NÃO seja alfanumerico.
busca = padrao.findall(texto)
print('Exemplo 9:', busca)
'MINUTAGEM 28'
"Link do video = https://www.youtube.com/watch?v=Jao4VwJCByk"