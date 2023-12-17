from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# Navegar até a URL
driver.get("https://www.google.com.br/search?q=Iphone+12+64gb&sca_esv=591329734&tbm=shop&source=lnms&biw=1024&bih=1145&dpr=1#spd=0")

'''produto = "Iphone 12 64gb"
driver.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys(produto,Keys.ENTER)
'''
sleep(5)
# Obtém todos os elementos disponiveis com o nome da tag 'p'
elements = driver.find_elements(By.CLASS_NAME, 'kHxwFf')

for e in elements:
    print(e.text)
