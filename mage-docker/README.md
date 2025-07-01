# Bees-breweries-data-engineering 


   Este pipeline de dados, desenvolvido com Mage.ai e executado em containers Docker, realiza a ingestão de dados da API Open Brewery DB. O processamento e a transformação dos dados são realizados utilizando o Apache Spark, com base na arquitetura Medallion. Os dados passam por três camadas de tratamento: são inicialmente ingeridos como dados brutos na camada Bronze, transformados e limpos na camada Silver, e posteriormente agregados e enriquecidos na camada Gold. Todo o fluxo é orquestrado pelo Mage.ai, que garante automação contínua e gerenciamento eficiente das tarefas. O armazenamento final dos dados processados em cada camada é feito em um banco de dados PostgreSQL, também executado em ambiente Docker, oferecendo persistência estruturada e fácil integração com ferramentas analíticas


  # Estrutura do Projeto
  
 ## Arquitetura do Pipeline de Dados – Open Brewery DB
 
-    Orquestração: Mage.ai (executando em Docker)
-    Ingestão de Dados: API pública Open Brewery DB
-    Processamento: Apache Spark
-    Armazenamento: PostgreSQL (container Docker)
-    Administração e Visualização dos Dados: pgAdmin
  
##  Arquitetura Camadas Aplicada:
  
-    Bronze: Ingestão de dados brutos
-    Silver: Limpeza e transformação
-    Gold: Enriquecimento e agregações
![Processo_BESS](https://github.com/user-attachments/assets/1ed9b55c-bc5f-433b-92d9-017c09ed9ff0)


#  Pré-requisitos
-   Docker instalado na maquina.

# Passos de Instalação
1.  Crie o diretório do projeto Mage.ai (caso não exista);
-     mkdir -p default_project
  
2.  Clone o Repositório
    no terminal, dentro do diretório do projeto:
 -      git clone https://github.com/Gabriellr/bees-breweries-data-engineering.git
        cd projeto
        cp dev.env .env
        rm dev.env
        docker compose up
    Esse comando irá iniciar os serviços:
-      docker compose up
    
  - mage.ai: http://localhost:6789 ou (http://127.0.0.1:6789)
  - pgAdmin: http://localhost:8080

#    Acessos
  ## pgAdmin
  - URL: http://localhost:8080
  - Email: user@localhost.com
  - Senha: breweries
## PostgreSQL
 - Host: postgres
 - porta: 5432
 - Usuário: airflow
 - Senha: airflow
 - Banco: breweries

#   Pipeline em execução
   ## Interface Mage
- Para adicionar o projeto no Mage clique no botão New pipeline e depois clique no menu Import pipeline zip e importe todos os arquivos.(Estão na pasta Marge_projeto)
  - camada_bronze.zip
  - camada_prata.zip
  - camada_ouro.zip
  ![interface](https://github.com/user-attachments/assets/583aa670-e29d-46c6-9041-8f05cca499b0)

  Verificação configuração arquivo io_config.yaml
     - Certifique que o arquivo esteja com a configuração do  Postgres conforme imagem abaixo:
     - http://127.0.0.1:6789/pipelines/camada_bronze/edit?sideview=tree
       ![image](https://github.com/user-attachments/assets/cd65777f-21d2-41cb-85e6-8f7dcdd49a56)

#   Arquitetura de pipeline   
![image](https://github.com/user-attachments/assets/f431cb22-23b3-42be-aba9-6e705dd9e603)

 Os pipelenes estão com Schedules para roda um horaio programado
![image](https://github.com/user-attachments/assets/55435427-d604-4c48-9572-ec7777b74b3b)

## Ordem de execução do pipelines manual
  - camada_bronze
  - camada_prata
  - camada_ouro

1. Camada Bronze - Ingerir Dados Brutos
 - Este processo busca dados da API do Open Brewery DB, processa-os e carrega-os no armazenamento no PostgreSQL no formato padrão. Ele utiliza o Apache Spark para processamento de dados e utiliza funções Python para gerenciar operações de arquivo e interações no PostgreSQL. O pipeline tem uma etapa que buscar dados por paginação. E depois faz a gravação no banco de dados PostgreSQL.

2. Camada de Prata - Transformar Dados
  - Ler os dados camada Bronze que foi gravados em uma tabela do PostgreSQL, transformando os valores os valores nulos com base no tipo de dados, selecionandos as colunas mais importantes e gravando os dados em outra tabela do PostgreSQL camada Prata.
   
3. Camada Ouro - Enriquecer e Agregar dados
  - Ler dados da camada Prata, agrega dados das colunas brewery type, city, e grava os dados em uma tabela no PostgreSQL camada Ouro.
    
Mage, cria tabela caso não exista e trunca os dados em cada execuçao, evitado que precise criar um fluxo para fazer isso.
    

# Monitoramento
 O monitoramento de pipelines no Mage.ai pode ser feito diretamente pela interface web da ferramenta, com suporte a logs, visualização em tempo real, alertas e histórico de execuções. 
 

# Teste
  Mage existe uma função @test onde se pode testar o codigo.
  
  ![image](https://github.com/user-attachments/assets/4975f93e-0789-4821-aeff-81592bd75dfa)
  
# Tratamento de erros
  Em caso de falhas nas execuções dos pipelines, o Mage enviara um alerta via canal do Slack informado o erro.
![image](https://github.com/user-attachments/assets/770daae1-2031-4d02-9bbc-bb792e2bd5de)



