

### Mini Projeto FastAPI

```markdown

Este é um mini projeto usando FastAPI, SQLAlchemy e Pydantic para criar uma API RESTful simples para gerenciar usuários.
A aplicação permite criar, ler, atualizar e deletar (CRUD) usuários.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

mini_projeto_fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── database.py
└── requirements.txt
```

- **app/__init__.py**: Indica que o diretório `app` é um pacote Python.
- **app/main.py**: Define a aplicação FastAPI e os endpoints da API.
- **app/models.py**: Define os modelos de dados utilizando SQLAlchemy.
- **app/schemas.py**: Define os esquemas de dados utilizando Pydantic.
- **app/crud.py**: Contém funções CRUD para interagir com o banco de dados.
- **app/database.py**: Configura a conexão com o banco de dados e cria a sessão.

## Funcionalidade da API

### Endpoints

- **POST /users/**: Cria um novo usuário.
- **GET /users/**: Retorna uma lista de usuários.
- **GET /users/{user_id}**: Retorna um usuário específico pelo ID.
- **PUT /users/{user_id}**: Atualiza um usuário específico pelo ID.
- **DELETE /users/{user_id}**: Deleta um usuário específico pelo ID.

### Modelos de Dados

- **User**: Modelo de dados do usuário com os campos `id`, `name`, `email` e `age`.

### Esquemas de Dados

- **UserBase**: Esquema base do usuário com os campos `name`, `email` e `age`.
- **UserCreate**: Esquema para criação de usuário.
- **User**: Esquema de retorno do usuário com o campo adicional `id`.

## Instruções de Execução

### Pré-requisitos

- Python 3.8+
- SQLite (ou outro banco de dados configurado no `DATABASE_URL`)

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/mini_projeto_fastapi.git
   cd mini_projeto_fastapi
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv env
   source env/bin/activate  # Linux/macOS
   .\env\Scripts\activate   # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

### Execução

1. Navegue até o diretório do projeto:

   ```bash
   cd testeFastAPI
   ```

2. Execute o Uvicorn para iniciar o servidor:

   ```bash
   uvicorn app.main:app --reload
   ```

3. Acesse a aplicação em `http://127.0.0.1:8000`.

4. Para ver a documentação automática da API, acesse `http://127.0.0.1:8000/docs`.

### Banco de Dados

O banco de dados é configurado para usar SQLite por padrão. O arquivo do banco de dados será criado no diretório raiz do projeto com o nome `test.db`.

Se quiser usar outro banco de dados, altere a variável `DATABASE_URL` no arquivo `app/database.py`.

## Contribuição

Se você quiser contribuir com este projeto, por favor, faça um fork do repositório e envie um pull request com suas melhorias ou correções de bugs.


Se precisar de mais alguma ajuda ou se houver algum problema específico, por favor, me avise!
