import requests 
from bs4 import BeautifulSoup
import json 


search = input('Digite o termo da sua pesquisa')
url_search = 'https://lista.mercadolivre.com.br/' + search
response = requests.get(url_search)
mercadoLivre = BeautifulSoup(response.text, 'html.parser')


def getProduct(search_link):
    produtos = search_link.find_all('div', attrs={'class': 'ui-search-result__wrapper'})

    for produto in produtos:
        preco = produto.find('span', attrs={'class': 'price-tag ui-search-price__part'}) #ok
        frete_gratis = produto.find('p', attrs={'class': 'ui-search-item__shipping ui-search-item__shipping--free'}) #ok
        nome_loja = produto.find('p', attrs= {'class': 'ui-search-official-store-label ui-search-item__group__element ui-search-color--GRAY'}) #ok
        nome_produto = produto.find('h2', attrs= {'ui-search-item__title ui-search-item__group__element'}) #ok
        numero_parcela = produto.find('span', attrs = {'ui-search-item__group__element ui-search-installments ui-search-color--LIGHT_GREEN'})
        valor_parcelado = produto.find_all('div', attrs = {'ui-search-price__second-line'}) #ok tem que puxar na posicao correta
        link_produto = produto.find('a', attrs={'class': 'ui-search-result__content ui-search-link'}) #okok
        codigo_produto = produto.find('input', attrs = {'name': 'itemId'}) #OKPORRA

    
        dados = { 

            'preco': preco.text,
            # 'frete_gratis': hasFreteGratis(frete_gratis),
            # 'nome_loja': hasLoja(nome_loja),
            'nome_produto': nome_produto.text,
            'numero_parcela': numero_parcela.text,
            'valor_parcelado': valor_parcelado[1].text,
            'link_produto': link_produto['href'],
            'codigo_produto': codigo_produto['value']
        
        }
    return dados


print(getProduct(mercadoLivre))