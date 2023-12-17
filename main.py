from selenium import webdriver
from googleShopping import busca_google_shopping
import pandas as pd
from buscapePesquisa import busca_buscape

tabela_produtos = pd.read_excel('buscas.xlsx')

nav = webdriver.Chrome()

tabela_ofertas = pd.DataFrame()

for linha in tabela_produtos.index:
    produto = tabela_produtos.loc[linha, 'Nome']
    termos_banidos = tabela_produtos.loc[linha, 'Termos banidos']
    preco_minimo = tabela_produtos.loc[linha, 'Preço mínimo']
    preco_maximo = tabela_produtos.loc[linha, 'Preço máximo']

    lista_offertas_google_shopping = busca_google_shopping(nav, produto, termos_banidos, preco_minimo, preco_maximo)
    if lista_offertas_google_shopping:
        tabela_google_shopping = pd.DataFrame(lista_offertas_google_shopping, columns=['produto', 'preco', 'link'])
        tabela_ofertas = pd.concat([tabela_ofertas, tabela_google_shopping])
    else:
        tabela_google_shopping = None
    listas_ofertas_buscape = busca_buscape(nav, produto, termos_banidos, preco_minimo, preco_maximo)
    if listas_ofertas_buscape:
        tabela_ofertas_buscape = pd.DataFrame(listas_ofertas_buscape, columns=['produto', 'preco', 'link'])
        tabela_ofertas = pd.concat([tabela_ofertas, tabela_ofertas_buscape])
    else:
        tabela_ofertas_buscape = None

print(tabela_ofertas)

tabela_ofertas.to_excel('produtos.xlsx', index=False)

print('tudo ok!')
