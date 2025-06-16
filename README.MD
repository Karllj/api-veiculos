# Gerenciamento de Veículos (FastAPI + SQLite)

Projeto CRUD para gerenciar veículos, construído com FastAPI e SQLite. Permite criar, listar, editar e excluir veículos por meio de uma interface HTML simples ou via ferramentas de API como Postman.

---

## ✨ Funcionalidades

* **Adicionar Veículo**: Cadastro de veículos com modelo, marca e ano.
* **Listar Veículos**: Visualização de todos os veículos cadastrados, mostrando ID e dados.
* **Editar Veículo**: Atualização dos dados de um veículo existente.
* **Excluir Veículo**: Remoção de veículos do banco.
* **Interface Web**: Front-end simples para interação direta via navegador.
* **API REST**: Endpoints documentados para integração ou testes via Postman.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**
* **FastAPI** – Framework para criação da API REST.
* **Uvicorn** – Servidor ASGI para rodar o app.
* **SQLite** – Banco de dados leve e embutido.
* **SQLAlchemy** – ORM para manipulação do banco.
* **HTML + JavaScript (fetch API)** – Front-end para consumir a API.

---

## ✅ Pré-requisitos

* Python 3.10 ou superior instalado: [python.org](https://www.python.org/)
* pip atualizado para instalar dependências
* Opcional: Postman para testes de API via GUI: [postman.com](https://www.postman.com/)

---

## ⚙️ Como Rodar o Projeto

1. Clone o repositório e acesse a pasta:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd api-veiculos
   ```

2. (Opcional) Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   venv\Scripts\activate       # Windows
   source venv/bin/activate    # Linux/Mac
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o servidor FastAPI:

   ```bash
   uvicorn main:app --reload
   ```

5. Acesse a API em `http://127.0.0.1:8000`.

---

## 🧪 Como Usar

### A) Via Interface Web (HTML + JavaScript)

* Abra `static/index.html` em seu navegador (basta dar um duplo clique no arquivo).
* Use o formulário para adicionar veículos.
* A lista exibirá todos os veículos, com opções para editar e excluir.
* A edição carrega os dados no formulário para modificação e salvamento.

### B) Via Postman (ou qualquer cliente REST)

1. **Listar veículos (GET)**

   * Método: GET
   * URL: `http://127.0.0.1:8000/veiculos`
   * Clique em "Send" para visualizar todos os veículos.

2. **Adicionar veículo (POST)**

   * Método: POST
   * URL: `http://127.0.0.1:8000/veiculos`
   * Body (JSON):

     ```json
     {
       "modelo": "Onix",
       "marca": "Chevrolet",
       "ano": 2023
     }
     ```
   * Envie a requisição para criar um veículo.

3. **Editar veículo (PUT)**

   * Método: PUT
   * URL: `http://127.0.0.1:8000/veiculos/{id}` (substitua `{id}` pelo ID real)
   * Body (JSON):

     ```json
     {
       "modelo": "Onix LT",
       "marca": "Chevrolet",
       "ano": 2024
     }
     ```
   * Envie para atualizar o veículo.

4. **Excluir veículo (DELETE)**

   * Método: DELETE
   * URL: `http://127.0.0.1:8000/veiculos/{id}` (substitua `{id}`)
   * Envie para remover o veículo.

---

## 📄 Documentação da API

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
  Interface interativa para testar os endpoints.

* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
  Documentação detalhada da API.

---

## 📁 Estrutura do Projeto

```
api-veiculos/
├── main.py              # Roteamento e lógica FastAPI
├── models.py            # Modelos SQLAlchemy
├── database.py          # Configuração do SQLite
├── schemas.py           # Schemas Pydantic
├── crud.py              # Funções CRUD reutilizáveis
├── requirements.txt     # Dependências Python
└── static/
    └── index.html       # Front-end estático (HTML + JS)
```

---

## 📝 Observações

* O front-end usa fetch API para comunicação com a API FastAPI.
* A aplicação segue padrões REST, com endpoints organizados e verbos HTTP apropriados.
* O banco de dados SQLite é local, fácil para testes e desenvolvimento.
* Para produção, configure permissões CORS e segurança adequadas.