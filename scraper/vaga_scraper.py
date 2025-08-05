import requests
from bs4 import BeautifulSoup
from .vaga import Vaga

class VagaScraper:
    def __init__(self, url):
        self.url = url

    def obter_vagas(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        elementos = soup.find_all('div', class_='card-content')

        vagas = []
        for elemento in elementos:
            titulo = elemento.find('h2', class_='title')
            empresa = elemento.find('h3', class_='company')
            local = elemento.find('p', class_='location')
            link_tag = elemento.find_next('a', text='Apply')

            if titulo and empresa and local and link_tag:
                vaga = Vaga(
                    titulo=titulo.text.strip(),
                    empresa=empresa.text.strip(),
                    localizacao=local.text.strip(),
                    link=link_tag['href']
                )
                vagas.append(vaga)

        return vagas