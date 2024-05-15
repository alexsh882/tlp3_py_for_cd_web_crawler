import requests 
from bs4 import BeautifulSoup
import json

url = 'https://www.xn--lamaanaonline-lkb.com.ar'


def get_all_a_from_url() -> list[str]:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    a = soup.find_all('a', class_="nav-link", attrs={'href': True})
    return a

def get_all_links() -> list[str]:
    a = get_all_a_from_url()
    links = []
    for link in a:
        if link['href'] != url and link['href'].find('#') != 0:
            links.append(link['href'])
    return links

def get_data_from_links():
    links = get_all_links()
    data = {}
    totalLinksLen = len(links)
    completedLinks = 0
    print(f'Total de links encontrados: {totalLinksLen}')    
    print("Realizando extracción de datos...")
    for link in links:        
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'html.parser')
            dataParsed = soup.find_all(['h1','p'])
            data[link] = str(dataParsed)
            completedLinks += 1
            print(f'Completado: {completedLinks} de {totalLinksLen} links.')
    return data

def save_data_to_json():
    data = get_data_from_links()
    with open('data.json', 'w') as f:
        json.dump(data, fp=f)

save_data_to_json()