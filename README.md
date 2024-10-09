# Projeto API Flask

Esta é uma API de teste desenvolvida em Flask para fins de estudo.

## Funcionalidades

- **GET /**: Retorna "Minha primeira Api!"
- **GET /users**: Retorna a lista de usuários.
- **GET /users/<id>**: Retorna um usuário específico.
- **POST /users**: Adiciona um novo usuário.
- **PUT /users/<id>**: Atualiza um usuário existente.
- **DELETE /users/<id>**: Remove um usuário.

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x
- Pip

### Passo a Passo

### Passo a Passo

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/projeto_api.git
    ```

2. **Navegue até o diretório do projeto:**

    ```bash
    cd projeto_api
    ```

3. **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv .venv
    ```

    **Ativar o ambiente virtual:**

    - **No Windows:**
    
        ```bash
        .venv\Scripts\activate
        ```
    
    - **No macOS e Linux:**
    
        ```bash
        source .venv/bin/activate
        ```

4. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Execute a aplicação:**

    ```bash
    python app.py
    ```

6. **Acesse a API no navegador:**

    Abra [http://127.0.0.1:5000/](http://127.0.0.1:5000/) no seu navegador.

## Tecnologias Utilizadas

- Python
- Flask

## Estrutura do Projeto

  projeto_api/ │ ├── .venv/ ├── app.py ├── routes/ │ ├── init.py │ └── users.py ├── models/ │ ├── init.py │ └── user.py ├── requirements.txt └── README.md


## Como Contribuir

1. **Faça um fork do projeto.**
2. **Crie uma branch para sua feature:**

    ```bash
    git checkout -b minha-nova-feature
    ```

3. **Faça as alterações necessárias e commit:**

    ```bash
    git commit -m "Adicionar nova funcionalidade"
    ```

4. **Envie para o branch no GitHub:**

    ```bash
    git push origin minha-nova-feature
    ```

5. **Abra um Pull Request.**


## Testes

Para executar os testes, utilize o seguinte comando:

```bash
pytest
````

## Exemplos de Uso

**Obter todos os usuários:**

```bash
curl http://127.0.0.1:5000/users
```

***Adicionar um novo usuário:***

```bash 
 curl -X POST -H "Content-Type: application/json" -d '{"id": 3, "name": "Charlie"}' http://127.0.0.1:5000/users
```

   

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
![License](https://img.shields.io/badge/license-MIT-blue.svg)


   

