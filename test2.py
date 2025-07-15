import requests
import re
from abc import ABC, abstractmethod

class BaseRegexScraper(ABC):
    def __init__(self, url: str, pattern: str, tema: str, fonte: str):
        self.url = url
        self.pattern = pattern
        self.tema = tema
        self.fonte = fonte

    def fetch(self):
        response = requests.get(self.url, timeout=10)
        response.raise_for_status()
        return response.text

    def extract(self):
        html = self.fetch()
        resultados = []
        matches = re.findall(self.pattern, html, re.DOTALL | re.IGNORECASE)
        for match in matches:
            conteudo = match[1] if isinstance(match, tuple) else match
            titulo = re.sub(r'<[^>]+>', '', conteudo).strip()
            titulo = re.sub(r'\s+', ' ', titulo)
            link_match = re.search(r'href=[\'"]([^\'"]+)[\'"]', conteudo)
            link = link_match.group(1) if link_match else None
            resultados.append({
                'titulo': titulo,
                'link': link,
                'fonte': self.fonte
            })
        return resultados

def main():
           
    scrapers = [
        BaseRegexScraper(
            url="https://www.gov.br/aneel/pt-br/assuntos/noticias",
            pattern= r'<h[12][^>]*>(.*?)</h[12]>',
            tema= "Minas e Energia",
            fonte="ANEEL"
        ),
        BaseRegexScraper(
            url="https://www.gov.br/mme/pt-br/assuntos/noticias",
            pattern=r'<h[12][^>]*>(.*?)</h[12]>',
            tema= "Minas e Energia",
            fonte="MME"
        ),
    ]

    all_news = []
    for scraper in scrapers:
        try:
            items = scraper.extract()
            print(f"[OK] {scraper.fonte}: {len(items)} itens encontrados")
            all_news.extend(items)
        except Exception as e:
            print(f"[ERROR] {scraper.fonte}: {e}")

    print("\n=== Notícias coletadas ===\n")
    print("Itens encontrados", len(all_news) )
    for n in all_news:
        print(f"[{n['fonte']}] {n['titulo']}")
        print(f" - Tema: {n['tema']}")
        print(f" - Link: {n['link']}\n")

if __name__ == "__main__":
    main()
