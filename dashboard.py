import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Configuração da página (Deve ser a primeira linha do Streamlit)
st.set_page_config(
    page_title="Dashboard Cyberpunk - Vendas & CRM",
    page_icon="⚡",
    layout="wide",
)

# 2. Injetando CSS Cyberpunk Customizado (Neon & Dark Mode)
st.markdown(
    """
    <style>
    /* Fundo geral da aplicação */
    .stApp {
        background-color: #05050a;
        color: #00ffcc;
    }
    
    /* Barra lateral estilo terminal futurista */
    [data-testid="stSidebar"] {
        background-color: #0b0b16;
        border-right: 1px solid #00ffcc33;
    }
    
    /* Estilização dos cards de métricas (KPIs) */
    div[data-testid="metric-container"] {
        background-color: #0e0e1a;
        border: 1px solid #00ffcc;
        padding: 15px;
        border-radius: 6px;
        box-shadow: 0 0 12px rgba(0, 255, 204, 0.25);
    }
    
    div[data-testid="metric-container"] label {
        color: #8a99ad !important;
        font-family: 'Courier New', monospace;
    }
    
    div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
        color: #00ffcc !important;
        font-family: 'Courier New', monospace;
        text-shadow: 0 0 8px rgba(0, 255, 204, 0.4);
    }
    
    /* Títulos com efeito tecnológico */
    h1, h2, h3 {
        font-family: 'Courier New', monospace;
        color: #00ffcc !important;
        text-shadow: 0 0 10px rgba(0, 255, 204, 0.3);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. Carregamento dos dados (Exemplo simulado ou lendo seu 'vendas.csv')
@st.cache_data
def carregar_dados():
    # Substitua pelo seu pd.read_csv('vendas.csv') real
    data = {
        "Data_Compra": [
            "2026-01-10",
            "2026-01-15",
            "2026-02-05",
            "2026-02-20",
            "2026-03-01",
            "2026-03-10",
        ],
        "Cliente": [
            "Empresa Alfa",
            "Empresa Beta",
            "Empresa Gama",
            "Empresa Alfa",
            "Empresa Delta",
            "Empresa Beta",
        ],
        "Vendedor": [
            "Ana",
            "Carlos",
            "Marcos",
            "Ana",
            "Marcos",
            "Carlos",
        ],
        "Produto": [
            "Software",
            "Consultoria",
            "Software",
            "Suporte",
            "Consultoria",
            "Software",
        ],
        "Valor_Total": [5000, 7500, 10500, 3000, 14400, 6000],
    }
    df = pd.DataFrame(data)
    df["Data_Compra"] = pd.to_datetime(df["Data_Compra"])
    return df


df_raw = carregar_dados()

# 4. Visão global de CRM (Calculada ANTES dos filtros da barra lateral)
df_crm_global = (
    df_raw.groupby("Cliente")
    .agg(
        total_comprado=("Valor_Total", "sum"),
        numero_compras=("Valor_Total", "count"),
        ultima_compra=("Data_Compra", "max"),
    )
    .reset_index()
    .sort_values(by="total_comprado", ascending=False)
)

# 5. Barra Lateral de Filtros
st.sidebar.markdown("## ⚙️ PAINEL DE CONTROLE")
vendedores_disponiveis = df_raw["Vendedor"].unique()
produtos_disponiveis = df_raw["Produto"].unique()

vendedor_selecionado = st.sidebar.multiselect(
    "Filtrar Vendedor", vendedores_disponiveis, default=vendedores_disponiveis
)
produto_selecionado = st.sidebar.multiselect(
    "Filtrar Produto", produtos_disponiveis, default=produtos_disponiveis
)

# Aplicando os filtros para o restante do dashboard
df_filtrado = df_raw[
    df_raw["Vendedor"].isin(vendedor_selecionado)
    & df_raw["Produto"].isin(produto_selecionado)
]

# 6. Corpo Principal do Dashboard
st.title("⚡ CYBER_DASH // VENDAS & CRM")
st.markdown(
    "*Sistema de monitoramento tático e inteligência comercial em tempo real.*"
)
st.markdown("---")

# Métricas (KPIs)
faturamento_total = df_filtrado["Valor_Total"].sum()
ticket_medio = (
    df_filtrado["Valor_Total"].mean() if not df_filtrado.empty else 0
)
num_vendas = len(df_filtrado)

col1, col2, col3 = st.columns(3)
col1.metric("FATURAMENTO TOTAL", f"R$ {faturamento_total:,.2f}")
col2.metric("TICKET MÉDIO", f"R$ {ticket_medio:,.2f}")
col3.metric("OPERAÇÕES (VENDAS)", f"{num_vendas}")

st.markdown("---")

# 7. Gráficos com Tema Escuro / Plotly Neon
cor_neon = "#00ffcc"
bg_escuro = "#05050a"

# Gráfico 1: Faturamento por Vendedor
if not df_filtrado.empty:
    df_vendedor = (
        df_filtrado.groupby("Vendedor")["Valor_Total"].sum().reset_index()
    )
    fig_vendedor = px.bar(
        df_vendedor,
        x="Vendedor",
        y="Valor_Total",
        title="Faturamento por Operador (Vendedor)",
    )
    fig_vendedor.update_layout(
        plot_bgcolor=bg_escuro,
        paper_bgcolor=bg_escuro,
        font_color="#00ffcc",
        title_font_color="#00ffcc",
    )
    fig_vendedor.update_traces(
        marker_color=cor_neon, marker_line_color="#ffffff", marker_line_width=1
    )
    st.plotly_chart(fig_vendedor, use_container_width=True)
else:
    st.warning("Nenhum dado encontrado para os filtros selecionados.")

# 8. Seção de CRM (Histórico Global)
st.markdown("### 🗃️ CLIENTES // BASE DE CRM")
st.caption(
    "ℹ️ *Nota: O histórico consolidado dos clientes permanece global para auditoria analítica.*"
)
st.dataframe(df_crm_global, use_container_width=True)