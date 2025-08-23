## Regulatório de energia
> :construction: Projeto em construção :construction: : Extração ONS ainda não foi implementada.
---
## Descrição 

Problemática & objetivo: Este projeto visa evitar o trabalho manual de visitar diversos sites do setor energético brasileiro para buscar notícias. O objetivo é automatizar o monitoramento e a coleta de informações relevantes do setor. 

Escopo:
1. Informações coletadas: 
- Título
- Data de publicação
- Link para a notícia 
2. Critérios de seleção:
-  São considerados apenas publicações dos últimos 7 dias.
-  São coletadas até 10 notícias por fonte.
3. Fontes de informação:
   Dados públicos extraídos dos sites oficiais. As fontes: MME, ANEEL, ANP, EPE, ONS e CCEE.
   
4. Saída do script: As notícias são exibidas diretamente no terminal, organizadas por data e, dentro de cada data, por fonte, contendo o título e o link de cada notícia.
---
## Tecnologias utilizadas

* Python 3.13: Linguagem de programação principal.
* BeautifulSoup4: Extração de dados de páginas web.
* Requests: Requisições HTTP e obter o conteúdo das páginas.
* datetime: Manipulação de datas e horas.
---

## Organização do projeto
```sh
app.py: extrai últimas 10 notícias por instituição, nos últimos 7 dias
app_v1.py: extrai últimas 5 notícias por instituição

regulatorioenergia/

├── app.py             # script principal
├── app_v1.py          # script alternativo 
├── requirements.txt   # bibliotecas necessárias
├── README.md          # este arquivo
├── Modelos
  └── extrair.py       # script de extração
  └── instituicoes.py  # regras específicas
```
---

## Como executar

**Pré requisitos**
  - Python -> Linguagem principal
  - Pip -> Gerenciador de pacotes
    
1. Clone o repositório
   ```sh
   git clone https://github.com/lilint1/regulatorioenergia.git
   ```
2. Navegue até o diretório
    ```sh
   cd regulatorioenergia
   ```
3. Instale as dependências
   ```sh
   pip install -r requirements.txt
   ```
4. Execute o script
   ```sh
   python app.py
   ```
---

## Licença

Este projeto é para fins de estudo pessoal.
