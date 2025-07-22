from Modelos.extrair import Extracao
from datetime import datetime

class MME_extracao(Extracao):
    """
    Representa o Ministério de Minas e Energia e seus critérios de extração. Exemplo de retorno:

    Data de publicação: 15/07/2025

    Categoria: WORKSHOP

    Título: MME debate novas soluções tecnológicas para avançar na descarbonização

    Link: https://www.gov.br/mme/pt-br/assuntos/noticias/mme-debate-novas-solucoes-tecnologicas-para-avancar-na-descarbonizacao
    """

    def __init__(self):
       
        super().__init__('https://www.gov.br/mme/pt-br/assuntos/noticias')
        self.siteNome = self.getNomeSite()
        self.siteDataAtualizacao = self.getDataAtualizacaoSite()

    def getNomeSite(self):
        """Extrai o nome do site da página do MME"""
        site_nome = self.soup.find('a', href='https://www.gov.br/mme/pt-br')
        return site_nome.text.strip() if site_nome else 'MME'
    
    def getDataAtualizacaoSite(self):
        """Extrai a data da última atualizacao do site do MME"""
        site_data = self.soup.find_all(class_='value')
        return site_data[1].text.strip()
    
    def novas_noticias(self, limit = 5):
        """Extrai o bloco de notícia"""
        titulos = self.soup.find_all('h2', class_='titulo')
        categorias = self.soup.find_all('div', class_='subtitulo-noticia')
        datas = self.soup.find_all('span', class_='data')

        novas_noticias = []
        for i in range(min(len(titulos), len(categorias), len(datas), limit)):
            titulo_tag = titulos[i]
            titulo = titulo_tag.text.strip()
            categoria = categorias[i].text.strip()
            data_publicacao = datas[i].text.strip()
            link_tag = titulo_tag.find('a')
            link = link_tag['href'].strip() if link_tag else 'Link não encontrado'

            novas_noticias.append({
                'data_publicacao': data_publicacao,
                'categoria': categoria,
                'titulo': titulo,
                'link': link,
            })
        return novas_noticias

    def listar_noticias(self):
        """Sobreescreve o método listar_noticias para extrair apenas informações desse site"""
        if not self.soup:
            return

        print(f'Órgão: {self.siteNome} | Atualizado em: {self.siteDataAtualizacao}')
        super().listar_noticias()


class ANEEL_extracao(Extracao):
    """
        Representa a Agência Nacional de Energia Elétrica e seus critérios de extração. Exemplo de retorno:

        Data de publicação: 15/07/2025

        Categoria: WORKSHOP

        Título: MME debate novas soluções tecnológicas para avançar na descarbonização

        Link: https://www.gov.br/mme/pt-br/assuntos/noticias/mme-debate-novas-solucoes-tecnologicas-para-avancar-na-descarbonizacao
    """
    def __init__(self):
        
        super().__init__('https://www.gov.br/aneel/pt-br/assuntos/noticias/2025')
        self.siteNome = self.getNomeSite()
        self.siteDataAtualizacao = self.getDataAtualizacaoSite()

    def getNomeSite(self):
        """Extrai o nome do site da página da ANEEL"""
        site_nome = self.soup.find('a', href='https://www.gov.br/aneel/pt-br')
        return site_nome.text.strip() if site_nome else 'ANEEL'
    
    def getDataAtualizacaoSite(self):
        """Extrai a data da última atualizacao do site do ANEEL"""
        site_data = self.soup.find_all(class_='value')
        return site_data[1].text.strip()
    
    def novas_noticias(self, limit = 5):
        """Extrai o bloco de notícia"""
        titulos = self.soup.find_all('h2', class_='titulo')
        categorias = self.soup.find_all('div', class_='subtitulo-noticia')
        datas = self.soup.find_all('span', class_='data')

        print(f"DEBUG ANEEL: Encontrados {len(titulos)} títulos.")
        print(f"DEBUG ANEEL: Encontrados {len(categorias)} categorias.")
        print(f"DEBUG ANEEL: Encontrados {len(datas)} datas.")

        novas_noticias = []
        for i in range(min(len(titulos), len(categorias), len(datas), limit)):
            titulo_tag = titulos[i]
            titulo = titulo_tag.text.strip()
            categoria = categorias[i].text.strip()
            data_publicacao = datas[i].text.strip()
            link_tag = titulo_tag.find('a')
            link = link_tag['href'].strip() if link_tag else 'Link não encontrado'

            novas_noticias.append({
                'data_publicacao': data_publicacao,
                'categoria': categoria,
                'titulo': titulo,
                'link': link,
            })
        print(f"DEBUG ANEEL: Retornando {len(novas_noticias)} notícias processadas.")
        print('-' * 50, flush=True)
        print('')
        return novas_noticias

    def listar_noticias(self):
        """Sobreescreve o método listar_noticias para extrair apenas informações desse site"""
        if not self.soup:
            return

        print(f'Órgão: {self.siteNome} | Atualizado em: {self.siteDataAtualizacao}')
        super().listar_noticias()


class EPE_extracao(Extracao):
    """
        Representa a Empresa de Pesquisa Energética e seus critérios de extração. Exemplo de retorno:

        Data de publicação: 15/07/2025

        Categoria: WORKSHOP

        Título: MME debate novas soluções tecnológicas para avançar na descarbonização

        Link: https://www.gov.br/mme/pt-br/assuntos/noticias/mme-debate-novas-solucoes-tecnologicas-para-avancar-na-descarbonizacao
    """
    def __init__(self):
        
        super().__init__('https://www.epe.gov.br/pt/imprensa/noticias')
        self.siteNome = self.getNomeSite()
        self.url_base = 'https://www.epe.gov.br'

    def getNomeSite(self):
        """Extrai o nome do site da página da EPE"""
        site_nome = self.soup.find('img', {'title': True})
        return site_nome['title'] if site_nome else 'EPE'
    
    def getDataAtualizacaoSite(self):
        """Extrai a data da última atualizacao do site da EPE"""
        site_data = self.soup.find_all(class_='value')
        return site_data[1].text.strip() if len(site_data) > 1 else 'N/A'
    
    def novas_noticias(self, limit = 5):
        """Extrai o bloco de notícia da EPE"""
        bloco_noticias = self.soup.find_all('div', class_ = 'item')

        print(f"DEBUG EPE: Encontrados {len(bloco_noticias)} blocos de notícias ('div class=item').")


        novas_noticias = []
        for i in range(min(len(bloco_noticias), limit)):
            noticias = bloco_noticias[i]
            
            titulo_tag = noticias.find('h2', class_='blue')
            titulo = titulo_tag.text.strip() if titulo_tag else 'Título não encontrado'
            tag_categoria = noticias.find('a', class_='tag-area')
            categoria = tag_categoria.text.strip() if tag_categoria else 'Categoria não encontrada'
            data_tag = noticias.find('span', class_='date')
            data_publicacao = data_tag.text.strip() if data_tag else 'Data não encontrada'
            link_tag = noticias.find('a')
            href = link_tag['href'].strip() if link_tag else ''
            link = self.url_base + href if href.startswith('/') else href if href else 'Link não encontrado'    

            novas_noticias.append({
                'data_publicacao': data_publicacao,
                'categoria': categoria,
                'titulo': titulo,
                'link': link,
            })
        print(f"DEBUG EPE: Retornando {len(novas_noticias)} notícias processadas.")
        print('-' * 50, flush=True)
        print('')
        return novas_noticias

    def listar_noticias(self):
        """Define método próprio de listar_noticias para extrair apenas informações desse site"""
        if not self.soup:
            return

        print(f'Órgão: {self.siteNome} | Atualizado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
        #print(f'Última atualização local: {datetime.now().strftime("%Y-%m-%d %H:%M")}')
        super().listar_noticias()


        #Adicionar ANP, ONS, CCEE

        #https://www.gov.br/anp/pt-br/canais_atendimento/imprensa/noticias-comunicados

class ANP_extracao(Extracao):
    """
        Representa a Agência Nacional de Petróleo, Gás Natural e Biocombustíveis e seus critérios de extração. Exemplo de retorno:

        Data de publicação: 15/07/2025

        Categoria: WORKSHOP

        Título: MME debate novas soluções tecnológicas para avançar na descarbonização

        Link: https://www.gov.br/mme/pt-br/assuntos/noticias/mme-debate-novas-solucoes-tecnologicas-para-avancar-na-descarbonizacao
    """
    def __init__(self):
        
        super().__init__('https://www.gov.br/anp/pt-br/canais_atendimento/imprensa/noticias-comunicados')
        self.siteNome = self.getNomeSite()
        self.siteDataAtualizacao = self.getDataAtualizacaoSite()

    def getNomeSite(self):
        """Extrai o nome do site da página da ANP"""
        site_nome = self.soup.find('a', href='https://www.gov.br/anp/pt-br')
        return site_nome.text.strip() if site_nome else 'ANP'
    
    def getDataAtualizacaoSite(self):
        """Extrai a data da última atualizacao do site do ANP"""
        site_data = self.soup.find_all(class_='value')
        return site_data[1].text.strip()
    
    def novas_noticias(self, limit = 5):
        """Extrai o bloco de notícia"""
        titulos = self.soup.find_all('h2', class_='titulo')
        categorias = self.soup.find_all('div', class_='subtitulo-noticia')
        datas = self.soup.find_all('span', class_='data')

        print(f"DEBUG ANEEL: Encontrados {len(titulos)} títulos.")
        print(f"DEBUG ANEEL: Encontrados {len(categorias)} categorias.")
        print(f"DEBUG ANEEL: Encontrados {len(datas)} datas.")

        novas_noticias = []
        for i in range(min(len(titulos), len(categorias), len(datas), limit)):
            titulo_tag = titulos[i]
            titulo = titulo_tag.text.strip()
            categoria = categorias[i].text.strip()
            data_publicacao = datas[i].text.strip()
            link_tag = titulo_tag.find('a')
            link = link_tag['href'].strip() if link_tag else 'Link não encontrado'

            novas_noticias.append({
                'data_publicacao': data_publicacao,
                'categoria': categoria,
                'titulo': titulo,
                'link': link,
            })
        print(f"DEBUG ANP: Retornando {len(novas_noticias)} notícias processadas.")
        print('-' * 50, flush=True)
        print('')
        return novas_noticias

    def listar_noticias(self):
        """Sobreescreve o método listar_noticias para extrair apenas informações desse site"""
        if not self.soup:
            return

        print(f'Órgão: {self.siteNome} | Atualizado em: {self.siteDataAtualizacao}')
        super().listar_noticias()