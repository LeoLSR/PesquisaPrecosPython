
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from verificacao import *
def busca_google_shopping(nav,produto, termos_banidos, preco_minimo, preco_maximo):
    produto = produto.lower()
    termos_banidos = termos_banidos.lower()
    lista_termos_banidos = termos_banidos.split(" ")
    lista_termos_nome_produto = produto.split(" ")
    lista_de_produtos = []
    preco_minimo = float(preco_minimo)
    preco_maximo = float(preco_maximo)

    nav.get("https://shopping.google.com.br/")

    nav.find_element('xpath', '/html/body/c-wiz[1]/div/div/c-wiz/form/div[2]/div[1]/input').send_keys(produto,
                                                                                                      Keys.ENTER)
    sleep(5)

    lista_resultados = nav.find_elements(By.CLASS_NAME, "i0X6df")

    for resultado in lista_resultados:

        # se o preco ta entre preco_minimo e preco_maximo
        nome = resultado.find_element(By.CLASS_NAME, "tAxDx").text
        nome = nome.lower()

        # Analistar se ele não tem nehum termo banido
        tem_termos_banidos = verificar_tem_termos_banidos(lista_termos_banidos,nome)

        # Analista se ele tem todos os termos do produto
        tem_todos_termos_produtos = verificar_tem_todos_produtos(lista_termos_nome_produto,nome)


        # Selecionar só os elmentos que tem os tem_termos_anidos = False e ao mesmo tempo tem todos True

        if not tem_termos_banidos and tem_todos_termos_produtos:
            preco = resultado.find_element(By.CLASS_NAME, "a8Pemb").text
            preco = preco.replace("R$", "").replace(" ", "").replace(".", "").replace(",", ".")
            preco = float(preco)


            if preco_minimo <= preco <= preco_maximo:
                elemento_refrencia = resultado.find_element(By.CLASS_NAME, 'bONr3b')
                elemento_pai = elemento_refrencia.find_element(By.XPATH, '..')
                link = elemento_pai.get_attribute('href')

                lista_de_produtos.append((nome, preco, link))

    return lista_de_produtos