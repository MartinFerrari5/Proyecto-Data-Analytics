import requests
from bs4 import BeautifulSoup

"""
SCRAPPING DEL VALOR DEL DOLAR (VALOR PROMEDIO DEL DOLAR OFICIAL EN ARGENTINA POR AÑO)
"""

# URL dolar
dolar_url = requests.get("https://www.dineroeneltiempo.com/divisas/usd-ars/historico").text
dolar_html = BeautifulSoup(dolar_url,"html.parser")
dolar_html= dolar_html.find_all("tr",class_="hover:bg-gray-100")
def dolar():
    dolar_valor = {}
    for registro in dolar_html:
        registro = registro.get_text().split()
        dolar_valor[registro[0]] = registro[3]
        if(registro[0]=="2014"):
            break
    return dolar_valor

