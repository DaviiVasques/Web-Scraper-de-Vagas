# 🕷️ Web Scraper de Vagas com Python

## 📄 Descrição

Este projeto é um **web scraper** desenvolvido em Python para coletar informações sobre vagas de emprego de um site público.  

O programa extrai dados como:

- Título da vaga  
- Empresa  
- Localização  
- Link para candidatura  

E exporta essas informações para um arquivo **CSV** organizado.

---

O projeto foi desenvolvido seguindo o paradigma de **Programação Orientada a Objetos (POO)**, com o objetivo de:

- Facilitar a manutenção  
- Reaproveitamento de código  
- Escalabilidade  

---

## ⚙️ Funcionalidades

- Realiza requisição HTTP para capturar o HTML da página de vagas  
- Analisa o conteúdo HTML usando a biblioteca **BeautifulSoup** para extrair dados relevantes  
- Modela as vagas de emprego como objetos da classe `Vaga`  
- Exporta as vagas coletadas para um arquivo CSV com formatação adequada  
- Organiza o código utilizando classes e métodos claros, seguindo os princípios da **POO**

---

## 📁 Estrutura do projeto

web_scraper_vagas/

├── main.py # Script principal que executa o scraper e salva o CSV

├── scraper/  

│ ├── init.py # Torna scraper um pacote Python

│ ├── vaga.py # Define a classe Vaga (modelo de vaga)

│ └── vaga_scraper.py # Define a classe VagaScraper (lógica do scraping)

├── data/
│ └── vagas.csv # CSV gerado com os dados coletad

## 🛠️ Tecnologias e bibliotecas usadas

| Biblioteca          | Finalidade                                  |
|---------------------|---------------------------------------------|
| `requests`          | Fazer requisições HTTP para acessar o site |
| `BeautifulSoup (bs4)` | Parsear e navegar pelo HTML da página      |
| `csv`               | Exportar os dados coletados para CSV        |
| `os`                | Gerenciar criação de diretórios locais      |
