## Regulatório de energia
> :construction: Projeto em construção :construction: : Extração ONS ainda não foi implementada.
---
## Descrição 

Este projeto consiste em um script Python para extrair automaticamente as últimas notícias dos principais órgãos do setor energético brasileiro. 
O objetivo é facilitar o monitoramento e a coleta de informações relevantes das fontes: MME, ANEEL, ANP, EPE, ONS e CCEE.

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