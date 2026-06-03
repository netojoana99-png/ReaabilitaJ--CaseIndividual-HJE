# SaúdeConectada Nordeste – Sistema de Monitoramento de Pacientes

## Descrição do Projeto

O SaúdeConectada Nordeste é uma aplicação web desenvolvida para auxiliar profissionais da saúde no acompanhamento remoto de pacientes. O sistema permite cadastrar pacientes, registrar sinais vitais, armazenar observações clínicas e consultar o histórico de atendimentos de forma simples e organizada.

A plataforma foi projetada para facilitar o monitoramento contínuo dos pacientes, centralizando informações importantes em um único ambiente digital e possibilitando acesso rápido aos dados clínicos registrados.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

* Cadastro de pacientes.
* Registro de sinais vitais, incluindo:

  * Frequência cardíaca.
  * Pressão arterial.
  * Saturação de oxigênio.
  * Temperatura corporal.
  * Frequência respiratória.
  * Glicemia.
* Registro de observações clínicas.
* Visualização detalhada dos dados de cada paciente.
* Consulta do histórico de atendimentos.
* Atualização em tempo real através de requisições assíncronas.
* Armazenamento persistente dos dados em arquivos JSON.

## Tecnologias Utilizadas

### Backend

* Python
* Flask
* Flask-CORS

### Frontend

* HTML5
* CSS3
* JavaScript
* Fetch API

### Persistência de Dados

* Arquivos JSON

## Estrutura do Projeto

```text
saudeconectada-nordeste/
│
├── app.py
├── prontuarios.json
├── requirements.txt
├── README.md
│
└── static/
    ├── index.html
    ├── style.css
    └── script.js
```

## Pré-requisitos

* Python 3.10 ou superior
* Pip instalado

## Como Executar o Projeto

1. Clonar o repositório.
2. Acessar a pasta do projeto.
3. Instalar as dependências:

```bash
pip install -r requirements.txt
```

4. Executar a aplicação:

```bash
python app.py
```

5. Abrir o navegador e acessar:

```text
http://localhost:5000
```

## Rotas Disponíveis

### GET /api/pacientes

Retorna a lista completa de pacientes cadastrados.

### GET /api/pacientes/<id>

Retorna os dados detalhados de um paciente específico.

### POST /api/pacientes

Realiza o cadastro de um novo paciente.

### PUT /api/pacientes/<id>

Atualiza as informações de um paciente existente.

### DELETE /api/pacientes/<id>

Remove um paciente do sistema.

## Dados Armazenados

Cada paciente pode possuir os seguintes registros:

* Nome completo.
* Idade.
* Sexo.
* Diagnóstico.
* Frequência cardíaca.
* Pressão arterial.
* Saturação de oxigênio.
* Temperatura corporal.
* Frequência respiratória.
* Glicemia.
* Observações clínicas.
* Data e hora do registro.

## Arquivos de Configuração

### requirements.txt

Contém todas as dependências necessárias para execução do projeto.

### prontuarios.json

Arquivo responsável pelo armazenamento persistente dos dados dos pacientes.

## Objetivo do Projeto

O sistema foi desenvolvido com o objetivo de demonstrar uma solução simples e funcional para monitoramento remoto de pacientes, permitindo que profissionais da saúde acompanhem informações clínicas importantes de maneira centralizada e acessível.

## Autor

Joana Mascarenhas Nogueira Neto
