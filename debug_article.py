import requests
from bs4 import BeautifulSoup

def debug_article_structure():
    base_url = "https://fanyi.kkabc.com"
    article_url = "https://fanyi.kkabc.com/mrfy/show-2941.html"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    response = requests.get(article_url, headers=headers, timeout=10)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'html.parser')

    print("Page title:", soup.title.string if soup.title else "No title")

    h2_tags = soup.find_all('h2')
    print(f"\nFound {len(h2_tags)} h2 tags:")
    for h2 in h2_tags:
        print(f"  - {h2.get_text(strip=True)}")

    content_divs = soup.find_all('div', class_='content')
    print(f"\nFound {len(content_divs)} divs with class 'content':")
    for div in content_divs:
        text = div.get_text(separator='\n', strip=True)
        print(f"Content:\n{text[:500]}...")

    article_divs = soup.find_all('div', class_='article')
    print(f"\nFound {len(article_divs)} divs with class 'article':")
    for div in article_divs:
        text = div.get_text(separator='\n', strip=True)
        print(f"Content:\n{text[:500]}...")

    main_content = soup.find('main')
    if main_content:
        print("\nFound <main> tag:")
        text = main_content.get_text(separator='\n', strip=True)
        print(f"Content:\n{text[:800]}...")

if __name__ == "__main__":
    debug_article_structure()
