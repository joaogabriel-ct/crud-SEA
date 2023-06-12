# crud-SEA
CRUD WEB, seguindo os parâmetros solicitados no e-mail. 

Realizado o CRUD conforme solicitado, realizando todas as operações.
Opreções:
/insert e /new: para criar e inputar os dados dentro do Banco de dados.
/update e /edit: para realizar o update da linha do banco de dados.
/delete: apenas por requisição delete via API, para que possa ter mais controle nos dados. 

Serviço Criado em python:
Framework: FastAPI
server: Uvicorn
Banco de dados realizado PostgreSQL, o banco de dados já está online na nuvem no site Railray 

Seguindo a estrutura do Banco 

CREATE TABLE pessoas (
  cod_pessoa SERIAL PRIMARY KEY,
  nome VARCHAR(100),
  cpf VARCHAR(100),
  dt_nasc DATE,
  email VARCHAR(100),
  num_telefone BIGINT
);
