## API REST com Flask

Este projeto consiste em uma API RESTful construída com Flask. Ele permite a criação, leitura, atualização e exclusão de itens em um banco de dados, além de implementar autenticação via JWT.

## Funcionalidades

- Login: Endpoint para autenticação via email e senha.
- CRUD de Itens: Criar, listar, atualizar e deletar itens no banco de dados.
- Paginação: A listagem de itens é paginada.
- Cache: A listagem de itens tem cache implementado para melhorar o desempenho.

## Tecnologias Utilizadas

- Flask: Framework utilizado para construção da API.
- Flask-JWT-Extended: Para autenticação com JWT.
- SQLAlchemy: ORM para interação com o banco de dados.
- Marshmallow: Para validação e serialização dos dados.
- Flask-Caching: Para cache de requisições.
- Unittest: Para testes automatizados.
- SQLite: Banco de dados utilizado (pode ser configurado para outro banco de dados).

## Como Usar

1. Configuração do Ambiente

Para rodar a aplicação, você precisa configurar algumas variáveis de ambiente:

- DATABASE_URL: URL de conexão do banco de dados (exemplo: sqlite:///mydatabase.db).
- JWT_SECRET_KEY: Chave secreta usada para gerar os tokens JWT.

## Você pode configurar essas variáveis diretamente no terminal (temporárias):

- set DATABASE_URL=sqlite:///mydatabase.db
- set JWT_SECRET_KEY=your_local_secret_key

# Ou você pode usar um arquivo .env (exemplo com python-dotenv):

- DATABASE_URL=sqlite:///mydatabase.db
- JWT_SECRET_KEY=your_local_secret_key

2. Instalar Dependências

## Instale as dependências necessárias com o pip:

- pip install -r requirements.txt

3.  Iniciar a Aplicação

## Após configurar as variáveis de ambiente, inicie a aplicação com o comando:

- python app.py
A aplicação estará disponível em http://127.0.0.1:5000.

## Testar a API

- Você pode testar os endpoints utilizando o Postman ou qualquer outra ferramenta de sua preferência.

## Endpoints

- POST /login: Autentica um usuário e retorna um token JWT.
- GET /items: Lista os itens, com suporte a paginação.
- POST /items: Cria um novo item.
- PUT /items/{id}: Atualiza um item existente.
- DELETE /items/{id}: Deleta um item.

## Exemplo de Requisição

- POST /login:

{
  "email": "usuario@example.com",
  "password": "senha123"
}

- GET /items: URL: /items?page=1
- POST /items:

{
  "name": "Novo Item",
  "description": "Descrição do item"
}

## Testes

- Os testes automatizados estão no arquivo tests.py. Para executá-los, use o comando:
- python -m unittest tests.py

### Esses testes garantem que os endpoints estão funcionando conforme o esperado.

## Deploy para Produção

# Para rodar sua API em produção, é recomendado usar um servidor WSGI como Gunicorn. Você pode iniciar a aplicação com:

- gunicorn app:app

## Configuração do Nginx (Exemplo)

# Se você estiver usando o Nginx como proxy reverso, uma configuração básica pode ser:

server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

## Licença

- Este projeto está licenciado sob a Licença MIT.