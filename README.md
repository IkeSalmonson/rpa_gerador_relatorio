# Gerador de Relatórios de Vendas

## 📝 Descrição
Este projeto é um sistema que gera relatórios de vendas a partir de diferentes fontes de dados. Ele foi desenvolvido para automatizar a geração de relatórios para pequenos negócios, simplificando o processo de consolidação e apresentação de dados de vendas.

## 💻 Tecnologias Utilizadas
[Liste as principais tecnologias, frameworks e bibliotecas usadas. Exemplo:]
- Python 3.12.3
- Docker
- Pytest 

## Funcionalidades

* **Leitura de Dados de Múltiplas Fontes:** O sistema é capaz de ler dados de vendas de diferentes fontes, como arquivos CSV locais e (futuramente) fontes de dados web.
* **Consolidação de Dados:** Os dados de vendas de diferentes fontes são consolidados em uma estrutura unificada para facilitar a geração de relatórios.
* **Geração de Relatórios em Diferentes Formatos:** O sistema pode gerar relatórios de vendas em diferentes formatos, como texto simples e HTML.
* **Configuração Flexível:** As fontes de dados a serem utilizadas são configuradas externamente através de um arquivo JSON, permitindo fácil adaptação a diferentes cenários.
* **Distribuição Simplificada:** A aplicação é distribuída como um executável, eliminando a necessidade de instalar Python ou bibliotecas.

## 🚀 Como Executar

1.  **Configurar as Fontes de Dados:**

    * Crie um arquivo `config.json` no mesmo diretório do executável para especificar as fontes de dados a serem utilizadas.
    * Consulte o exemplo de `config.json` abaixo para a estrutura do arquivo.
    * Certifique-se de que os caminhos para os arquivos CSV estejam corretos.


### Exemplo de `config.json`

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
```

2.  **Executar a Aplicação:**
  ### Execução para cliente
    * Execute o arquivo executável.
    * A aplicação irá ler as fontes de dados configuradas, consolidar os dados e gerar os relatórios em formato texto e HTML, exibindo-os no console.



### Execução para desenvolvedor 

**Pré-requisitos:**
  -  Docker 
 Build 
 ```sh
 docker build -t gerador_relatorio . 
 ```
Execução da aplicação 
<br> Container: 

```sh
  docker run -it -v .$(pwd)/:/usr/share/rpa_projeto_relatorio/ gerador_relatorio sh
```

Dentro do container execute: 
```sh
  python /gerador_relatorio/main.py
```

## Demonstração de resultado

<h1>Relatório de Vendas</h1><table><tr><th>order_id</th><th>product_id</th><th>product_name</th><th>category</th><th>price</th><th>quantity</th><th>discount</th><th>dt_sale</th><th>customer_id</th><th>customer_name</th><th>payment_method</th><th>store_id</th></tr><tr><td>2</td><td>292</td><td>Arroz</td><td>Alimentos</td><td>50.55</td><td>3</td><td>0.15</td><td>2025-04-06</td><td>1007</td><td>Paulo Sousa</td><td>Cartão de Débito</td><td>2</td></tr><tr><td>3</td><td>235</td><td>Macarrão</td><td>Alimentos</td><td>137.34</td><td>4</td><td>0.1</td><td>2025-04-06</td><td>1006</td><td>Maitê da Costa</td><td>Cartão de Débito</td><td>3</td></tr><tr><td>4</td><td>244</td><td>Camiseta Polo</td><td>Roupas</td><td>35.36</td><td>1</td><td>0.01</td><td>2025-04-15</td><td>1010</td><td>Dra. Eduarda Martins</td><td>Pix</td><td>2</td></tr><tr><td>5</td><td>262</td><td>Arroz</td><td>Alimentos</td><td>73.76</td><td>4</td><td>0.08</td><td>2025-04-11</td><td>1010</td><td>Diego Câmara</td><td>Cartão de Débito</td><td>3</td></tr><tr><td>6</td><td>168</td><td>Mochila Casual</td><td>Acessórios</td><td>147.69</td><td>3</td><td>0.18</td><td>2025-04-12</td><td>1004</td><td>Vitória Dias</td><td>Boleto</td><td>3</td></tr><tr><td>7</td><td>160</td><td>Pão Francês</td><td>Alimentos</td><td>188.84</td><td>1</td><td>0.01</td><td>2025-04-10</td><td>1008</td><td>Pietro Vieira</td><td>Cartão de Crédito</td><td>1</td></tr><tr><td>8</td><td>325</td><td>Calça Jeans</td><td>Roupas</td><td>121.31</td><td>1</td><td>0.13</td><td>2025-04-13</td><td>1001</td><td>Sr. Joaquim Câmara</td><td>Cartão de Débito</td><td>3</td></tr><tr><td>9</td><td>271</td><td>Bolo de Chocolate</td><td>Alimentos</td><td>145.33</td><td>3</td><td>0.12</td><td>2025-04-07</td><td>1001</td><td>Anthony da Costa</td><td>Cartão de Crédito</td><td>2</td></tr><tr><td>10</td><td>374</td><td>Refrigerante</td><td>Alimentos</td><td>158.62</td><td>4</td><td>0.01</td><td>2025-04-14</td><td>1003</td><td>Melina Rodrigues</td><td>Pix</td><td>1</td></tr><tr><td>11</td><td>269</td><td>Suco Natural</td><td>Alimentos</td><td>34.48</td><td>4</td><td>0.06</td><td>2025-04-03</td><td>1008</td><td>Thomas Alves</td><td>Cartão de Débito</td><td>2</td></tr><tr><td>12</td><td>275</td><td>Café</td><td>Alimentos</td><td>29.81</td><td>4</td><td>0.07</td><td>2025-04-02</td><td>1001</td><td>Pedro Lucas Sampaio</td><td>Dinheiro</td><td>2</td></tr><tr><td>13</td><td>391</td><td>Café</td><td>Alimentos</td><td>169.27</td><td>1</td><td>0.09</td><td>2025-04-08</td><td>1004</td><td>Otávio Pires</td><td>Cartão de Crédito</td><td>1</td></tr><tr><td>14</td><td>371</td><td>Arroz</td><td>Alimentos</td><td>170.28</td><td>5</td><td>0.18</td><td>2025-04-06</td><td>1002</td><td>Breno Novais</td><td>Cartão de Crédito</td><td>1</td></tr><tr><td>15</td><td>370</td><td>Mochila Casual</td><td>Acessórios</td><td>94.44</td><td>3</td><td>0.09</td><td>2025-04-11</td><td>1010</td><td>Cecilia Cunha</td><td>Cartão de Crédito</td><td>2</td></tr><tr><td>16</td><td>158</td><td>Feijão</td><td>Alimentos</td><td>72.78</td><td>3</td><td>0.03</td><td>2025-04-15</td><td>1006</td><td>Manuela da Paz</td><td>Boleto</td><td>2</td></tr><tr><td>17</td><td>228</td><td>Camiseta Básica</td><td>Roupas</td><td>112.25</td><td>3</td><td>0.17</td><td>2025-04-02</td><td>1002</td><td>Dante Rocha</td><td>Boleto</td><td>1</td></tr><tr><td>18</td><td>393</td><td>Vestido Floral</td><td>Roupas</td><td>67.96</td><td>4</td><td>0.11</td><td>2025-04-07</td><td>1009</td><td>Sra. Maria Flor Dias</td><td>Dinheiro</td><td>1</td></tr><tr><td>19</td><td>147</td><td>Colar de Prata</td><td>Acessórios</td><td>43.56</td><td>4</td><td>0.17</td><td>2025-04-13</td><td>1004</td><td>Dr. Arthur Sá</td><td>Cartão de Crédito</td><td>3</td></tr><tr><td>20</td><td>320</td><td>Cinto de Couro</td><td>Acessórios</td><td>67.13</td><td>2</td><td>0.19</td><td>2025-04-12</td><td>1003</td><td>Brayan Mendes</td><td>Cartão de Crédito</td><td>3</td></tr></table>