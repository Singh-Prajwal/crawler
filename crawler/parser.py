from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def extract_links(base_url, html_content):
    try:
        soup = BeautifulSoup(html_content, 'lxml')
        links = set()
        base_netloc = urlparse(base_url).netloc

        for a_tag in soup.find_all('a', href=True):
            try:
                href = a_tag['href']
                if href.startswith(("mailto:", "tel:", "javascript:")):
                    continue

                joined = urljoin(base_url, href)
                parsed = urlparse(joined)

                if parsed.netloc and base_netloc in parsed.netloc:
                    links.add(joined.split('#')[0])
            except Exception as inner_e:
                print(f"\033[91m[ERROR]\033[0m Malformed link skipped: {inner_e}")

        return links
    except Exception as e:
        print(f"\033[91m[ERROR]\033[0m Failed to parse HTML from {base_url}: {e}")
        return set()
