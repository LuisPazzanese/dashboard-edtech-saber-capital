import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="EdTech Companies Analysis - Saber Capital", layout="wide", page_icon=":bar_chart:")

# Company data
data = pd.DataFrame([
    {"Company": "Skillsoft", "Gross Margin": 65, "Scalability": 8, "Regulatory Risk": 3, "Thesis Fit": 9},
    {"Company": "Nerdy", "Gross Margin": 70, "Scalability": 10, "Regulatory Risk": 2, "Thesis Fit": 10},
    {"Company": "2U", "Gross Margin": 50, "Scalability": 6, "Regulatory Risk": 8, "Thesis Fit": 7},
])

st.title("EdTech Companies Analysis - Saber Capital")
st.markdown("""
This interactive dashboard allows you to visualize and compare companies based on strategic KPIs used by Search Funds.
""")

# Comparison chart
st.header("Company Comparison")
fig = px.bar(
    data.melt(id_vars="Company", var_name="Criterion", value_name="Value"),
    x="Company", y="Value", color="Criterion", barmode="group",
    title="Comparison of Strategic KPIs Across Companies"
)
st.plotly_chart(fig, use_container_width=True)

# KPI Table
st.header("KPI Table")
st.dataframe(data.set_index("Company"))

# Valuation Simulator
st.header("Valuation Simulator")
st.markdown("""
Adjust the parameters below to simulate the projected valuation of an EdTech company:
""")

current_revenue = st.number_input("Current Annual Revenue (US$ thousands)", min_value=0, value=10000, step=500)
annual_growth = st.slider("Annual Growth Rate (%)", 0, 100, 20)
ebitda_margin = st.slider("EBITDA Margin (%)", 0, 100, 30)
ev_ebitda_multiple = st.slider("EV/EBITDA Multiple", 1, 30, 12)
projection_years = st.slider("Projection Horizon (years)", 1, 10, 5)

# Calculations
future_revenue = current_revenue * ((1 + annual_growth / 100) ** projection_years)
future_ebitda = future_revenue * (ebitda_margin / 100)
estimated_valuation = future_ebitda * ev_ebitda_multiple

st.subheader("Simulation Results")
st.write(f"Estimated Revenue in Year {projection_years}: US$ {future_revenue:,.0f}")
st.write(f"Estimated EBITDA: US$ {future_ebitda:,.0f}")
st.write(f"Estimated Valuation (EV): US$ {estimated_valuation:,.0f}")

# Strategy Frameworks Section
st.header("Strategic Frameworks Applied")

with st.expander("Market Map: EdTech B2B Ecosystem Segments"):
    st.markdown("""
    **1. Learning Infrastructure**: LMS platforms, HRIS integrations, educational APIs

    **2. Content and Curriculum**: Companies creating proprietary courses or curating external content

    **3. Distribution and Scalability**: Marketplaces, white-labels, plug-and-play solutions

    **4. Data and Engagement**: Analytics tools, personalization, gamification, continuous feedback
    """)

with st.expander("Growth Flywheel: Virtuous Growth Cycle"):
    st.markdown("""
    **Efficient Acquisition**: Low CAC, organic acquisition, institutional partnerships

    **Perceived Value Delivery**: High retention, user engagement, time spent on platform

    **Revenue Expansion**: Upsell, cross-sell, increased LTV and contracted licenses
    """)
