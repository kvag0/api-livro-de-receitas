# API de Livro de Receitas com Python e Flask (Projeto 3)

Este projeto é a terceira parte de uma série de estudos de tech stacks. O objetivo foi construir uma API RESTful completa utilizando um ecossistema de backend diferente: **Python**, o micro-framework **Flask**, e um banco de dados relacional **PostgreSQL**.

O foco principal foi o aprendizado por contraste, comparando esta abordagem com a stack Node.js/Express/MongoDB do Projeto 1.

---

## 🧠 Principais Aprendizados e Comparações

* **Python/Flask vs. Node.js/Express:** Explorámos a sintaxe limpa e direta do Python e a filosofia minimalista do Flask, que oferece um núcleo pequeno e grande flexibilidade. A definição de rotas com "decoradores" (`@app.route`) é um bom exemplo dessa abordagem elegante.

* **SQL (PostgreSQL) vs. NoSQL (MongoDB):** Esta foi a maior mudança conceitual. Trabalhámos com dados estruturados em **tabelas, colunas e linhas**, em vez de documentos flexíveis. Isto forçou-nos a pensar na estrutura dos dados antecipadamente.

* **Modelagem Relacional:** Aprendemos a criar uma relação "um-para-muitos" (uma receita tem muitos ingredientes) usando `ForeignKey` para ligar as tabelas.

* **ORM: SQLAlchemy vs. Mongoose:** Vimos como o SQLAlchemy, o ORM (Object-Relational Mapper) do mundo Python, traduz classes Python em tabelas SQL. Entendemos o conceito de **sessão** (`db.session`) para agrupar operações (`add`, `delete`) e confirmá-las (`commit`) como uma transação única.

---

## 🛠️ Tech Stack & Ferramentas

* **Linguagem:** Python
* **Framework:** Flask
* **Banco de Dados:** PostgreSQL
* **ORM:** SQLAlchemy (integrado via Flask-SQLAlchemy)
* **Driver do Banco de Dados:** `psycopg2`
* **Gerenciamento de Ambiente:** `venv` (Ambiente Virtual) e `pip` (Instalador de Pacotes)
* **Gestão de Segredos:** `python-dotenv`

---

## 🚀 Endpoints da API (Funcionalidades)

A API implementa um CRUD (Create, Read, Update, Delete) completo para as receitas.

| Funcionalidade | Método HTTP | Endpoint | Corpo (Body) da Requisição | Resposta de Sucesso |
| :--- | :--- | :--- | :--- | :--- |
| **Listar todas as receitas** | `GET` | `/api/recipes` | *Nenhum* | `200 OK` |
| **Criar uma nova receita** | `POST` | `/api/recipes` | `{ "name": "...", "instructions": "...", "ingredients": [...] }` | `201 Created` |
| **Buscar uma receita** | `GET` | `/api/recipes/<id>` | *Nenhum* | `200 OK` |
| **Atualizar uma receita** | `PUT` | `/api/recipes/<id>` | `{ "name": "...", "instructions": "..." }` | `200 OK` |
| **Deletar uma receita** | `DELETE` | `/api/recipes/<id>` | *Nenhum* | `200 OK` |

---

## ⚙️ Como Executar o Projeto Localmente

**Pré-requisitos:**
* Python 3
* Servidor PostgreSQL instalado e a correr
* Git

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/api-livro-de-receitas.git](https://github.com/seu-usuario/api-livro-de-receitas.git)
    cd api-livro-de-receitas
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    # Criar o ambiente
    python3 -m venv venv

    # Ativar no macOS/Linux
    source venv/bin/activate

    # Ativar no Windows (cmd.exe)
    # .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o Banco de Dados:**
    * Aceda ao seu terminal `psql` do PostgreSQL.
    * Crie a base de dados para o projeto:
        ```sql
        CREATE DATABASE recipe_book_db;
        ```

5.  **Configure as Variáveis de Ambiente:**
    * Crie um ficheiro chamado `.env` na raiz do projeto.
    * Adicione a sua URL de conexão, seguindo o exemplo abaixo:
        ```env
        # Exemplo para Windows com usuário 'postgres' e senha 'admin'
        # DATABASE_URL=postgresql://postgres:admin@localhost:5432/recipe_book_db

        # Exemplo para macOS com Postgres.app e usuário 'caiosobrinho'
        # DATABASE_URL=postgresql://caiosobrinho@localhost:5432/recipe_book_db
        ```

6.  **Crie as Tabelas da Aplicação:**
    * No terminal (com o ambiente virtual ativo), execute o `flask shell`:
        ```bash
        flask shell
        ```
    * Dentro do shell, execute os seguintes comandos Python:
        ```python
        >>> from app import db
        >>> db.create_all()
        >>> exit()
        ```

7.  **Execute o servidor de desenvolvimento:**
    ```bash
    python3 app.py
    ```
    O servidor estará a correr em `http://127.0.0.1:5000`.
