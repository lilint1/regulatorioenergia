from Modelos.extrair import Extracao
from datetime import datetime

class MME_extracao(Extracao):
    """
    Representa o MME e seus critérios de extração. 
    """

    def __init__(self):
        super().__init__("https://www.gov.br/mme/pt-br/assuntos/noticias", "MME")
    
    def novas_noticias(self, limit = 10):
        """Extrai o bloco de notícia"""
        titulos = self.soup.find_all("h2", class_="titulo")
        categorias = self.soup.find_all("div", class_="subtitulo-noticia")
        datas = self.soup.find_all("span", class_="data")

        novas_noticias = []
        for i in range(min(len(titulos), len(categorias), len(datas), limit)):
            titulo_tag = titulos[i]
            link_tag = titulo_tag.find("a")

            novas_noticias.append({
                "data_publicacao": datas[i].text.strip(),
                "categoria": categorias[i].text.strip(),
                "titulo": titulo_tag.text.strip(),
                "link": link_tag["href"].strip() if link_tag else "Link não encontrado",
            })
        return novas_noticias


class ANEEL_extracao(Extracao):
    """
    Representa a ANEEL e seus critérios de extração. 
    """
    def __init__(self):
        super().__init__("https://www.gov.br/aneel/pt-br/assuntos/noticias/2025", "ANEEL") 

    def novas_noticias(self, limit = 10):
        """Extrai o bloco de notícia"""
        titulos = self.soup.find_all("h2", class_="titulo")
        categorias = self.soup.find_all("div", class_="subtitulo-noticia")
        datas = self.soup.find_all("span", class_="data")

        novas_noticias = []
        for i in range(min(len(titulos), len(categorias), len(datas), limit)):
            titulo_tag = titulos[i]
            link_tag = titulo_tag.find("a")

            novas_noticias.append({
                "data_publicacao": datas[i].text.strip(),
                "categoria": categorias[i].text.strip(),
                "titulo": titulo_tag.text.strip(),
                "link": link_tag["href"].strip() if link_tag else "Link não encontrado",
            })
        return novas_noticias


class EPE_extracao(Extracao):
    """
        Representa a EPE e seus critérios de extração. 
    """
    def __init__(self):
        super().__init__("https://www.epe.gov.br/pt/imprensa/noticias", "EPE")
    
    def novas_noticias(self, limit = 5):
        """Extrai o bloco de notícia da EPE"""
        bloco_noticias = self.soup.find_all("div", class_ = "item")
        url_base = "https://www.epe.gov.br"

        novas_noticias = []
        for i in range(min(len(bloco_noticias), limit)):
            noticia = bloco_noticias[i]
            titulo_tag = noticia.find("h2", class_="blue")
            tag_categoria = noticia.find("a", class_="tag-area")
            data_tag = noticia.find("span", class_="date")
            link_tag = noticia.find("a")
            href = link_tag["href"].strip() if link_tag else ""
 

            novas_noticias.append({
                "data_publicacao": data_tag.text.strip(),
                "categoria": tag_categoria.text.strip(),
                "titulo": titulo_tag.text.strip(),
                "link": url_base + href if href.startswith("/") else href,
            })

        return novas_noticias

class ANP_extracao(Extracao):
    """
        Representa a ANP e seus critérios de extração.
    """
    def __init__(self):
        super().__init__("https://www.gov.br/anp/pt-br/canais_atendimento/imprensa/noticias-comunicados", "ANP")
    
    def novas_noticias(self, limit = 5):
        """Extrai o bloco de notícia"""
        titulos = self.soup.find_all("h2", class_="titulo")
        categorias = self.soup.find_all("div", class_="subtitulo-noticia")
        datas = self.soup.find_all("span", class_="data")

        novas_noticias = []
        for i in range(min(len(titulos), len(categorias), len(datas), limit)):
            titulo_tag = titulos[i]
            link_tag = titulo_tag.find("a")

            novas_noticias.append({
                "data_publicacao": datas[i].text.strip(),
                "categoria": categorias[i].text.strip(),
                "titulo": titulo_tag.text.strip(),
                "link": link_tag["href"].strip() if link_tag else "Link não encontrado"
            })
        return novas_noticias


class CCEE_extracao(Extracao):
    """
        Representa a CCEE e seus critérios de extração. 
    """

    def __init__(self):
        super().__init__("https://www.ccee.org.br/noticias", "CCEE")
    
    def novas_noticias(self, limit = 5):
        """Extrai os dois blocos de notícias da CCEE"""

        bloco_destaques = self.soup.find_all("div", class_ = "page-highlight-slider-item")
        bloco_ultimas = self.soup.find_all("div", class_ = "page-cards-slider-item")
        url_base = "https://www.ccee.org.br/"

        grupo_de_noticias = []
        for i in range(min(len(bloco_destaques), limit)):
            destaque = bloco_destaques[i]
            link_tag = destaque.find("a", href = True)
            if link_tag:
                grupo_de_noticias.append({
                "data_publicacao": destaque.find("span").text.strip(),
                "categoria": "Destaques",
                "titulo": destaque.find("h3").text.strip(),
                "link": url_base + link_tag["href"] if link_tag["href"].startswith("/") else link_tag["href"],
                })
            
        for i in range(min(len(bloco_ultimas), limit)):
            ultima = bloco_ultimas[i]
            link_tag = ultima.find("a", href = True)
            titulo_tag = ultima.find("h3")
            if link_tag:
                grupo_de_noticias.append({
                "data_publicacao": ultima.find("span").text.strip(),
                "categoria": "Últimas Noticias",
                "titulo": titulo_tag.text.strip(),
                "link": url_base + link_tag["href"] if link_tag["href"].startswith("/") else link_tag["href"],                    
                })
        return grupo_de_noticias
    

