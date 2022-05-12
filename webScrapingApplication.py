
import util


def getProduct(search_link):
    '''Método principal, busca pelos elementos, ainda brutos, no html da página e depois recebe o
    refinamento de dados para serem agrupados em uma array '''
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

        
        valueParcel = util.processPriceValue(parcel_value[1].text)
        amountParcel = util.processAmountParcel(amount_value.text)

        dado = { 

            'valor': util.processPriceValue(price.text),
            'valor_parcelado': util.parcelValue(valueParcel, amountParcel),
            'nome_produto': str(product_name.text),
            'foto': product_image['data-src'],
            'frete_gratis': util.hasFreeShipping(free_shipping),
            'nome_loja': util.processStoreName(store_name),
            'link_produto': product_link['href'],
            'codigo_produto': product_code['value']
     
    
        }
        dados.append(dado)
    return dados
