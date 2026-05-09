import requests
from bs4 import BeautifulSoup

def debug_structure():
    base_url = "https://fanyi.kkabc.com"
    list_url = f"{base_url}/mrfy/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    response = requests.get(list_url, headers=headers, timeout=10)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'html.parser')

    print("Page title:", soup.title.string if soup.title else "No title")

    lists_divs = soup.find_all('div', class_='list')
    print(f"Found {len(lists_divs)} divs with class 'list'")

    all_links = soup.find_all('a')
    print(f"Found {len(all_links)} total links")

    mrfy_links = [a for a in all_links if '/mrfy/show-' in a.get('href', '')]
    print(f"Found {len(mrfy_links)} '每日翻译' article links")

    if mrfy_links:
        print("\nFirst few article links:")
        for link in mrfy_links[:5]:
            print(f"  - {link.get('href')}: {link.get_text(strip=True)}")

if __name__ == "__main__":
    debug_structure()
