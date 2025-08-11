# Gerador de Relatórios de Vendas

## 📝 Sobre o Projeto
Este projeto é um sistema que gera relatórios de vendas a partir de diferentes fontes de dados. Ele foi desenvolvido para automatizar a geração de relatórios para pequenos negócios, simplificando o processo de consolidação e apresentação de dados de vendas.

## 💻 Tecnologias Utilizadas

- Python 3.12.3
- Docker
- Pytest 

## 🛠️ Funcionalidades

* **Leitura de Dados de Múltiplas Fontes:** O sistema é capaz de ler dados de vendas de diferentes fontes, como arquivos CSV locais e (💡 planejada para o futuro) fontes de dados web.
* **Consolidação de Dados:** Os dados de vendas de diferentes fontes são consolidados em uma estrutura unificada para facilitar a geração de relatórios.
* **Geração de Relatórios em Diferentes Formatos:** O sistema pode gerar relatórios de vendas em diferentes formatos, como texto simples e HTML.
* **Configuração Flexível:** As fontes de dados a serem utilizadas são configuradas externamente através de um arquivo JSON, permitindo fácil adaptação a diferentes cenários.
* **Distribuição Simplificada:**  💡(planejada para o futuro) A aplicação é distribuída como um executável, eliminando a necessidade de instalar Python ou bibliotecas.

## 🚀 Como Executar

### **Configurar as Fontes de Dados:**

* Crie um arquivo `config.json` no mesmo diretório do projeto ou executável para especificar as fontes de dados.
* Consulte o exemplo de `config.json` abaixo para a estrutura do arquivo.
* Certifique-se de que os caminhos relativos para os arquivos CSV estejam corretos.

#### ⚙️ Exemplo de config.json

```json
{
  "sources": [
    {
      "type": "local",
      "location": "../relatorios/vendas.csv"
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
---
### **Executar a Aplicação:**

  #### Execução para cliente*
  (planejada para o futuro 💡) 
* Execute o arquivo executável.
* A aplicação irá ler as fontes de dados configuradas, consolidar os dados e gerar os relatórios em formato texto e HTML no destino.

#### ▶️ Execução para Desenvolvedor

**Pré-requisitos:**
  -  Docker instalado localmente
**Execução**
 1. Build da imagem docker do dockerfile:  
 ```sh
 docker build -t gerador_relatorio . 
 ```
2. Inicializar o container em modo iterativo: 
```sh
  docker run -it --rm -v $(pwd)/:/usr/share/rpa_projeto_relatorio/ gerador_relatorio sh
```
3. Executar o main.py dentro do container: 
```sh
  python gerador_relatorio/main.py
```

4. Executar testes unitários dentro do container:
```sh
  pytest 
```

## ✨ Demonstração de resultado
**Formatação HTML**
<!DOCTYPE html>
<html lang='pt-BR'>
<head>
    <meta charset='UTF-8'>
    <title>Relatório de Vendas</title>
    <style>
        body { font-family: sans-serif; margin: 20px; }
        h1, h2 { color: #333; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .statistics-section { margin-top: 40px; }
        .statistics-table { width: auto; }
    </style>
</head>
<body>
    <h1>Relatório de Vendas</h1>
    <h2>Dados de Vendas</h2>
    <table>
        <thead>
            <tr>
                <th>dt_sale</th>
                <th>product_name</th>
                <th>price</th>
                <th>product_id</th>
                <th>category</th>
                <th>customer_name</th>
                <th>discount</th>
                <th>store_id</th>
                <th>order_id</th>
                <th>customer_id</th>
                <th>payment_method</th>
                <th>quantity</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>2025-04-12</td>
                <td>Cinto de Couro</td>
                <td>144.88</td>
                <td>207</td>
                <td>Acessórios</td>
                <td>Sr. Juan da Mata</td>
                <td>0.04</td>
                <td>2</td>
                <td>1</td>
                <td>1003</td>
                <td>Cartão de Débito</td>
                <td>4</td>
            </tr>
            <tr>
                <td>2025-04-06</td>
                <td>Arroz</td>
                <td>50.55</td>
                <td>292</td>
                <td>Alimentos</td>
                <td>Paulo Sousa</td>
                <td>0.15</td>
                <td>2</td>
                <td>2</td>
                <td>1007</td>
                <td>Cartão de Débito</td>
                <td>3</td>
            </tr>
            <tr>
                <td>2025-04-06</td>
                <td>Macarrão</td>
                <td>137.34</td>
                <td>235</td>
                <td>Alimentos</td>
                <td>Maitê da Costa</td>
                <td>0.1</td>
                <td>3</td>
                <td>3</td>
                <td>1006</td>
                <td>Cartão de Débito</td>
                <td>4</td>
            </tr>
            <tr>
                <td>2025-04-15</td>
                <td>Camiseta Polo</td>
                <td>35.36</td>
                <td>244</td>
                <td>Roupas</td>
                <td>Dra. Eduarda Martins</td>
                <td>0.01</td>
                <td>2</td>
                <td>4</td>
                <td>1010</td>
                <td>Pix</td>
                <td>1</td>
            </tr>
            <tr>
                <td>2025-04-11</td>
                <td>Arroz</td>
                <td>73.76</td>
                <td>262</td>
                <td>Alimentos</td>
                <td>Diego Câmara</td>
                <td>0.08</td>
                <td>3</td>
                <td>5</td>
                <td>1010</td>
                <td>Cartão de Débito</td>
                <td>4</td>
            </tr>
            <tr>
                <td>2025-04-12</td>
                <td>Mochila Casual</td>
                <td>147.69</td>
                <td>168</td>
                <td>Acessórios</td>
                <td>Vitória Dias</td>
                <td>0.18</td>
                <td>3</td>
                <td>6</td>
                <td>1004</td>
                <td>Boleto</td>
                <td>3</td>
            </tr>
            <tr>
                <td>2025-04-10</td>
                <td>Pão Francês</td>
                <td>188.84</td>
                <td>160</td>
                <td>Alimentos</td>
                <td>Pietro Vieira</td>
                <td>0.01</td>
                <td>1</td>
                <td>7</td>
                <td>1008</td>
                <td>Cartão de Crédito</td>
                <td>1</td>
            </tr>
            <tr>
                <td>2025-04-13</td>
                <td>Calça Jeans</td>
                <td>121.31</td>
                <td>325</td>
                <td>Roupas</td>
                <td>Sr. Joaquim Câmara</td>
                <td>0.13</td>
                <td>3</td>
                <td>8</td>
                <td>1001</td>
                <td>Cartão de Débito</td>
                <td>1</td>
            </tr>
            <tr>
                <td>2025-04-07</td>
                <td>Bolo de Chocolate</td>
                <td>145.33</td>
                <td>271</td>
                <td>Alimentos</td>
                <td>Anthony da Costa</td>
                <td>0.12</td>
                <td>2</td>
                <td>9</td>
                <td>1001</td>
                <td>Cartão de Crédito</td>
                <td>3</td>
            </tr>
            <tr>
                <td>2025-04-14</td>
                <td>Refrigerante</td>
                <td>158.62</td>
                <td>374</td>
                <td>Alimentos</td>
                <td>Melina Rodrigues</td>
                <td>0.01</td>
                <td>1</td>
                <td>10</td>
                <td>1003</td>
                <td>Pix</td>
                <td>4</td>
            </tr>
            <tr>
                <td>2025-04-03</td>
                <td>Suco Natural</td>
                <td>34.48</td>
                <td>269</td>
                <td>Alimentos</td>
                <td>Thomas Alves</td>
                <td>0.06</td>
                <td>2</td>
                <td>11</td>
                <td>1008</td>
                <td>Cartão de Débito</td>
                <td>4</td>
            </tr>
            <tr>
                <td>2025-04-02</td>
                <td>Café</td>
                <td>29.81</td>
                <td>275</td>
                <td>Alimentos</td>
                <td>Pedro Lucas Sampaio</td>
                <td>0.07</td>
                <td>2</td>
                <td>12</td>
                <td>1001</td>
                <td>Dinheiro</td>
                <td>4</td>
            </tr>
            <tr>
                <td>2025-04-08</td>
                <td>Café</td>
                <td>169.27</td>
                <td>391</td>
                <td>Alimentos</td>
                <td>Otávio Pires</td>
                <td>0.09</td>
                <td>1</td>
                <td>13</td>
                <td>1004</td>
                <td>Cartão de Crédito</td>
                <td>1</td>
            </tr>
            <tr>
                <td>2025-04-06</td>
                <td>Arroz</td>
                <td>170.28</td>
                <td>371</td>
                <td>Alimentos</td>
                <td>Breno Novais</td>
                <td>0.18</td>
                <td>1</td>
                <td>14</td>
                <td>1002</td>
                <td>Cartão de Crédito</td>
                <td>5</td>
            </tr>
            <tr>
                <td>2025-04-11</td>
                <td>Mochila Casual</td>
                <td>94.44</td>
                <td>370</td>
                <td>Acessórios</td>
                <td>Cecilia Cunha</td>
                <td>0.09</td>
                <td>2</td>
                <td>15</td>
                <td>1010</td>
                <td>Cartão de Crédito</td>
                <td>3</td>
            </tr>
            <tr>
                <td>2025-04-15</td>
                <td>Feijão</td>
                <td>72.78</td>
                <td>158</td>
                <td>Alimentos</td>
                <td>Manuela da Paz</td>
                <td>0.03</td>
                <td>2</td>
                <td>16</td>
                <td>1006</td>
                <td>Boleto</td>
                <td>3</td>
            </tr>
            <tr>
                <td>2025-04-02</td>
                <td>Camiseta Básica</td>
                <td>112.25</td>
                <td>228</td>
                <td>Roupas</td>
                <td>Dante Rocha</td>
                <td>0.17</td>
                <td>1</td>
                <td>17</td>
                <td>1002</td>
                <td>Boleto</td>
                <td>3</td>
            </tr>
            <tr>
                <td>2025-04-07</td>
                <td>Vestido Floral</td>
                <td>67.96</td>
                <td>393</td>
                <td>Roupas</td>
                <td>Sra. Maria Flor Dias</td>
                <td>0.11</td>
                <td>1</td>
                <td>18</td>
                <td>1009</td>
                <td>Dinheiro</td>
                <td>4</td>
            </tr>
            <tr>
                <td>2025-04-13</td>
                <td>Colar de Prata</td>
                <td>43.56</td>
                <td>147</td>
                <td>Acessórios</td>
                <td>Dr. Arthur Sá</td>
                <td>0.17</td>
                <td>3</td>
                <td>19</td>
                <td>1004</td>
                <td>Cartão de Crédito</td>
                <td>4</td>
            </tr>
            <tr>
                <td>2025-04-12</td>
                <td>Cinto de Couro</td>
                <td>67.13</td>
                <td>320</td>
                <td>Acessórios</td>
                <td>Brayan Mendes</td>
                <td>0.19</td>
                <td>3</td>
                <td>20</td>
                <td>1003</td>
                <td>Cartão de Crédito</td>
                <td>2</td>
            </tr>
        </tbody>
    </table>
    <div class='statistics-section'>
        <h2>Estatísticas</h2>
        <table class='statistics-table'>
            <thead>
                <tr>
                    <th>Métrica</th>
                    <th>Mínimo</th>
                    <th>Máximo</th>
                    <th>Contagem de Nulos</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>dt_sale</td>
                    <td>None</td>
                    <td>None</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>product_name</td>
                    <td>None</td>
                    <td>None</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>price</td>
                    <td>29.81</td>
                    <td>188.84</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>product_id</td>
                    <td>147.0</td>
                    <td>393.0</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>category</td>
                    <td>None</td>
                    <td>None</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>customer_name</td>
                    <td>None</td>
                    <td>None</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>discount</td>
                    <td>0.01</td>
                    <td>0.19</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>store_id</td>
                    <td>1.0</td>
                    <td>3.0</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>order_id</td>
                    <td>1.0</td>
                    <td>20.0</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>customer_id</td>
                    <td>1001.0</td>
                    <td>1010.0</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>payment_method</td>
                    <td>None</td>
                    <td>None</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>quantity</td>
                    <td>1.0</td>
                    <td>5.0</td>
                    <td>0</td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>

**Formatação TXT**
---
 ====================== Relatório de Vendas ======================
Dados de Vendas:

category | product_name | customer_name | order_id | product_id | price | discount | dt_sale | customer_id | payment_method | store_id | quantity
-------------------------------------------------------------------------------------------------------------------------------------------------
Acessórios | Cinto de Couro | Sr. Juan da Mata | 1 | 207 | 144.88 | 0.04 | 2025-04-12 | 1003 | Cartão de Débito | 2 | 4
Alimentos | Arroz | Paulo Sousa | 2 | 292 | 50.55 | 0.15 | 2025-04-06 | 1007 | Cartão de Débito | 2 | 3
Alimentos | Macarrão | Maitê da Costa | 3 | 235 | 137.34 | 0.1 | 2025-04-06 | 1006 | Cartão de Débito | 3 | 4
Roupas | Camiseta Polo | Dra. Eduarda Martins | 4 | 244 | 35.36 | 0.01 | 2025-04-15 | 1010 | Pix | 2 | 1
Alimentos | Arroz | Diego Câmara | 5 | 262 | 73.76 | 0.08 | 2025-04-11 | 1010 | Cartão de Débito | 3 | 4
Acessórios | Mochila Casual | Vitória Dias | 6 | 168 | 147.69 | 0.18 | 2025-04-12 | 1004 | Boleto | 3 | 3
Alimentos | Pão Francês | Pietro Vieira | 7 | 160 | 188.84 | 0.01 | 2025-04-10 | 1008 | Cartão de Crédito | 1 | 1
Roupas | Calça Jeans | Sr. Joaquim Câmara | 8 | 325 | 121.31 | 0.13 | 2025-04-13 | 1001 | Cartão de Débito | 3 | 1
Alimentos | Bolo de Chocolate | Anthony da Costa | 9 | 271 | 145.33 | 0.12 | 2025-04-07 | 1001 | Cartão de Crédito | 2 | 3
Alimentos | Refrigerante | Melina Rodrigues | 10 | 374 | 158.62 | 0.01 | 2025-04-14 | 1003 | Pix | 1 | 4
Alimentos | Suco Natural | Thomas Alves | 11 | 269 | 34.48 | 0.06 | 2025-04-03 | 1008 | Cartão de Débito | 2 | 4
Alimentos | Café | Pedro Lucas Sampaio | 12 | 275 | 29.81 | 0.07 | 2025-04-02 | 1001 | Dinheiro | 2 | 4
Alimentos | Café | Otávio Pires | 13 | 391 | 169.27 | 0.09 | 2025-04-08 | 1004 | Cartão de Crédito | 1 | 1
Alimentos | Arroz | Breno Novais | 14 | 371 | 170.28 | 0.18 | 2025-04-06 | 1002 | Cartão de Crédito | 1 | 5
Acessórios | Mochila Casual | Cecilia Cunha | 15 | 370 | 94.44 | 0.09 | 2025-04-11 | 1010 | Cartão de Crédito | 2 | 3
Alimentos | Feijão | Manuela da Paz | 16 | 158 | 72.78 | 0.03 | 2025-04-15 | 1006 | Boleto | 2 | 3
Roupas | Camiseta Básica | Dante Rocha | 17 | 228 | 112.25 | 0.17 | 2025-04-02 | 1002 | Boleto | 1 | 3
Roupas | Vestido Floral | Sra. Maria Flor Dias | 18 | 393 | 67.96 | 0.11 | 2025-04-07 | 1009 | Dinheiro | 1 | 4
Acessórios | Colar de Prata | Dr. Arthur Sá | 19 | 147 | 43.56 | 0.17 | 2025-04-13 | 1004 | Cartão de Crédito | 3 | 4
Acessórios | Cinto de Couro | Brayan Mendes | 20 | 320 | 67.13 | 0.19 | 2025-04-12 | 1003 | Cartão de Crédito | 3 | 2
===========================================================
Estatísticas:

  - Coluna: category
    Mínimo: N/A
    Máximo: N/A
    Nulos: 0

  - Coluna: product_name
    Mínimo: N/A
    Máximo: N/A
    Nulos: 0

  - Coluna: customer_name
    Mínimo: N/A
    Máximo: N/A
    Nulos: 0

  - Coluna: order_id
    Mínimo: 1.0
    Máximo: 20.0
    Nulos: 0

  - Coluna: product_id
    Mínimo: 147.0
    Máximo: 393.0
    Nulos: 0

  - Coluna: price
    Mínimo: 29.81
    Máximo: 188.84
    Nulos: 0

  - Coluna: discount
    Mínimo: 0.01
    Máximo: 0.19
    Nulos: 0

  - Coluna: dt_sale
    Mínimo: N/A
    Máximo: N/A
    Nulos: 0

  - Coluna: customer_id
    Mínimo: 1001.0
    Máximo: 1010.0
    Nulos: 0

  - Coluna: payment_method
    Mínimo: N/A
    Máximo: N/A
    Nulos: 0

  - Coluna: store_id
    Mínimo: 1.0
    Máximo: 3.0
    Nulos: 0

  - Coluna: quantity
    Mínimo: 1.0
    Máximo: 5.0
    Nulos: 0


---


# Melhorias Futuras
  - **utilizar Pandas**: O projeto foi arquitetado com simplicidade e desempenho em mente para conjuntos de dados de pequeno a médio porte. Atualmente, a manipulação de dados é feita com listas e dicionários Python padrão, uma abordagem leve e direta. Como melhoria futura, caso o volume de dados ou a complexidade das análises cresça, a implementação poderá ser refatorada para utilizar a biblioteca Pandas.
  