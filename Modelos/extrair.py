import requests
from bs4 import BeautifulSoup
from datetime import datetime


class Extracao:
    """Representa a extracao de um site"""

    def __init__(self, url):
        self.url = url
        self.soup = self.getSoup()

    def getSoup(self):
        """
        Requisita o HTTP e retorna o BeautifulSoup
        """
        try:
            response = requests.get(self.url)
            return BeautifulSoup(response.text, 'html.parser')
        except:
            print(f'Erro ao processar o HTTP {self.url}')
            return None
        
    def novas_noticias(self, limit=5):
        raise NotImplementedError("O método novas noticias deve ser implementado nas subclasses.")
    

    def listar_noticias(self):
        """
        Lista as notícias no formato abaixo:

        Data: Data da notícia

        Categoria: Categoria da notícia

        Título: Título da notícia
        
        Link: Link da notícia

        """
        if not self.soup:
            return 
                
        print(f'Última atualização local: {datetime.now().strftime("%d/%m/%Y %H:%M")}', flush=True)
        print("-" * 50, flush=True)

        novas = self.novas_noticias()
        if novas:
            for nova in novas:
                print(f'Data de publicação: {nova.get('data_publicacao', 'N/A')}', flush=True)
                print(f'Categoria: {nova.get('categoria')}', flush=True)
                print(f'Título: {nova.get('titulo')}', flush=True)
                print(f'Link: {nova.get('link')}', flush=True)
                print('-' * 50, flush=True)
        else:
            print("Nenhuma notícia encontrada ou erro na extração.")

    
