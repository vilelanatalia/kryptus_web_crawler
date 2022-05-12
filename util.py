from bs4 import BeautifulSoup
import json 

def createJson(datas):
    json_object = json.dumps(datas, indent = 4, ensure_ascii=False)
    with open("datas.json", "w", encoding='utf8') as outfile:
        outfile.write(json_object)

def hasFreeShipping(string_text):
    '''Verifica se a loja possui frete gratis'''
    try:
        string_text.text
        return True
    except:
        return False

def processStoreName(string_text):
    '''Trata o dado bruto do nome da loja, retornando apenas o nome da loja para o arquivo json'''
    try:
        new_string = string_text.text.split(' ')
        del(new_string[0])
        return ' '.join(new_string)
    except:
        return "NOME_DA_LOJA_NAO_FORNECIDO"

def processPriceValue(string_text):
    '''Trata o dado bruto de preços, retirando da string valores não interessantes e convertendo-o para o tipo float'''
    try:
        new_string = string_text.replace("R$", ",").split(',')
        del(new_string[0])
        return float(new_string[0]+ '.'+ new_string[1])
    except:
        return 0.0

def processAmountParcel(string_text):
    '''Trata o dado bruto do numero de parcela, retirando da string valores não interessantes e convertendo-o para o tipo float'''
    new_string = string_text.replace("em", "x").split('x')
    return float(new_string[1])

def parcelValue(valueParcel, amountParcel ):
    '''Multiplica o valor da parcela e a quantidade de parcelas para retornar o valor total da parcela'''
    valueTotal = valueParcel * amountParcel
    return valueTotal
