ReabilitaJá – Portal do Fisioterapeuta
Descrição do Projeto

O Portal do Fisioterapeuta é uma aplicação web desenvolvida para o case ReabilitaJá. O sistema permite que fisioterapeutas acompanhem a evolução dos pacientes em reabilitação, consultem o histórico recente de sessões e registrem observações clínicas. Além disso, o sistema implementa uma trilha de auditoria para registrar acessos e ações realizadas, atendendo às exigências de governança e rastreabilidade dos hospitais parceiros.

Funcionalidades

O sistema disponibiliza uma tela de listagem de pacientes contendo nome, protocolo em andamento, última sessão concluída e nível de dor mais recente. Também permite visualizar o histórico das últimas sete sessões de cada paciente, incluindo informações sobre exercícios realizados e dor relatada.

Os fisioterapeutas podem registrar observações clínicas diretamente pelo portal, recebendo uma confirmação visual sem necessidade de recarregar a página. Todas as ações relevantes são registradas em uma trilha de auditoria para garantir rastreabilidade e conformidade com os requisitos do projeto.

Tecnologias Utilizadas

O backend foi desenvolvido em Python utilizando Flask e Flask-CORS para disponibilização da API. O frontend foi construído com HTML, CSS e JavaScript, utilizando a Fetch API para comunicação assíncrona com o servidor. Os dados são armazenados em arquivos JSON para simplificar a implementação do MVP.

Estrutura do Projeto

O projeto é composto pelo arquivo principal da aplicação Flask, arquivos JSON responsáveis pelo armazenamento dos pacientes, observações e registros de auditoria, além da pasta de arquivos estáticos contendo a interface web. Também estão presentes os arquivos de configuração, documentação e gerenciamento de dependências.

Como Executar o Projeto

Para executar o sistema localmente é necessário possuir Python 3 instalado. Após clonar o repositório, as dependências devem ser instaladas através do arquivo requirements.txt. Em seguida, basta executar o arquivo principal da aplicação e acessar o endereço local disponibilizado pelo Flask através do navegador.

Rotas Disponíveis

A API disponibiliza três rotas principais:

GET /pacientes: retorna a lista de pacientes cadastrados.
GET /pacientes/<id>/historico: retorna o histórico das últimas sete sessões do paciente selecionado.
POST /pacientes/<id>/observacao: registra uma observação clínica associada ao paciente, incluindo o identificador do fisioterapeuta e o horário da ação.
Trilha de Auditoria

Para atender às exigências dos hospitais parceiros, o sistema registra informações sobre os acessos realizados pelos fisioterapeutas. Cada registro contém o profissional responsável pela ação, o paciente acessado, o recurso utilizado, a operação realizada e o momento exato em que ocorreu. Essa funcionalidade aumenta a transparência e auxilia na conformidade com requisitos de governança e proteção de dados.

Arquivos de Configuração

O projeto inclui um arquivo .env.example contendo as variáveis de ambiente necessárias para execução local e um arquivo .gitignore configurado para impedir o versionamento de informações sensíveis, ambientes virtuais e arquivos temporários.

Controle de Versão

O desenvolvimento foi documentado utilizando o padrão Conventional Commits, garantindo um histórico de alterações claro, rastreável e alinhado às boas práticas de engenharia de software.

```text
reabilitaja-portal/
│
├── app.py
├── pacientes.json
├── observacoes.json
├── auditoria.json
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
└── static/
    ├── index.html
    ├── style.css
    └── script.js
```

## Pré-requisitos

- Python 3.10 ou superior
- Pip instalado

## Como Executar o Projeto

1. Clonar o repositório.
2. Acessar a pasta do projeto.
3. Instalar as dependências com `pip install -r requirements.txt`.
4. Executar a aplicação com `python app.py`.
5. Abrir o navegador e acessar `http://localhost:5000`.

## Rotas Disponíveis

### GET /pacientes
Retorna a lista de pacientes cadastrados.

### GET /pacientes/<id>/historico
Retorna as últimas 7 sessões do paciente selecionado.

### POST /pacientes/<id>/observacao
Registra uma observação clínica contendo o identificador do fisioterapeuta, a observação realizada e o timestamp da ação.

## Trilha de Auditoria

O sistema registra as ações realizadas pelos fisioterapeutas para garantir rastreabilidade e conformidade com as exigências dos hospitais parceiros. Cada registro contém:

- Identificador do fisioterapeuta.
- Paciente acessado.
- Recurso acessado.
- Ação realizada.
- Data e hora da ação.

## Arquivos de Configuração

### .env.example

Contém as variáveis de ambiente necessárias para execução local do projeto.

### .gitignore

Impede o versionamento de arquivos sensíveis, ambientes virtuais e arquivos temporários.

## Histórico de Commits

O desenvolvimento foi documentado utilizando o padrão Conventional Commits para garantir rastreabilidade das alterações realizadas ao longo do projeto.

## Autor

Joana Mascarenhas Nogueira Neto
