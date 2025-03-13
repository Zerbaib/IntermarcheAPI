import requests
from bs4 import BeautifulSoup
import os

# URL de la page à récupérer
recherche = input("Que voulez-vous rechercher ? ")
url = f'https://www.carrefour.fr/s?q={recherche}'

# Faire une requête GET à l'URL
response = requests.get(url)

# Sauvegarder le contenu HTML de la page
with open('page.html', 'w', encoding='utf-8') as file:
    print(response.text)
    file.write(response.text)

# Parser le contenu HTML avec BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver les divs avec la classe "product-price__amounts"
price_divs = soup.find_all('div', class_='product-price__amounts', limit=3)

# Récupérer les noms et prix des produits
for price_div in price_divs:
    product_name = price_div.find_previous('h3', class_='c-text c-text--size-m c-text--style-p c-text--bold c-text--spacing-default product-card-title__text product-card-title__text--hoverable').text.strip()
    product_price = price_div.text.strip()
    print(f'{product_name}:{product_price}')

# Supprimer le fichier page.html
if os.path.exists('page.html'):
    os.remove('page.html')
    print("Le fichier page.html a été supprimé.")
else:
    print("Le fichier page.html n'existe pas.")