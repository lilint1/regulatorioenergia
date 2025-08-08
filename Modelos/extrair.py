import locale
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta


class Extracao:
    """Representa a extracao de um site"""

    def __init__(self, url, nome_site):
        self.url = url
        self.nome_site = nome_site
        self.soup = self.getSoup()

    def getSoup(self):
        """
        Requisita o HTTP e retorna o BeautifulSoup
        """
        try:
            response = requests.get(self.url)
            return BeautifulSoup(response.text, "html.parser")
        except:
            print(f"Erro ao processar o HTTP {self.url}")
            return None
        
    def novas_noticias(self, limit=15): 
        raise NotImplementedError("O método novas noticias deve ser implementado nas subclasses.")
    
    def formatacao_datas(self, data_str):
            """
            Converte a string data para um objeto date
            """
            try: #para DD/MM/AAAA
                return datetime.strptime(data_str, "%d/%m/%Y").date() 
            except ValueError:
                try: #para DD/MM/AA
                    return datetime.strptime(data_str, "%d/%m/%y").date()
                except ValueError:
                    return None

    def noticias_ultimos_dias(self):
        """
        Retorna as notícias dos últimos n dias
        """

        if not self.soup:
            return []
        
        todas_noticias = self.novas_noticias()
        noticias_filtradas = []
        ndias = 7

        hoje = date.today()
        datas_ultimos_ndias = [hoje - timedelta(days=i) for i in range(ndias)]

        for noticia in todas_noticias:
            data_noticia = self.formatacao_datas(noticia.get("data_publicacao", ""))

            if data_noticia and data_noticia in datas_ultimos_ndias:
                noticia["orgao"] = self.nome_site
                noticias_filtradas.append(noticia)

        return noticias_filtradas
