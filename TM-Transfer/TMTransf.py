import requests
from bs4 import BeautifulSoup

# URL do site
url = "https://trophymanager.com/transfer/#/de/for/amax/25/rmin/8/cost/aff/"

# Fazendo a requisição GET para obter o conteúdo da página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parse do conteúdo HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrando todos os divs com a classe 'player_name'
    player_name_divs = soup.find_all('div', class_='player_name')

    print(player_name_divs)
    # Lista para armazenar os links
    links = []

    # Iterando sobre os divs encontrados
    for div in player_name_divs:
        # Encontrando o link dentro do div
        link = div.find('a')['href']
        linkA = div.find('a')
        print(linkA)
        # Adicionando o link à lista
        links.append(link)

    # Imprimindo os links encontrados
    for link in links:
        print(link)
else:
    print("Falha ao obter a página:", response.status_code)
