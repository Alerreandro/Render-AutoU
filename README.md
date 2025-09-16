# Email Class

Email Class é uma aplicação web desenvolvida em Python com Django que ajuda os usuários a gerenciar seus emails diários de forma eficiente. Com o Email Class, os usuários podem classificar a prioridade de seus emails, como improdutivo e produto e também a aplicação oferecer respostas automáticas, facilitando e otimizando o trabalho do usuário.

## Funcionalidades

- **Classificando o email:** O usuario fornecer o e-mail, por meio de um arquivo .TXT ou digitando, para a aplicacao e ele retorna sua classificação, como produtivo ou improdutivo.
    
- **Gerando respostas automáticas:** Após a classificação dos e-mails, o sistema também fornecer uma respota automática baseado no email analisado.

## Instalação

1. Certifique-se de ter o [Python](https://www.python.org/downloads/) e o [Django](https://www.python.org/downloads/) instalados em sua máquina.

2. Clone o repositório do projeto:

    ```bash
        git clone https://github.com/Alerreandro/Projeto-Case-Pratico-AutoU.git
        cd Projeto-Case-Pratico-AutoU
    
3. Instale as dependências:
    
    ```bash
        pip install -r requirements.txt

4. Configure as Variáveis de Ambiente:

    * Crie um arquivo .env na raiz do projeto
    * Adicione dentro dele sua chave da [API do Gemini](https://aistudio.google.com/apikey)
    
    ```bash 
        GEMINI_API_KEY="SUA_CHAVE_SECRETA_DA_API_AQUI"
 
5. Inicie o Servidor Django:

    ```bash
        python manage.py runserver
    
6. Acesse a aplicação no seu navegador:

    ```bash
        http://127.0.0.1:8000/

## Tecnologias Utilizadas

 * Django: Versão 5.2.1.
 * Python: Versão 3.11.3
 * Google Gemini API
 * HTML 
 * CSS 
 * JavaScript

## Licença
Este projeto é licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes
    
