import pandas as pd

df = pd.read_csv("vendas.csv")

# KPI 1: faturamento total
faturamento_total = df["valor"].sum()
print(f"Faturamento total: R$ {faturamento_total}")

# KPI 2: ticket médio (valor médio por venda)
ticket_medio = df["valor"].mean()
print(f"Ticket médio: R$ {ticket_medio:.2f}")

# KPI 3: faturamento por vendedor
faturamento_por_vendedor = df.groupby("vendedor")["valor"].sum()
print("\nFaturamento por vendedor:")
print(faturamento_por_vendedor)

# KPI 4: faturamento por produto
faturamento_por_produto = df.groupby("produto")["valor"].sum()
print("\nFaturamento por produto:")
print(faturamento_por_produto)
