import requests
from bs4 import BeautifulSoup

def debug_full_structure():
    article_url = "https://fanyi.kkabc.com/mrfy/show-2941.html"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    response = requests.get(article_url, headers=headers, timeout=10)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'html.parser')

    body_content = soup.find('body')
    if body_content:
        with open('page_structure.txt', 'w', encoding='utf-8') as f:
            f.write(body_content.prettify())
        print("Page structure saved to page_structure.txt")

if __name__ == "__main__":
    debug_full_structure()
