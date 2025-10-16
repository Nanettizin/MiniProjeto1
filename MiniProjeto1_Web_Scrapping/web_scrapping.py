import requests
import bs4

url = 'https://g1.globo.com'

# Tive que colocar essa maldade por que o g1 sabia do webscrapping
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print("Baixando a página do G1...")
resposta = requests.get(url, headers=HEADERS)
resposta.raise_for_status()

soup = bs4.BeautifulSoup(resposta.text, 'lxml')
print("Iniciando extração de manchetes...")

lista_manchetes = soup.select('a.feed-post-link')

print(f"{len(lista_manchetes)} Manchetes Encontradas!")

for manchete in lista_manchetes:    
    texto_manchete = manchete.get_text(strip=True)    
    link_mancheche = manchete.get('href')
    print(f"Título: {texto_manchete}")
    print(f"Link: {link_mancheche}")
    print("-" * 20) 