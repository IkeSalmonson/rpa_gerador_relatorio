import csv
import random
from datetime import datetime, timedelta
from faker import Faker

# Inicializa o Faker para gerar dados em português do Brasil
fake = Faker('pt_BR')

# Define as colunas do arquivo CSV
colunas_1 = [
    "order_id", "product_id", "product_name", "category", "price",
    "quantity", "discount", "dt_sale", "customer_id", "customer_name",
    "payment_method", "store_id"
]

colunas_2 = [
    "order_id", "product_id", "product_name", "category", "price",
    "quantity",  "dt_sale", "customer_id",  
    "payment_method", "store_id"
]


# Número de linhas de dados
num_linhas = 20

# Data de início e fim do período de vendas
data_inicio = datetime(2025, 4, 1)
data_fim = datetime(2025, 4, 15)

# Métodos de pagamento possíveis
metodos_pagamento = ["Cartão de Crédito", "Cartão de Débito", "Dinheiro", "Pix", "Boleto"]

# Categorias de produtos possíveis (REDUZIDO)
categorias = ["Roupas", "Acessórios", "Alimentos"]

# Nomes de produtos possíveis (AJUSTADO PARA AS CATEGORIAS)
nomes_produtos = {
    "Roupas": ["Camiseta Básica", "Calça Jeans", "Camiseta Polo", "Saia Longa", "Vestido Floral"],
    "Acessórios": ["Mochila Casual", "Óculos de Sol", "Cinto de Couro", "Colar de Prata", "Chapéu de Palha"],
    "Alimentos": ["Pão Francês", "Bolo de Chocolate", "Café", "Arroz", "Feijão", "Macarrão", "Refrigerante", "Suco Natural"]
}


# Gera os dados
dados1 = []
for i in range(num_linhas):
    data_venda = data_inicio + timedelta(days=random.randint(0, (data_fim - data_inicio).days))
    
    categoria = random.choice(categorias) # Seleciona aleatoriamente uma das 3 categorias
    nome_produto = random.choice(nomes_produtos[categoria]) # Seleciona um produto aleatório da categoria
    
    dados1.append({
        "order_id": i + 1,
        "product_id": random.randint(100, 400),
        "product_name": nome_produto,
        "category": categoria,
        "price": round(random.uniform(10, 200), 2),
        "quantity": random.randint(1, 5),
        "discount": round(random.uniform(0, 0.2), 2),
        "dt_sale": data_venda.strftime("%Y-%m-%d"),
        "customer_id": random.randint(1001, 1010),
        "customer_name": fake.name(),
        "payment_method": metodos_pagamento[random.randint(0, len(metodos_pagamento) - 1)],
        "store_id": random.randint(1, 3)
    })


# Gera os dados2
dados2 = []
for i in range(num_linhas):
    data_venda = data_inicio + timedelta(days=random.randint(0, (data_fim - data_inicio).days))
    
    categoria = random.choice(categorias) # Seleciona aleatoriamente uma das 3 categorias
    nome_produto = random.choice(nomes_produtos[categoria]) # Seleciona um produto aleatório da categoria
    
    dados2.append({
        "order_id": i + 1,
        "product_id": random.randint(100, 400),
        "product_name": nome_produto,
        "category": categoria,
        "price": round(random.uniform(10, 200), 2),
        "quantity": random.randint(1, 5),
         "dt_sale": data_venda.strftime("%Y-%m-%d"),
                 "customer_id": random.randint(1001, 1010),
         "payment_method": metodos_pagamento[random.randint(0, len(metodos_pagamento) - 1)],
        "store_id": random.randint(1, 3)
    })


# Salva os dados1 em um arquivo CSV
nome_arquivo_csv = f"vendas_especificas_{data_inicio}.csv"
with open( "colunas_1"+nome_arquivo_csv, mode="w", newline="", encoding="utf-8") as arquivo_csv:
    writer = csv.DictWriter(arquivo_csv, fieldnames=colunas_1)
    writer.writeheader()
    writer.writerows(dados1)

print(f"Arquivo CSV '{nome_arquivo_csv}' gerado com sucesso.")

# Salva os dados2 em um arquivo CSV
with open( "colunas_2"+nome_arquivo_csv, mode="w", newline="", encoding="utf-8") as arquivo_csv:
    writer = csv.DictWriter(arquivo_csv, fieldnames=colunas_2)
    writer.writeheader()
    writer.writerows(dados2)
print(f"Arquivo CSV '{nome_arquivo_csv}' gerado com sucesso.")