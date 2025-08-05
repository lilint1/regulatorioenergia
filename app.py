from Modelos.instituicoes import MME_extracao, ANEEL_extracao, EPE_extracao, ANP_extracao, CCEE_extracao
from Modelos.extrair import Extracao
from datetime import date, timedelta


def main():
    print("")
    print("NOTÍCIAS DOS ÚLTIMOS 7 DIAS")
    print("_" * 50 )
    
    extracoes = [
        MME_extracao(),
        ANEEL_extracao(),
        EPE_extracao(),
        ANP_extracao(),
        CCEE_extracao()
    ]

    noticias_por_data = {}
    links_vistos = set() 
    

    for extrator in extracoes:
        todas_as_noticias = extrator.noticias_ultimos_dias()
        for noticia in todas_as_noticias:
            data_news = extrator.formatacao_datas(noticia.get('data_publicacao'))

            if data_news and noticia.get('link') not in links_vistos:
                if data_news not in noticias_por_data:
                    noticias_por_data[data_news] = []
                noticias_por_data[data_news].append(noticia)
                links_vistos.add(noticia.get('link'))

    hoje = date.today()
    for i in range(7): # Loop para os últimos 7 dias
        data_a_exibir = hoje - timedelta(days=i)
        
        if data_a_exibir in noticias_por_data:
            print(f"Dia {data_a_exibir.strftime('%d/%m/%Y')}")
            print("-" * 50)
            
            noticias_do_dia = sorted(noticias_por_data[data_a_exibir], key=lambda x: x['orgao'])
            
            orgao_atual = ""
            contador = 0
            for noticia in noticias_do_dia:
                if noticia['orgao'] != orgao_atual:
                    print("")
                    print(f"  - Notícias {noticia['orgao']}")
                    orgao_atual = noticia['orgao']
                    contador = 1
                
                print(f"    {contador}- Título: {noticia['titulo']}")
                print(f"      Link: {noticia['link']}")
                contador += 1

            print("\n")


if __name__ == "__main__":
    main()