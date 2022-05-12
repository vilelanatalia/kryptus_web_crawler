import requests 
from bs4 import BeautifulSoup
import json 

def createJson(datas):
    json_object = json.dumps(datas, indent = 4, ensure_ascii=False)
    with open("datas.json", "w", encoding='utf8') as outfile:
        outfile.write(json_object)

def hasFreeShipping(string_text):
    try:
        string_text.text
        return True
    except:
        return False

def processStoreName(string_text):
    try:
        new_string = string_text.text.split(' ')
        del(new_string[0])
        return ' '.join(new_string)
    except:
        return "NOME_DA_LOJA_NAO_FORNECIDO"

def convertFloat(string_value):
    return float(string_value)

def processPriceValue(string_text):
    try:
        new_string = string_text.replace("R$", ",").split(',')
        del(new_string[0])
        return convertFloat(new_string[0]+ '.'+ new_string[1])
    except:
        return 0.0

def processAmountParcel(string_text):
    new_string = string_text.replace("em", "x").split('x')
    return convertFloat(new_string[1])

def parcelValue(valueParcel, amountParcel ):
    valueTotal = valueParcel * amountParcel
    return valueTotal


response = requests.get('https://lista.mercadolivre.com.br/tenis-nike')
mercadoLivre = BeautifulSoup(response.text, 'html.parser')


def getProduct(search_link):
    dados = []
    products = search_link.find_all('div', attrs={'class': 'ui-search-result__wrapper'})

    for product in products:
        price = product.find('span', attrs={'class': 'price-tag ui-search-price__part'}) 
        free_shipping = product.find('p', attrs={'class': 'ui-search-item__shipping ui-search-item__shipping--free'}) 
        store_name = product.find('p', attrs= {'class': 'ui-search-official-store-label ui-search-item__group__element ui-search-color--GRAY'}) #ok
        product_name = product.find('h2', attrs= {'ui-search-item__title ui-search-item__group__element'}) 
        amount_value = product.find('div', attrs = {'ui-search-item__group ui-search-item__group--price'})
        parcel_value = product.find_all('div', attrs = {'ui-search-price__second-line'}) 
        product_link = product.find('a', attrs={'class': 'ui-search-result__content ui-search-link'}) 
        product_code = product.find('input', attrs = {'name': 'itemId'})
        product_image = product.find('img', attrs = {'width': '284'})

        valueParcel = processPriceValue(parcel_value[1].text)
        amountParcel = processAmountParcel(amount_value.text)

        dado = { 

            'valor': processPriceValue(price.text),
            'valor_parcelado': parcelValue(valueParcel, amountParcel),
            'nome_produto': product_name.text,
            'foto': product_image['data-src'],
            'frete_gratis': hasFreeShipping(free_shipping),
            'nome_loja': processStoreName(store_name),
            'link_produto': product_link['href'],
            'codigo_produto': product_code['value']
     
        
        }
        dados.append(dado)
    return dados


createJson(getProduct(mercadoLivre))
