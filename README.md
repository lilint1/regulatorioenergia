# Extração de notícias do Setor Energético Brasileiro
> :construction: Projeto em construção :construction: : Extrações ONS e CEEE ainda não foram implementadas.
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
regulatorioenergia/

├── app.py             # script principal
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