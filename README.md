# 📊 Dashboard de Vendas e CRM

Dashboard interativo de vendas desenvolvido em Python, com indicadores de desempenho (KPIs) e visão de CRM.

## 🚀 Funcionalidades

- **KPIs em tempo real:** faturamento total, ticket médio e número de vendas.
- **Filtros interativos:** por vendedor e por produto.
- **Gráficos:** faturamento por vendedor, por produto e evolução mensal.
- **Visão de clientes (CRM):** total comprado, número de compras e última compra por cliente.

## 🛠️ Tecnologias utilizadas

- [Python](https://python.org)
- [Pandas](https://pydata.org) - manipulação e análise de dados
- [Streamlit](https://streamlit.io) - interface web interativa

## 💻 Como rodar o projeto localmente

1. **Clone o repositório:**
```bash
git clone https://github.com/brunocamposmartins5-max/dashboard-vendas-python.git
cd dashboard-vendas-python
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Rode o dashboard:**
```bash
streamlit run dashboard.py
```

## 📂 Estrutura do projeto

```text
dashboard-crm/
├── dashboard.py       # Aplicação principal do dashboard
├── analise.py         # Script inicial de exploração dos dados
├── vendas.csv         # Base de dados de exemplo (vendas fictícias)
├── requirements.txt   # Dependências do projeto
└── .streamlit/
    └── config.toml    # Tema visual customizado
```

## 👥 Autor

Bruno Martins
