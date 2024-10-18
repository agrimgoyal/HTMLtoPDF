import requests
import pdfkit
from bs4 import BeautifulSoup

def extract_and_download_pdf(html_content, base_url=None):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a', href=True)
    html_links = []
    for link in links:
        href = link['href']
        if href and href.startswith('./afl'):
            if base_url:
                href = base_url + href[2:]
                try:
                    pdfkit.from_url(href, href.split('/')[-1] + '.pdf')
                    print(f"Downloaded {href.split('/')[-1]}.pdf")
                except Exception as e:
                    print(f"Failed to download {href}: {e}")
            else:
                print(f"Warning: Relative URL encountered: {href}. Base URL needed for absolute conversion.")
        html_links.append(href)
    return html_links

# Example usage:
url = "https://www.example.com"
base_url = "https://www.example.com"

extract_and_download_pdf(html_content, base_url)