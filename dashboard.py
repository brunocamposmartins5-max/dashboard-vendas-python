import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

st.title("Dashboard de Vendas")
st.caption("Acompanhamento de faturamento, vendedores e produtos")

df = pd.read_csv("vendas.csv")
# Filtros na barra lateral
st.sidebar.header("Filtros")

vendedores = st.sidebar.multiselect(
    "Vendedor",
    options=df["vendedor"].unique(),
    default=df["vendedor"].unique()
)

produtos = st.sidebar.multiselect(
    "Produto",
    options=df["produto"].unique(),
    default=df["produto"].unique()
)

df = df[df["vendedor"].isin(vendedores) & df["produto"].isin(produtos)]
# Cartões de indicadores no topo
col1, col2, col3 = st.columns(3)

col1.metric("Faturamento total", f"R$ {df['valor'].sum():,.0f}")
col2.metric("Ticket médio", f"R$ {df['valor'].mean():,.2f}")
col3.metric("Número de vendas", len(df))

st.divider()
st.subheader("Faturamento por vendedor")
faturamento_vendedor = df.groupby("vendedor")["valor"].sum()
st.bar_chart(faturamento_vendedor)

st.subheader("Faturamento por produto")
faturamento_produto = df.groupby("produto")["valor"].sum()
st.bar_chart(faturamento_produto)

st.subheader("Evolução de vendas por mês")
df["data"] = pd.to_datetime(df["data"])
df["mes"] = df["data"].dt.to_period("M").astype(str)
vendas_por_mes = df.groupby("mes")["valor"].sum()
st.line_chart(vendas_por_mes)
st.subheader("Clientes (visão CRM)")

resumo_clientes = df.groupby("cliente").agg(
    total_comprado=("valor", "sum"),
    numero_compras=("valor", "count"),
    ultima_compra=("data", "max")
).reset_index()

resumo_clientes = resumo_clientes.sort_values("total_comprado", ascending=False)

st.dataframe(resumo_clientes, width="stretch")
st.write(df)