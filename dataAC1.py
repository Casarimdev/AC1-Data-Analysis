import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

sns.set_theme(style="whitegrid")

# Gerando dados fictícios
np.random.seed(42)
dates = pd.date_range(start="2024-01-01", periods=100, freq="D")
products = ["Notebook", "Smartphone", "Tablet", "Monitor", "Teclado", "Mouse"]
categories = {"Notebook": "Eletrônicos", "Smartphone": "Eletrônicos", "Tablet": "Eletrônicos", "Monitor": "Eletrônicos", "Teclado": "Acessórios", "Mouse": "Acessórios"}

# Criando DataFrame com vendas fictícias
data = {
    "Data": np.random.choice(dates, 100),
    "Produto": np.random.choice(products, 100),
    "Quantidade": np.random.randint(1, 10, 100),
    "Preco_Unitario": np.random.uniform(100, 5000, 100)
}
df = pd.DataFrame(data)
df["Categoria"] = df["Produto"].map(categories)
df["Receita_Total"] = df["Quantidade"] * df["Preco_Unitario"]

# Estatísticas descritivas
def estatisticas_descritivas(df):
    print("\n### Estatísticas Descritivas ###\n")
    print(df.describe())

# Gráfico de distribuição de receita
def grafico_receita(df):
    plt.figure(figsize=(10,5))
    sns.histplot(df["Receita_Total"], bins=20, kde=True, color="blue")
    plt.title("Distribuição de Receita Total", fontsize=14)
    plt.xlabel("Receita Total")
    plt.ylabel("Frequência")
    plt.show()

# Gráfico de vendas por produto
def grafico_vendas_produto(df):
    plt.figure(figsize=(10,5))
    sns.barplot(x=df["Produto"].value_counts().index, y=df["Produto"].value_counts().values, palette="viridis")
    plt.title("Quantidade de Vendas por Produto", fontsize=14)
    plt.xlabel("Produto")
    plt.ylabel("Número de Vendas")
    plt.xticks(rotation=45)
    plt.show()

# Gráfico de receita por categoria
def grafico_receita_categoria(df):
    plt.figure(figsize=(10,5))
    sns.boxplot(x="Categoria", y="Receita_Total", data=df, palette="pastel")
    plt.title("Receita por Categoria", fontsize=14)
    plt.xlabel("Categoria")
    plt.ylabel("Receita Total")
    plt.show()

# Insight de tendência de vendas
def insight_tendencias(df):
    df_trend = df.groupby("Data")["Receita_Total"].sum().reset_index()
    plt.figure(figsize=(12,6))
    sns.lineplot(x="Data", y="Receita_Total", data=df_trend, marker="o", color="red")
    plt.title("Tendência de Receita ao Longo do Tempo", fontsize=14)
    plt.xlabel("Data")
    plt.ylabel("Receita Total")
    plt.xticks(rotation=45)
    plt.show()

# Função principal para análise de dados
def main():
    estatisticas_descritivas(df)
    grafico_receita(df)
    grafico_vendas_produto(df)
    grafico_receita_categoria(df)
    insight_tendencias(df)

# Executar análise
if __name__ == "__main__":
    main()


