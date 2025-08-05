import csv
import os
from scraper.vaga_scraper import VagaScraper

def salvar_em_csv(vagas, caminho_csv):
    os.makedirs(os.path.dirname(caminho_csv), exist_ok=True)

    with open(caminho_csv, mode='w', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["Título", "Empresa", "Localização", "Link"])
        for vaga in vagas:
            writer.writerow(vaga.to_list())

if __name__ == "__main__":
    url = 'https://realpython.github.io/fake-jobs/'
    scraper = VagaScraper(url)
    vagas = scraper.obter_vagas()

    salvar_em_csv(vagas, 'data/vagas.csv')

    print(f"\n✅ {len(vagas)} vagas salvas com sucesso no arquivo 'data/vagas.csv'\n")
    for vaga in vagas[:5]:  # Mostra só as 5 primeiras no terminal
        print(vaga)
