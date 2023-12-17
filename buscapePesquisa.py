from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from googleShopping import busca_google_shopping
from verificacao import verificar_tem_termos_banidos, verificar_tem_todos_produtos


def busca_buscape(nav, produto, termos_banidos, preco_minimo, preco_maximo):
    produto = produto.lower()
    termos_banidos = termos_banidos.lower()
    lista_termos_banidos = termos_banidos.split(" ")
    lista_termos_nome_produto = produto.split(" ")
    lista_de_produtos = []
    preco_minimo = float(preco_minimo)
    preco_maximo = float(preco_maximo)
    nav.get('https://www.buscape.com.br/')
    nav.find_element(by=By.XPATH,
                     value='/html/body/div[1]/main/header/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/input').send_keys(
        produto,
        Keys.ENTER)

    while len(nav.find_elements(By.CLASS_NAME, 'HitsPerPage_HitsPerPageWrapper__8HEd9')) < 1:
        sleep(1)

    lista_resultados = nav.find_elements(By.CLASS_NAME, 'ProductCard_ProductCard_Inner__gapsh')

    for resultado in lista_resultados:
        preco = resultado.find_element(By.CLASS_NAME, 'Text_MobileHeadingS__HEz7L').text
        nome = resultado.find_element(By.CLASS_NAME, 'ProductCard_ProductCard_Name__U_mUQ').text
        nome = nome.lower()
        link = resultado.get_attribute('href')

        tem_termos_banidos = verificar_tem_termos_banidos(lista_termos_banidos, nome)

        # Analista se ele tem todos os termos do produto
        tem_todos_termos_produtos = verificar_tem_todos_produtos(lista_termos_nome_produto, nome)

        if not tem_termos_banidos and tem_todos_termos_produtos:

            preco = preco.replace("R$", "").replace(" ", "").replace(".", "").replace(",", ".")
            preco = float(preco)
            if preco_minimo <= preco <= preco_maximo:
                lista_de_produtos.append((nome, preco, link))
    return lista_de_produtos
