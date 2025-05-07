# Gerador de Relatórios de Vendas

Este projeto é um sistema que gera relatórios de vendas a partir de diferentes fontes de dados. Ele foi desenvolvido para automatizar a geração de relatórios para pequenos negócios, simplificando o processo de consolidação e apresentação de dados de vendas.

## Funcionalidades

* **Leitura de Dados de Múltiplas Fontes:** O sistema é capaz de ler dados de vendas de diferentes fontes, como arquivos CSV locais e (futuramente) fontes de dados web.
* **Consolidação de Dados:** Os dados de vendas de diferentes fontes são consolidados em uma estrutura unificada para facilitar a geração de relatórios.
* **Geração de Relatórios em Diferentes Formatos:** O sistema pode gerar relatórios de vendas em diferentes formatos, como texto simples e HTML.
* **Configuração Flexível:** As fontes de dados a serem utilizadas são configuradas externamente através de um arquivo JSON, permitindo fácil adaptação a diferentes cenários.
* **Distribuição Simplificada:** A aplicação é distribuída como um executável, eliminando a necessidade de instalar Python ou bibliotecas.

## Uso Básico

1.  **Configurar as Fontes de Dados:**

    * Crie um arquivo `config.json` no mesmo diretório do executável para especificar as fontes de dados a serem utilizadas.
    * Consulte o exemplo de `config.json` abaixo para a estrutura do arquivo.
    * Certifique-se de que os caminhos para os arquivos CSV estejam corretos.

2.  **Executar a Aplicação:**

    * Execute o arquivo executável.
    * A aplicação irá ler as fontes de dados configuradas, consolidar os dados e gerar os relatórios em formato texto e HTML, exibindo-os no console.

## Exemplo de `config.json`

```json
{
  "sources": [
    {
      "type": "local",
      "location": "vendas.csv"
    },
    {
      "type": "web",
      "location": "[https://exemplo.com/vendas](https://exemplo.com/vendas)",
      "credentials": {
        "username": "usuario",
        "password": "senha"
      }
    }
  ]
}