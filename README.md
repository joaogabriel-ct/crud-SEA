# CRUD

Este é um projeto de um CRUD (Create, Read, Update, Delete) WEB desenvolvido em Python.

## Funcionalidades

O projeto permite realizar as seguintes operações:

- `/insert` e `/new`: criação e inserção de dados na tabela "pessoas" do banco de dados.
- `/update` e `/edit`: atualização de linhas existentes na tabela "pessoas" do banco de dados.
- `/delete`: exclusão de registros por meio de requisições DELETE via API.

## Tecnologias Utilizadas

- Framework: FastAPI
- Servidor: Uvicorn
- Banco de Dados: PostgreSQL (o banco de dados está hospedado na nuvem no site Railray)

## Estrutura do Banco de Dados

A tabela "pessoas" possui a seguinte estrutura:

CREATE TABLE pessoas (
cod_pessoa SERIAL PRIMARY KEY,
nome VARCHAR(100),
cpf VARCHAR(100),
dt_nasc DATE,
email VARCHAR(100),
num_telefone BIGINT
);


As credenciais já estão no projeto o Banco está online

Para executar o projeto, siga as etapas abaixo:

1. Clone o repositório para o seu ambiente local.
2. Instale as dependências do projeto executando o comando `pip install -r requirements.txt`.
3. Execute o servidor utilizando o comando `uvicorn main:app --reload`.
4. Acesse a interface do projeto em um navegador através da URL fornecida pelo FastAPI.
