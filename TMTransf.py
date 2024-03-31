import requests
from bs4 import BeautifulSoup

# Fazendo a solicitação HTTP para obter o conteúdo da página
url = 'https://trophymanager.com/transfer/#/de/for/amax/null/cost/aff/'
response = requests.get(url)

# Verificando se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Parseando o conteúdo HTML usando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraindo informações desejadas
    # Por exemplo, para extrair o título da página:
    title = soup.title.text
    print("Título da Página:", title)

    # Outro exemplo, para extrair todos os links na página:
    links = soup.find_all('a')
    perfis = soup.find_all('div')
    print("\nLinks na Página:")
    for p in perfis:
        print(p.get('player_name'))

    # Você pode continuar a extrair outras informações conforme necessário
else:
    print("Falha ao carregar a página:", response.status_code)
