from Modelos.instituicoes import MME_extracao, ANEEL_extracao, EPE_extracao, ANP_extracao, CCEE_extracao #ONS_extracao
from Modelos.extrair import Extracao
from datetime import date, timedelta


def main():
    print("")
    print("NOTÍCIAS DOS ÚLTIMOS 7 DIAS")
    print("_" * 50)
    
    extratores = [
        {'orgao': 'MME', 'extrator': MME_extracao()},
        {'orgao': 'ANEEL', 'extrator': ANEEL_extracao()},
  #      {'orgao': 'EPE', 'extrator': EPE_extracao()},
        {'orgao': 'ANP', 'extrator': ANP_extracao()},
        {'orgao': 'CCEE', 'extrator': CCEE_extracao()}
       # {'orgao': 'ONS', 'extrator': ONS_extracao()}
    ]

    noticias_por_data = {}
    links_vistos = set()

    for item in extratores:
        extrator = item['extrator']
        todas_as_noticias = extrator.noticias_ultimos_dias()

        for noticia in todas_as_noticias:
            data_noticia = extrator.formatacao_datas(noticia.get('data_publicacao'))

            if data_noticia and noticia.get('link') not in links_vistos:
                if data_noticia not in noticias_por_data:
                    noticias_por_data[data_noticia] = []
                noticias_por_data[data_noticia].append(noticia)
                links_vistos.add(noticia.get('link'))

    hoje = date.today()
    for i in range(7):  # Loop para os últimos 7 dias
        data_a_exibir = hoje - timedelta(days=i)
        
        print(f"Dia {data_a_exibir.strftime('%d/%m/%Y')}")
        print("-" * 50)
        
        orgao_com_noticia = set()
        if data_a_exibir in noticias_por_data:
            noticias_do_dia = sorted(noticias_por_data[data_a_exibir], key=lambda x: x['orgao'])
            
            orgao_atual = ""
            contador = 0
            for noticia in noticias_do_dia:
                orgao_com_noticia.add(noticia['orgao'])

                if noticia['orgao'] != orgao_atual:
                    print(f"\n   - Notícias {noticia['orgao']}")
                    orgao_atual = noticia['orgao']
                    contador = 1
                
                print(f"      {contador}- Título: {noticia['titulo']} - Link: {noticia['link']}")
                #print(f"        Link: {noticia['link']}")
                contador += 1
        
        orgaos_todos = {item['orgao'] for item in extratores}
        orgao_sem_noticia = orgaos_todos - orgao_com_noticia
        
        if orgao_sem_noticia:
            for orgao in sorted(list(orgao_sem_noticia)):
                print(f"\n   - {orgao}: Sem notícias")

        print("\n")


if __name__ == "__main__":
    main()