import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Configuração da página
st.set_page_config(
    page_title="CYBER_DASH // Inteligência Comercial & CRM",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. CSS Dark Neon Executivo (alinhado ao Portfólio)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap');

    .stApp {
        background-color: #060911;
        background-image:
            linear-gradient(rgba(0, 242, 254, 0.025) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 242, 254, 0.025) 1px, transparent 1px);
        background-size: 50px 50px;
        color: #e2e8f0;
        font-family: 'Inter', sans-serif;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0b0f19;
        border-right: 1px solid #1e293b;
    }

    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] label {
        color: #e2e8f0 !important;
        font-family: 'JetBrains Mono', monospace;
    }

    [data-testid="stSidebar"] span[data-baseweb="tag"] {
        background-color: rgba(0, 242, 254, 0.1) !important;
        border: 1px solid rgba(0, 242, 254, 0.35) !important;
        color: #00f2fe !important;
        border-radius: 100px !important;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.76rem !important;
    }

    [data-testid="stSidebar"] span[data-baseweb="tag"] svg {
        fill: #00f2fe !important;
    }

    [data-testid="stSidebar"] div[data-baseweb="select"] > div {
        background-color: #0d1527 !important;
        border-color: #1e293b !important;
    }

    /* KPI Cards */
    div[data-testid="metric-container"] {
        background-color: #0d1527;
        border: 1px solid #1e293b;
        border-top: 2px solid #00f2fe;
        padding: 18px 20px;
        border-radius: 10px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
        transition: all 0.25s ease;
    }

    div[data-testid="metric-container"]:hover {
        border-color: rgba(0, 242, 254, 0.45);
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.15);
    }

    div[data-testid="metric-container"] label {
        color: #94a3b8 !important;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.74rem !important;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
        color: #f8fafc !important;
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
        font-size: 1.65rem !important;
    }

    /* Títulos */
    h1, h2, h3 {
        font-family: 'JetBrains Mono', monospace;
        color: #f8fafc !important;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 1px solid #1e293b;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: #0d1527;
        border: 1px solid #1e293b;
        border-radius: 8px 8px 0 0;
        color: #94a3b8;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.82rem;
        padding: 8px 18px;
    }

    .stTabs [aria-selected="true"] {
        background-color: rgba(0, 242, 254, 0.1) !important;
        border-color: #00f2fe !important;
        color: #00f2fe !important;
    }

    /* Botão Download */
    .stDownloadButton button {
        background-color: rgba(0, 242, 254, 0.1) !important;
        border: 1px solid rgba(0, 242, 254, 0.4) !important;
        color: #00f2fe !important;
        font-family: 'JetBrains Mono', monospace;
        border-radius: 8px;
    }

    .stDownloadButton button:hover {
        background-color: #00f2fe !important;
        color: #060911 !important;
    }

    hr { border-color: #1e293b !important; }

    .header-tag {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        color: #39ff14;
        background: rgba(57, 255, 20, 0.08);
        border: 1px solid rgba(57, 255, 20, 0.25);
        padding: 4px 12px;
        border-radius: 100px;
        margin-bottom: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# 3. Base de Dados B2B Realista (Jan - Jun 2026)
@st.cache_data
def carregar_dados():
    registros = [
        ("2026-01-08", "Empresa Alfa", "Ana", "Software", 12500),
        ("2026-01-14", "Empresa Beta", "Carlos", "Consultoria", 8400),
        ("2026-01-22", "Empresa Gama", "Marcos", "Suporte", 4200),
        ("2026-01-29", "TechNova Ltda", "Ana", "Software", 15800),
        ("2026-02-05", "Empresa Gama", "Marcos", "Software", 11200),
        ("2026-02-11", "Grupo Vértice", "Carlos", "Consultoria", 9600),
        ("2026-02-18", "Empresa Alfa", "Ana", "Suporte", 3800),
        ("2026-02-25", "Empresa Delta", "Marcos", "Consultoria", 14400),
        ("2026-03-03", "Empresa Beta", "Carlos", "Software", 13200),
        ("2026-03-10", "TechNova Ltda", "Ana", "Consultoria", 11500),
        ("2026-03-17", "InovaCorp", "Marcos", "Software", 16900),
        ("2026-03-24", "Grupo Vértice", "Carlos", "Suporte", 4900),
        ("2026-04-02", "Empresa Alfa", "Ana", "Software", 14100),
        ("2026-04-09", "Empresa Delta", "Marcos", "Consultoria", 12800),
        ("2026-04-16", "InovaCorp", "Ana", "Suporte", 5400),
        ("2026-04-23", "Empresa Beta", "Carlos", "Consultoria", 10200),
        ("2026-05-04", "TechNova Ltda", "Marcos", "Software", 18500),
        ("2026-05-12", "Grupo Vértice", "Ana", "Consultoria", 13700),
        ("2026-05-19", "Empresa Gama", "Carlos", "Software", 12100),
        ("2026-05-26", "Empresa Delta", "Marcos", "Suporte", 6100),
        ("2026-06-03", "InovaCorp", "Ana", "Software", 21000),
        ("2026-06-11", "Empresa Alfa", "Carlos", "Consultoria", 15300),
        ("2026-06-18", "TechNova Ltda", "Marcos", "Consultoria", 16400),
        ("2026-06-25", "Empresa Beta", "Ana", "Suporte", 5800),
    ]
    df = pd.DataFrame(
        registros,
        columns=["Data_Compra", "Cliente", "Vendedor", "Produto", "Valor_Total"],
    )
    df["Data_Compra"] = pd.to_datetime(df["Data_Compra"])
    df["Mes"] = df["Data_Compra"].dt.to_period("M").astype(str)
    return df


df_raw = carregar_dados()

# 4. Sidebar de Filtros
st.sidebar.markdown("## ⚙️ PAINEL DE CONTROLE")

vendedores_disponiveis = sorted(df_raw["Vendedor"].unique())
produtos_disponiveis = sorted(df_raw["Produto"].unique())
data_min = df_raw["Data_Compra"].min().date()
data_max = df_raw["Data_Compra"].max().date()

periodo = st.sidebar.date_input(
    "Período de Análise",
    value=(data_min, data_max),
    min_value=data_min,
    max_value=data_max,
)

vendedor_selecionado = st.sidebar.multiselect(
    "Vendedor", vendedores_disponiveis, default=vendedores_disponiveis
)
produto_selecionado = st.sidebar.multiselect(
    "Linha de Produto", produtos_disponiveis, default=produtos_disponiveis
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "👤 **Bruno Campos Martins**  \n"
    "🔗 [Portfólio](https://brunocamposmartins5-max.github.io/portfolio/) · "
    "[GitHub](https://github.com/brunocamposmartins5-max)"
)

# Aplicando filtros
if isinstance(periodo, tuple) and len(periodo) == 2:
    inicio, fim = pd.to_datetime(periodo[0]), pd.to_datetime(periodo[1])
    mask_data = (df_raw["Data_Compra"] >= inicio) & (df_raw["Data_Compra"] <= fim)
else:
    mask_data = True

df_filtrado = df_raw[
    mask_data
    & df_raw["Vendedor"].isin(vendedor_selecionado)
    & df_raw["Produto"].isin(produto_selecionado)
]

# 5. Cabeçalho
st.markdown('<div class="header-tag">🟢 LIVE BI // INTELIGÊNCIA COMERCIAL</div>', unsafe_allow_html=True)
st.title("⚡ CYBER_DASH // VENDAS & CRM")
st.caption("Painel executivo de performance comercial, mix de produtos e carteira de clientes B2B.")

# 6. KPIs Executivos
faturamento_total = df_filtrado["Valor_Total"].sum()
ticket_medio = df_filtrado["Valor_Total"].mean() if not df_filtrado.empty else 0
num_vendas = len(df_filtrado)
clientes_ativos = df_filtrado["Cliente"].nunique()

k1, k2, k3, k4 = st.columns(4)
k1.metric("FATURAMENTO TOTAL", f"R$ {faturamento_total:,.2f}")
k2.metric("TICKET MÉDIO", f"R$ {ticket_medio:,.2f}")
k3.metric("OPERAÇÕES", f"{num_vendas}")
k4.metric("CLIENTES ATIVOS", f"{clientes_ativos}")

st.markdown("")

# 7. Abas de Análise
tab_exec, tab_crm, tab_ops = st.tabs(
    ["📈 Visão Executiva", "🗃️ Base de CRM", "📋 Detalhamento de Operações"]
)

bg_card = "#0d1527"
grid_color = "#1e293b"

with tab_exec:
    if df_filtrado.empty:
        st.warning("Nenhum registro encontrado para os filtros selecionados.")
    else:
        # Gráfico 1: Evolução Mensal (Largura Total)
        df_mensal = (
            df_filtrado.groupby("Mes")["Valor_Total"]
            .sum()
            .reset_index()
            .sort_values("Mes")
        )
        fig_mensal = px.area(
            df_mensal,
            x="Mes",
            y="Valor_Total",
            title="Evolução Mensal de Faturamento (R$)",
            markers=True,
        )
        fig_mensal.update_traces(
            line_color="#00f2fe",
            fillcolor="rgba(0, 242, 254, 0.12)",
            marker=dict(color="#00f2fe", size=8),
            hovertemplate="<b>%{x}</b><br>Faturamento: R$ %{y:,.2f}<extra></extra>",
        )
        fig_mensal.update_layout(
            plot_bgcolor=bg_card,
            paper_bgcolor=bg_card,
            font_color="#e2e8f0",
            title_font_color="#00f2fe",
            xaxis=dict(title="", gridcolor=grid_color),
            yaxis=dict(title="", gridcolor=grid_color),
            margin=dict(l=20, r=20, t=50, b=20),
            height=320,
        )
        st.plotly_chart(fig_mensal, use_container_width=True)

        # Gráficos 2 e 3: Vendedor + Mix de Produtos
        c1, c2 = st.columns([1.2, 1])

        with c1:
            df_vendedor = (
                df_filtrado.groupby("Vendedor")["Valor_Total"]
                .sum()
                .reset_index()
                .sort_values("Valor_Total", ascending=True)
            )
            fig_vendedor = px.bar(
                df_vendedor,
                x="Valor_Total",
                y="Vendedor",
                orientation="h",
                title="Ranking de Faturamento por Vendedor",
            )
            fig_vendedor.update_traces(
                marker_color="#00f2fe",
                hovertemplate="<b>%{y}</b><br>R$ %{x:,.2f}<extra></extra>",
            )
            fig_vendedor.update_layout(
                plot_bgcolor=bg_card,
                paper_bgcolor=bg_card,
                font_color="#e2e8f0",
                title_font_color="#00f2fe",
                xaxis=dict(title="", gridcolor=grid_color),
                yaxis=dict(title="", gridcolor=grid_color),
                margin=dict(l=20, r=20, t=50, b=20),
                height=320,
            )
            st.plotly_chart(fig_vendedor, use_container_width=True)

        with c2:
            df_produto = (
                df_filtrado.groupby("Produto")["Valor_Total"].sum().reset_index()
            )
            fig_produto = px.pie(
                df_produto,
                names="Produto",
                values="Valor_Total",
                hole=0.58,
                title="Mix de Faturamento por Produto",
                color_discrete_sequence=["#00f2fe", "#bf5af2", "#39ff14"],
            )
            fig_produto.update_traces(
                textposition="inside",
                textinfo="percent+label",
                hovertemplate="<b>%{label}</b><br>R$ %{value:,.2f} (%{percent})<extra></extra>",
            )
            fig_produto.update_layout(
                plot_bgcolor=bg_card,
                paper_bgcolor=bg_card,
                font_color="#e2e8f0",
                title_font_color="#bf5af2",
                showlegend=False,
                margin=dict(l=20, r=20, t=50, b=20),
                height=320,
            )
            st.plotly_chart(fig_produto, use_container_width=True)

with tab_crm:
    df_crm = (
        df_raw.groupby("Cliente")
        .agg(
            Total_Comprado=("Valor_Total", "sum"),
            Operacoes=("Valor_Total", "count"),
            Ticket_Medio=("Valor_Total", "mean"),
            Ultima_Compra=("Data_Compra", "max"),
        )
        .reset_index()
        .sort_values(by="Total_Comprado", ascending=False)
    )
    total_geral = df_crm["Total_Comprado"].sum()
    df_crm["Participacao_%"] = (df_crm["Total_Comprado"] / total_geral) * 100

    st.dataframe(
        df_crm,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Cliente": st.column_config.TextColumn("Cliente B2B"),
            "Total_Comprado": st.column_config.NumberColumn(
                "Total Comprado", format="R$ %.2f"
            ),
            "Ticket_Medio": st.column_config.NumberColumn(
                "Ticket Médio", format="R$ %.2f"
            ),
            "Operacoes": st.column_config.NumberColumn("Operações", format="%d"),
            "Ultima_Compra": st.column_config.DateColumn(
                "Última Compra", format="DD/MM/YYYY"
            ),
            "Participacao_%": st.column_config.ProgressColumn(
                "Share (%)", format="%.1f%%", min_value=0, max_value=100
            ),
        },
    )

with tab_ops:
    df_ops = df_filtrado.sort_values("Data_Compra", ascending=False).drop(columns=["Mes"])
    st.dataframe(
        df_ops,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Data_Compra": st.column_config.DateColumn("Data", format="DD/MM/YYYY"),
            "Valor_Total": st.column_config.NumberColumn("Valor", format="R$ %.2f"),
        },
    )

    csv = df_ops.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Exportar Operações (CSV)",
        data=csv,
        file_name="operacoes_vendas_crm.csv",
        mime="text/csv",
    )
