import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Configuração da página
st.set_page_config(
    page_title="Bruno Martins | Dashboard Vendas & CRM",
    page_icon="⚡",
    layout="wide",
)

# 2. CSS Dark Neon (mesmo visual do Portfólio: #060911, #0d1527, #00f2fe, #39ff14)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap');

    /* Fundo geral com grid sutil */
    .stApp {
        background-color: #060911;
        background-image:
            linear-gradient(rgba(0, 242, 254, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 242, 254, 0.03) 1px, transparent 1px);
        background-size: 50px 50px;
        color: #e2e8f0;
        font-family: 'Inter', sans-serif;
    }

    /* Barra lateral */
    [data-testid="stSidebar"] {
        background-color: #0b0f19;
        border-right: 1px solid rgba(0, 242, 254, 0.2);
    }

    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] label {
        color: #e2e8f0 !important;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Cards de métricas (KPIs) */
    div[data-testid="metric-container"] {
        background-color: #0d1527;
        border: 1px solid rgba(0, 242, 254, 0.3);
        padding: 18px 20px;
        border-radius: 12px;
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.12);
        transition: all 0.3s ease;
    }

    div[data-testid="metric-container"]:hover {
        border-color: #00f2fe;
        box-shadow: 0 0 24px rgba(0, 242, 254, 0.25);
    }

    div[data-testid="metric-container"] label {
        color: #94a3b8 !important;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.78rem !important;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
        color: #00f2fe !important;
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
        text-shadow: 0 0 12px rgba(0, 242, 254, 0.45);
    }

    /* Títulos */
    h1, h2, h3 {
        font-family: 'JetBrains Mono', monospace;
        color: #e2e8f0 !important;
    }

    h1 {
        color: #00f2fe !important;
        text-shadow: 0 0 18px rgba(0, 242, 254, 0.35);
    }

    /* Divisor */
    hr {
        border-color: #1e293b !important;
    }

    /* Badge de status */
    .live-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.78rem;
        color: #39ff14;
        background: rgba(57, 255, 20, 0.08);
        border: 1px solid rgba(57, 255, 20, 0.25);
        padding: 4px 12px;
        border-radius: 100px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 3. Carregamento dos dados
@st.cache_data
def carregar_dados():
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

st.sidebar.markdown("---")
st.sidebar.markdown(
    "🔗 [Portfólio Bruno Martins](https://brunocamposmartins5-max.github.io/portfolio/)"
)

# Aplicando os filtros
df_filtrado = df_raw[
    df_raw["Vendedor"].isin(vendedor_selecionado)
    & df_raw["Produto"].isin(produto_selecionado)
]

# 6. Cabeçalho Principal
st.markdown('<div class="live-badge">🟢 Sistema Online · Tempo Real</div>', unsafe_allow_html=True)
st.title("⚡ CYBER_DASH // VENDAS & CRM")
st.markdown(
    "<span style='color:#94a3b8;'>Sistema de monitoramento tático e inteligência comercial em tempo real.</span>",
    unsafe_allow_html=True,
)
st.markdown("---")

# Métricas (KPIs)
faturamento_total = df_filtrado["Valor_Total"].sum()
ticket_medio = df_filtrado["Valor_Total"].mean() if not df_filtrado.empty else 0
num_vendas = len(df_filtrado)

col1, col2, col3 = st.columns(3)
col1.metric("FATURAMENTO TOTAL", f"R$ {faturamento_total:,.2f}")
col2.metric("TICKET MÉDIO", f"R$ {ticket_medio:,.2f}")
col3.metric("OPERAÇÕES (VENDAS)", f"{num_vendas}")

st.markdown("---")

# 7. Gráficos com Tema Dark Neon do Portfólio
neon_blue = "#00f2fe"
neon_purple = "#bf5af2"
bg_card = "#0d1527"

if not df_filtrado.empty:
    gcol1, gcol2 = st.columns(2)

    with gcol1:
        df_vendedor = df_filtrado.groupby("Vendedor")["Valor_Total"].sum().reset_index()
        fig_vendedor = px.bar(
            df_vendedor,
            x="Vendedor",
            y="Valor_Total",
            title="Faturamento por Vendedor",
        )
        fig_vendedor.update_layout(
            plot_bgcolor=bg_card,
            paper_bgcolor=bg_card,
            font_color="#e2e8f0",
            title_font_color=neon_blue,
            xaxis=dict(gridcolor="#1e293b"),
            yaxis=dict(gridcolor="#1e293b"),
        )
        fig_vendedor.update_traces(
            marker_color=neon_blue, marker_line_color="#ffffff", marker_line_width=1
        )
        st.plotly_chart(fig_vendedor, use_container_width=True)

    with gcol2:
        df_produto = df_filtrado.groupby("Produto")["Valor_Total"].sum().reset_index()
        fig_produto = px.bar(
            df_produto,
            x="Produto",
            y="Valor_Total",
            title="Faturamento por Produto",
        )
        fig_produto.update_layout(
            plot_bgcolor=bg_card,
            paper_bgcolor=bg_card,
            font_color="#e2e8f0",
            title_font_color=neon_purple,
            xaxis=dict(gridcolor="#1e293b"),
            yaxis=dict(gridcolor="#1e293b"),
        )
        fig_produto.update_traces(
            marker_color=neon_purple, marker_line_color="#ffffff", marker_line_width=1
        )
        st.plotly_chart(fig_produto, use_container_width=True)
else:
    st.warning("Nenhum dado encontrado para os filtros selecionados.")

# 8. Seção de CRM (Histórico Global)
st.markdown("### 🗃️ CLIENTES // BASE DE CRM")
st.caption(
    "ℹ️ *Nota: O histórico consolidado dos clientes permanece global para auditoria analítica.*"
)
st.dataframe(df_crm_global, use_container_width=True)
