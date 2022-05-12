from bs4 import BeautifulSoup
import requests 
import util
from webScrapingApplication import getProduct

###MAIN
search = input("Insira o nome do produto: \n")

response = requests.get('https://lista.mercadolivre.com.br/'+search)
mercadoLivre = BeautifulSoup(response.text, 'html.parser')

util.createJson(getProduct(mercadoLivre))
