# 📊 Dashboard de Vendas & CRM — Cyberpunk Edition

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Status](https://img.shields.io/badge/Status-🟢%20Live%20Online-00ff88?style=for-the-badge)

**[🚀 Acesse o Dashboard ao vivo →](https://dashboard-vendas-brunomartins.streamlit.app/)**

</div>

---

## 🎯 Sobre o Projeto

Dashboard interativo de **Vendas & CRM** com tema visual **Cyberpunk Neon** (verde `#00ffcc`), construído do zero com Python e Streamlit. O sistema simula um painel de inteligência comercial em tempo real para acompanhamento de operações de vendas, com visão consolidada de clientes.

> 🎓 Projeto desenvolvido como portfólio acadêmico — 2° Semestre de ADS na **Faculdade Impacta Tecnologia**

---

## ✨ Funcionalidades

| Feature | Descrição |
|---|---|
| **KPIs em Tempo Real** | Faturamento total, ticket médio e número de operações |
| **Filtros Interativos** | Filtrar por vendedor e por produto com multiselect dinâmico |
| **Gráficos Neon** | Faturamento por vendedor com tema escuro e cores neon via Plotly |
| **Visão de CRM** | Total comprado, número de compras e última compra por cliente |
| **Cache Otimizado** | `@st.cache_data` para performance de carregamento |

---

## 🛠️ Stack Técnica

```
Backend & Data:   Python 3 · Pandas · Streamlit
Visualização:     Plotly Express (tema dark customizado)
Estilo:           CSS3 injetado (Dark Mode Cyberpunk Neon)
Deploy:           Streamlit Community Cloud (gratuito)
```

---

## 📸 Screenshots

> **Tema escuro com indicadores Cyberpunk Neon**  
> KPIs em destaque, filtros laterais e gráficos com brilho neon característico.

---

## 💻 Rodando Localmente

```bash
# 1. Clone o repositório
git clone https://github.com/brunocamposmartins5-max/dashboard-vendas-python.git
cd dashboard-vendas-python

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Inicie o dashboard
streamlit run dashboard.py
```

Acesse em: `http://localhost:8501`

---

## 📂 Estrutura do Projeto

```
dashboard-crm/
├── 📄 dashboard.py        # App principal — lógica e interface
├── 📄 analise.py          # Exploração inicial dos dados
├── 📊 vendas.csv          # Dataset de vendas (exemplo fictício)
├── 📋 requirements.txt    # Dependências do projeto
└── ⚙️  .streamlit/
    └── config.toml        # Tema visual personalizado
```

---

## 🧠 Decisões Técnicas

- **Separação de concerns:** A visão de CRM é calculada a partir do `df_raw` global (antes dos filtros) para manter consistência analítica de auditoria, enquanto os gráficos respondem aos filtros em tempo real.
- **CSS Custom Injection:** O tema Cyberpunk é injetado via `st.markdown()` com `unsafe_allow_html=True`, sobrescrevendo os seletores nativos do Streamlit para uma identidade visual exclusiva.

---

## 👤 Autor

**Bruno Campos Martins** | Estudante de ADS — Faculdade Impacta Tecnologia  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bruno-campos-martins-9325b9381)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/brunocamposmartins5-max)
