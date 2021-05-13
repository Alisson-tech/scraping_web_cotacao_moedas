from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
'''
webdrive:
Google chrome - chromedriver
'''
#abrir o navegador
navegador = webdriver.Chrome(executable_path='webdriver/chromedriver.exe')

#entrar no google
navegador.get('https://www.google.com/')

#DOLAR
#Os elementos da pagina estão sendo identificados pelo xpath
#Digitar "Cotaçao do dolar"
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Cotação Dolar')

#apertar a tecla 'enter'
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)

#Obter o data-value do elemento
dolar = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

#------------------------

#EURO
#entrar no google
navegador.get('https://www.google.com/')

#Os elementos da pagina estão sendo identificados pelo xpath
#Digitar "Cotaçao do dolar"
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Cotação Euro')

#apertar a tecla 'enter'
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)

#Obter o data-value do elemento
euro = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

#OURO
#entrar no melhorcambio
navegador.get('https://www.melhorcambio.com/ouro-hoje')

#Os elementos da pagina estão sendo identificados pelo xpath

#Obter o data-value do elemento
ouro = navegador.find_element_by_xpath('//*[@id="comercial"]').get_attribute('value')
ouro = ouro.replace(',', '.')
print(dolar, euro, ouro)

#fecahr navegador
navegador.quit()

dados = pd.read_excel('Produtos.xlsx')

#Ataulizar a Cotação das moedas
#                  linha          |  Coluna
dados.loc[dados['Moeda']=='Dólar', 'Cotação'] = float(dolar)
dados.loc[dados['Moeda']=='Euro', 'Cotação'] = float(euro)
dados.loc[dados['Moeda']=='Ouro', 'Cotação'] = float(ouro)

#Atualizar a preço de base reais
dados['Preço Base Reais'] = dados['Cotação'] * dados['Preço Base Original']

#Atualizar Preço Final

dados['Preço Final'] = (dados['Preço Base Reais'] * dados['Ajuste']).map('{:.2f}'.format)
dados['Cotação'].map('{:.2f}'.format)
dados['Preço Base Reais'].map('{:.2f}'.format)

dados.to_excel('Produtos_Atualizado.xlsx')