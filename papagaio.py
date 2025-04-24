import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Análise EdTechs - Saber Capital", layout="wide", page_icon=":bar_chart:")

# Dados das empresas
dados = pd.DataFrame([
    {"Empresa": "Skillsoft", "Margem Bruta": 65, "Escalabilidade": 8, "Risco Regulatório": 3, "Alinhamento com Tese": 9},
    {"Empresa": "Nerdy", "Margem Bruta": 70, "Escalabilidade": 10, "Risco Regulatório": 2, "Alinhamento com Tese": 10},
    {"Empresa": "2U", "Margem Bruta": 50, "Escalabilidade": 6, "Risco Regulatório": 8, "Alinhamento com Tese": 7},
])

st.title("Análise de Empresas EdTech - Saber Capital")
st.markdown("""
Este dashboard interativo permite visualizar e comparar empresas com base em critérios estratégicos utilizados por Search Funds.
""")

# Gráfico comparativo
st.header("Comparativo entre Empresas")
fig = px.bar(
    dados.melt(id_vars="Empresa", var_name="Critério", value_name="Valor"),
    x="Empresa", y="Valor", color="Critério", barmode="group",
    title="Comparativo de KPIs Estratégicos entre as Empresas"
)
st.plotly_chart(fig, use_container_width=True)

# Tabela de dados
st.header("Tabela de KPIs")
st.dataframe(dados.set_index("Empresa"))

# Simulador de Valuation
st.header("Simulador de Valuation")
st.markdown("""
Ajuste os parâmetros abaixo para simular o valuation projetado para uma empresa EdTech:
""")

receita_atual = st.number_input("Receita Anual Atual (US$ mil)", min_value=0, value=10000, step=500)
crescimento_anual = st.slider("Taxa de Crescimento Anual (%)", 0, 100, 20)
margem_ebitda = st.slider("Margem EBITDA (%)", 0, 100, 30)
mult_ev_ebitda = st.slider("Múltiplo EV/EBITDA", 1, 30, 12)
periodo_anos = st.slider("Horizonte de Projeção (anos)", 1, 10, 5)

# Cálculos
receita_futura = receita_atual * ((1 + crescimento_anual / 100) ** periodo_anos)
ebitda_futuro = receita_futura * (margem_ebitda / 100)
valuation_estimado = ebitda_futuro * mult_ev_ebitda

st.subheader("Resultado da Simulação")
st.write(f"Receita Estimada no Ano {periodo_anos}: US$ {receita_futura:,.0f}")
st.write(f"EBITDA Estimado: US$ {ebitda_futuro:,.0f}")
st.write(f"Valuation Estimado (EV): US$ {valuation_estimado:,.0f}")

# Tela de apresentação dos Frameworks
st.header("Frameworks Estratégicos Aplicados")

with st.expander("Market Map: Segmentos do Ecossistema EdTech B2B"):
    st.markdown("""
    **1. Infraestrutura de Aprendizado**: Plataformas LMS, integrações com HRIS, APIs educacionais

    **2. Conteúdo e Currículo**: Empresas que produzem cursos próprios ou curam conteúdo externo

    **3. Distribuição e Escalabilidade**: Marketplaces, white-labels, soluções plug-and-play

    **4. Dados e Engajamento**: Ferramentas de analytics, personalização, gamificação, feedback contínuo
    """)

with st.expander("Growth Flywheel: Ciclo Virtuoso de Crescimento"):
    st.markdown("""
    **Aquisição Eficiente**: CAC baixo, aquisição orgânica, parcerias institucionais

    **Entrega de Valor Percebido**: Alta retenção, engajamento do usuário, tempo na plataforma

    **Expansão de Receita**: Upsell, cross-sell, aumento de LTV e licenças contratadas
    """)