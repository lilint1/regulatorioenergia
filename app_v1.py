#Versão alternativa - Extrai 5 últimas notícias por instituição

#ESTRUTURA RECOMENDADA
# regulatorioenergia/

#├── app_v1.py          # script principal
#├── requirements.txt   # bibliotecas necessárias
#├── README.md          
#├── Modelos
#  └── extrair.py       # script de extração
#  └── instituicoes.py  # regras específicas


# Modelos/extrair.py

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
            return BeautifulSoup(response.text, "html.parser")
        except:
            print(f"Erro ao processar o HTTP {self.url}")
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
                
        print(f"Última atualização local: {datetime.now().strftime("%d/%m/%Y %H:%M")}", flush=True)
        print("-" * 50, flush=True)

        novas = self.novas_noticias()
        if novas:
            for nova in novas:
                print(f"Data de publicação: {nova.get("data_publicacao", "N/A")}", flush=True)
                print(f"Categoria: {nova.get("categoria")}", flush=True)
                print(f"Título: {nova.get("titulo")}", flush=True)
                print(f"Link: {nova.get("link")}", flush=True)
                print("-" * 50, flush=True)
        else:
            print("Nenhuma notícia encontrada ou erro na extração.")

    
# Modelos/ instituicoes.py

from Modelos.extrair import Extracao
from datetime import datetime

class MME_extracao(Extracao):
    """
    Representa o MME e seus critérios de extração. Exemplo de retorno:

    Data de publicação: 15/07/2025

    Categoria: WORKSHOP

    Título: MME debate novas soluções tecnológicas para avançar na descarbonização

    Link: https://www.gov.br/mme/pt-br/assuntos/noticias/mme-debate-novas-solucoes-tecnologicas-para-avancar-na-descarbonizacao
    """

    def __init__(self):
       
        super().__init__("https://www.gov.br/mme/pt-br/assuntos/noticias")
        self.siteNome = self.getNomeSite()
        self.siteDataAtualizacao = self.getDataAtualizacaoSite()

    def getNomeSite(self):
        """Extrai o nome do site da página do MME"""
        site_nome = self.soup.find("a", href="https://www.gov.br/mme/pt-br")
        return site_nome.text.strip() if site_nome else "MME"
    
    def getDataAtualizacaoSite(self):
        """Extrai a data da última atualizacao do site do MME"""
        site_data = self.soup.find_all(class_="value")
        return site_data[1].text.strip()
    
    def novas_noticias(self, limit = 5):
        """Extrai o bloco de notícia"""
        titulos = self.soup.find_all("h2", class_="titulo")
        categorias = self.soup.find_all("div", class_="subtitulo-noticia")
        datas = self.soup.find_all("span", class_="data")

        novas_noticias = []
        for i in range(min(len(titulos), len(categorias), len(datas), limit)):
            titulo_tag = titulos[i]
            titulo = titulo_tag.text.strip() if titulo_tag else "Titulo não encontrado"
            categoria = categorias[i].text.strip() if categorias[i] else "Categoria não encontrada"
            data_publicacao = datas[i].text.strip() if datas[i] else "Data não encontrada"
            link_tag = titulo_tag.find("a")
            link = link_tag["href"].strip() if link_tag else "Link não encontrado"

            novas_noticias.append({
                "data_publicacao": data_publicacao,
                "categoria": categoria,
                "titulo": titulo,
                "link": link,
            })
        return novas_noticias

    def listar_noticias(self):
        """Sobreescreve o método listar_noticias para extrair apenas informações desse site"""
        if not self.soup:
            return

        print(f"Órgão: {self.siteNome} | Atualizado em: {self.siteDataAtualizacao}")
        super().listar_noticias()


class ANEEL_extracao(Extracao):
    """
        Representa a ANEEL e seus critérios de extração. Exemplo de retorno:

        Data de publicação: 01/08/2025

        Categoria: EFICIÊNCIA ENERGÉTICA

        Título: Inscrições para a Olimpíada Nacional de Eficiência Energética 2025 estão abertas

        Link: https://www.gov.br/aneel/pt-br/assuntos/noticias/2025/inscricoes-para-a-olimpiada-nacional-de-eficiencia-energetica-2025-estao-abertas
    """
    def __init__(self):
        
        super().__init__("https://www.gov.br/aneel/pt-br/assuntos/noticias/2025")
        self.siteNome = self.getNomeSite()
        self.siteDataAtualizacao = self.getDataAtualizacaoSite()

    def getNomeSite(self):
        """Extrai o nome do site da página da ANEEL"""
        site_nome = self.soup.find("a", href="https://www.gov.br/aneel/pt-br")
        return site_nome.text.strip() if site_nome else "ANEEL"
    
    def getDataAtualizacaoSite(self):
        """Extrai a data da última atualizacao do site do ANEEL"""
        site_data = self.soup.find_all(class_="value")
        return site_data[1].text.strip()
    

    def novas_noticias(self, limit = 5):
        """Extrai o bloco de notícia"""
        titulos = self.soup.find_all("h2", class_="titulo")
        categorias = self.soup.find_all("div", class_="subtitulo-noticia")
        datas = self.soup.find_all("span", class_="data")

        print(f"DEBUG ANEEL: Encontrados {len(titulos)} títulos.")
        print(f"DEBUG ANEEL: Encontrados {len(categorias)} categorias.")
        print(f"DEBUG ANEEL: Encontrados {len(datas)} datas.")

        novas_noticias = []
        for i in range(min(len(titulos), len(categorias), len(datas), limit)):
            titulo_tag = titulos[i]
            titulo = titulo_tag.text.strip() if titulo_tag else "Titulo não encontrado"
            categoria = categorias[i].text.strip() if categorias[i] else "Categoria não encontrada"
            data_publicacao = datas[i].text.strip() if datas[i] else "Data não encontrada"
            link_tag = titulo_tag.find("a")
            link = link_tag["href"].strip() if link_tag else "Link não encontrado"

            novas_noticias.append({
                "data_publicacao": data_publicacao,
                "categoria": categoria,
                "titulo": titulo,
                "link": link,
            })
        print(f"DEBUG ANEEL: Retornando {len(novas_noticias)} notícias processadas.")
        print("-" * 50, flush=True)
        print("")
        return novas_noticias

    def listar_noticias(self):
        """Sobreescreve o listar_noticias para extrair apenas informações desse site"""
        if not self.soup:
            return

        print(f"Órgão: {self.siteNome} | Atualizado em: {self.siteDataAtualizacao}")
        super().listar_noticias()


class EPE_extracao(Extracao):
    """
        Representa a EPE e seus critérios de extração. Exemplo de retorno:

        Data de publicação: 01/08/2025 -

        Categoria: Energia Elétrica

        Título: EPE, ONS e CCEE divulgam segunda revisão quadrimestral da previsão de carga para o planejamento de 2025-2029

        Link: https://www.epe.gov.br/pt/imprensa/noticias/epe-ons-e-ccee-divulgam-segunda-revisao-quadrimestral-da-previsao-de-carga-para-o-planejamento-de-2025-2029
    """
    def __init__(self):
        
        super().__init__("https://www.epe.gov.br/pt/imprensa/noticias")
        self.siteNome = self.getNomeSite()
        self.url_base = "https://www.epe.gov.br"

    def getNomeSite(self):
        """Extrai o nome do site da página da EPE"""
        site_nome = self.soup.find("img", {"title": True})
        return site_nome["title"] if site_nome else "EPE"
    
    def getDataAtualizacaoSite(self):
        """Extrai a data da última atualizacao do site da EPE"""
        site_data = self.soup.find_all(class_="value")
        return site_data[1].text.strip() if len(site_data) > 1 else "N/A"
    
    def novas_noticias(self, limit = 5):
        """Extrai o bloco de notícia da EPE"""
        bloco_noticias = self.soup.find_all("div", class_ = "item")

        print(f"DEBUG EPE: Encontrados {len(bloco_noticias)} blocos de notícias")


        novas_noticias = []
        for i in range(min(len(bloco_noticias), limit)):
            noticias = bloco_noticias[i]
            
            titulo_tag = noticias.find("h2", class_="blue")
            titulo = titulo_tag.text.strip() if titulo_tag else "Título não encontrado"
            tag_categoria = noticias.find("a", class_="tag-area")
            categoria = tag_categoria.text.strip() if tag_categoria else "Categoria não encontrada"
            data_tag = noticias.find("span", class_="date")
            data_publicacao = data_tag.text.strip() if data_tag else "Data não encontrada"
            link_tag = noticias.find("a")
            href = link_tag["href"].strip() if link_tag else ""
            link = self.url_base + href if href.startswith("/") else href if href else "Link não encontrado"    

            novas_noticias.append({
                "data_publicacao": data_publicacao,
                "categoria": categoria,
                "titulo": titulo,
                "link": link,
            })
        print(f"DEBUG EPE: Retornando {len(novas_noticias)} notícias processadas.")
        print("-" * 50, flush=True)
        print("")
        return novas_noticias

    def listar_noticias(self):
        """Define método próprio de listar_noticias para extrair apenas informações desse site"""
        if not self.soup:
            return

        print(f"Órgão: {self.siteNome} | Atualizado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")
        #print(f"Última atualização local: {datetime.now().strftime("%Y-%m-%d %H:%M")}")
        super().listar_noticias()


class ANP_extracao(Extracao):
    """
        Representa a ANP e seus critérios de extração. Exemplo de retorno:

        Data de publicação: 01/08/2025

        Categoria: Boletim da produção

        Título: Produções de petróleo e de gás natural batem novo recorde em junho

        Link: https://www.gov.br/anp/pt-br/canais_atendimento/imprensa/noticias-comunicados/producoes-de-petroleo-e-de-gas-natural-batem-novo-recorde-em-junho
    """
    def __init__(self):
        
        super().__init__("https://www.gov.br/anp/pt-br/canais_atendimento/imprensa/noticias-comunicados")
        self.siteNome = self.getNomeSite()
        self.siteDataAtualizacao = self.getDataAtualizacaoSite()

    def getNomeSite(self):
        """Extrai o nome do site da página da ANP"""
        site_nome = self.soup.find("a", href="https://www.gov.br/anp/pt-br")
        return site_nome.text.strip() if site_nome else "ANP"
    
    def getDataAtualizacaoSite(self):
        """Extrai a data da última atualizacao do site do ANP"""
        site_data = self.soup.find_all(class_="value")
        return site_data[1].text.strip()
    
    def novas_noticias(self, limit = 5):
        """Extrai o bloco de notícia"""
        titulos = self.soup.find_all("h2", class_="titulo")
        categorias = self.soup.find_all("div", class_="subtitulo-noticia")
        datas = self.soup.find_all("span", class_="data")

        print(f"DEBUG ANP: Encontrados {len(titulos)} títulos.")
        print(f"DEBUG ANP: Encontrados {len(categorias)} categorias.")
        print(f"DEBUG ANP: Encontrados {len(datas)} datas.")

        novas_noticias = []
        for i in range(min(len(titulos), len(categorias), len(datas), limit)):
            titulo_tag = titulos[i]
            titulo = titulo_tag.text.strip() if titulo_tag else "Título não encontrado"
            categoria = categorias[i].text.strip() if categorias[i] else "Categoria não encontrada"
            data_publicacao = datas[i].text.strip() if datas[i] else "Data não encontrada"
            link_tag = titulo_tag.find("a")
            link = link_tag["href"].strip() if link_tag else "Link não encontrado"

            novas_noticias.append({
                "data_publicacao": data_publicacao,
                "categoria": categoria,
                "titulo": titulo,
                "link": link,
            })
        print(f"DEBUG ANP: Retornando {len(novas_noticias)} notícias processadas.")
        print("-" * 50, flush=True)
        print("")
        return novas_noticias

    def listar_noticias(self):
        """Sobreescreve o método listar_noticias para extrair apenas informações desse site"""
        if not self.soup:
            return

        print(f"Órgão: {self.siteNome} | Atualizado em: {self.siteDataAtualizacao}")
        super().listar_noticias()


class CCEE_extracao(Extracao):
    """
        Representa a CCEE e seus critérios de extração. Exemplo de retorno:

        Data de publicação: 01/08/25

        Categoria: Destaques

        Título: CCEE, ONS e EPE divulgam segunda revisão quadrimestral da previsão de carga para o planejamento de 2025-2029

        Link: https://www.ccee.org.br//web/guest/-/ccee-ons-e-epe-divulgam-segunda-revisao-quadrimestral-da-previsao-de-carga-para-o-planejamento-de-2025-2029
    """

    def __init__(self):
        
        super().__init__("https://www.ccee.org.br/noticias")
        self.siteNome = self.getNomeSite()
        self.url_base = "https://www.ccee.org.br/"
        #print(self.soup.prettify())

    def getNomeSite(self):
        """Extrai o nome do site da página da CCEE"""
        site_titulo = self.soup.find("title")
        return site_titulo.text.strip().split("-")[0].strip() if site_titulo else "CCEE"
    
    def getDataAtualizacaoSite(self):
        """Extrai a data da última atualizacao do site da CCEE"""
        site_data = self.soup.find_all(class_="caption")
        return site_data[1].text.strip() if len(site_data) > 1 else "N/A"
    
    def novas_noticias(self, limit = 5):
        """Extrai os dois blocos de notícias da CCEE"""

        bloco_destaques_noticias = self.soup.find_all("div", class_ = "page-highlight-slider-item")
        bloco_ultimas_noticias = self.soup.find_all("div", class_ = "col-12 col-lg-4 page-cards-slider-item box-cards-slider-noticias mb-5")

        print(f"DEBUG DESTAQUE CCEE: Encontrados {len(bloco_destaques_noticias)} blocos de notícias")
        print(f"DEBUG ÚLTIMAS CCEE: Encontrados {len(bloco_ultimas_noticias)} blocos de notícias")


        grupo_de_noticias = []
        for i in range(min(len(bloco_destaques_noticias), limit)):
            dnoticias = bloco_destaques_noticias[i]
            
            titulo_tag = dnoticias.find("h3")
            titulo = titulo_tag.text.strip() if titulo_tag else "Título não encontrado"
            data_tag = dnoticias.find("span")
            data_publicacao = data_tag.text.strip() if data_tag else "Data não encontrada"
            link_tag = dnoticias.find("a", href = True)
            link = self.url_base + link_tag["href"] if link_tag and link_tag["href"].startswith("/") else "Link não encontrado"  

            grupo_de_noticias.append({
                "data_publicacao": data_publicacao,
                "categoria": "Destaques",
                "titulo": titulo,
                "link": link,
            })

        for i in range(min(len(bloco_ultimas_noticias), limit)):
            unoticias = bloco_ultimas_noticias[i]
            
            titulo_tag = unoticias.find("h3", class_ = "multiline-ellipsis-3")
            titulo = titulo_tag.text.strip() if titulo_tag else "Título não encontrado"
            data_tag = unoticias.find("span")
            data_publicacao = data_tag.text.strip() if data_tag else "Data não encontrada"
            link_tag = unoticias.find("a", href = True)
            link = self.url_base + link_tag["href"] if link_tag and link_tag["href"].startswith("/") else "Link não encontrado"  

            grupo_de_noticias.append({
                "data_publicacao": data_publicacao,
                "categoria": "Últimas Noticias",
                "titulo": titulo,
                "link": link,
            })


        print(f"DEBUG CCEE: Retornando {len(grupo_de_noticias)} notícias processadas.")
        print("-" * 50, flush=True)
        print("")
        return grupo_de_noticias
    

    def listar_noticias(self):
        """Define método próprio de listar_noticias para extrair apenas informações desse site"""
        if not self.soup:
            return

        print(f"Órgão: {self.siteNome} | Atualizado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")
        #print(f"Última atualização local: {datetime.now().strftime("%Y-%m-%d %H:%M")}")
        super().listar_noticias()


# app.py

from Modelos.instituicoes import MME_extracao, ANEEL_extracao, EPE_extracao, ANP_extracao, CCEE_extracao

def main():
    print("")
    print(" NOTÍCIAS DO MINISTERIO DE MINAS E ENERGIA - MME")
    print("")
    site_mme = MME_extracao()
    site_mme.listar_noticias()

    print("")
    print("NOTÍCIAS DA EMPRESA DE PESQUISA ENERGÉTICA - EPE")
    print("")
    site_epe = EPE_extracao()
    site_epe.listar_noticias()

    print("")
    print("NOTÍCIAS DA AGÊNCIA NACIONAL DO PETRÓLEO, GÁS NATURAL E BIOCOMBUSTÍVEIS - ANP")
    print("")
    site_anp = ANP_extracao()
    site_anp.listar_noticias()

    print("")
    print("NOTÍCIAS DA AGÊNCIA NACIONAL DE ENERGIA ELÉTRICA - ANEEL")
    print("")
    site_aneel = ANEEL_extracao()
    site_aneel.listar_noticias()

    print("")
    print("NOTÍCIAS DA CÂMARA DE COMERCIALIZAÇÃO DE ENERGIA ELÉTRICA - CCEE")
    print("")
    site_ccee = CCEE_extracao()
    site_ccee.listar_noticias()

if __name__ == "__main__":
    main()