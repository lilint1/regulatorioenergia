## Regulatório de energia
⚠️ Projeto em desenvolvimento – extração do ONS ainda não implementada

## Descrição 

Objetivo: Extrair informações relevantes de órgãos reguladores e operadores, organizando-as por data e fonte.

Problema: Atualmente, a busca manual é lenta e propensa a erros. Este projeto centraliza as informações e prepara para futuras análises.

## Escopo:
- Informações coletadas: título, data, link da notícia.  
- Limite: até 10 notícias por fonte.  
- Filtra apenas publicações dos últimos 7 dias.  
- Fontes: MME, ANEEL, ANP, EPE, ONS e CCEE.  
- Saída: notícias exibidas no terminal organizadas por data e fonte.

## Tecnologias utilizadas

* Principais: Python 3.13; Requests; BeautifulSoup4
* Auxiliares: datetime
  
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
