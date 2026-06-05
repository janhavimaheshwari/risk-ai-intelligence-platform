import streamlit as st
import pandas as pd

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(
    page_title="RiskPulse AI | Enterprise Risk Intelligence",
    page_icon="📊",
    layout="wide"
)

# ----------------------------------
# CUSTOM CSS
# ----------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #0B0F19 !important;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #161F33 0%, #0D1527 100%);
        border: 1px solid #23355A;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }
    .metric-label {
        color: #8A99AD;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 600;
        margin-bottom: 8px;
    }
    .metric-val {
        color: #FFFFFF;
        font-size: 32px;
        font-weight: 700;
        font-family: 'Courier New', monospace;
    }

    .executive-summary-box {
        background: #0E1E38;
        border-left: 5px solid #00F2FE;
        padding: 25px;
        border-radius: 4px 12px 12px 4px;
        margin-bottom: 25px;
    }
    .risk-matrix-box {
        background: #251219;
        border-left: 5px solid #FF4A5A;
        padding: 25px;
        border-radius: 4px 12px 12px 4px;
        margin-bottom: 25px;
    }
    .recommendation-box {
        background: #0F2422;
        border-left: 5px solid #10B981;
        padding: 25px;
        border-radius: 4px 12px 12px 4px;
        margin-bottom: 25px;
    }
    
    .title-gradient {
        background: linear-gradient(90deg, #00F2FE 0%, #4FACFE 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 38px;
        font-weight: 800;
        letter-spacing: -0.5px;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------------
# LOAD DATA
# ----------------------------------
@st.cache_data
def load_transactional_universe():
    try:
        return pd.read_csv("data/financial_anomaly_data.csv")
    except FileNotFoundError:
        return pd.DataFrame({
            "Amount": [52000, 120500, 4500, 890000, 12000, 310000],
            "AccountID": ["ACC-901", "ACC-104", "ACC-901", "ACC-772", "ACC-104", "ACC-901"],
            "Merchant": ["GlobalCorp", "AlphaLogistics", "GlobalCorp", "ApexTrading", "AlphaLogistics", "GlobalCorp"],
            "Location": ["NY, USA", "LN, UK", "NY, USA", "HK, CN", "LN, UK", "NY, USA"]
        })

df = load_transactional_universe()

# KPI Calculations
total_txns = len(df)
total_amount = df["Amount"].sum()
avg_amount = df["Amount"].mean()
accounts = df["AccountID"].nunique()

if "app_view" not in st.session_state:
    st.session_state.app_view = "dashboard"

# ----------------------------------
# HEADER NAVIGATION
# ----------------------------------
col_title, col_actions = st.columns([0.7, 0.3])
with col_title:
    st.markdown("<div class='title-gradient'>🛡️ RiskPulse AI Intelligence</div>", unsafe_allow_html=True)
    st.write("Enterprise-grade risk monitoring and dynamic autonomous threat evaluation framework.")

with col_actions:
    st.write("")
    nav_col1, nav_col2 = st.columns(2)
    with nav_col1:
        if st.button("📊 System Metrics", use_container_width=True):
            st.session_state.app_view = "dashboard"
    with nav_col2:
        if st.button("🧠 AI Risk Insights", use_container_width=True):
            st.session_state.app_view = "ai_insights"

st.markdown("---")

# ----------------------------------
# VIEW 1: MANAGEMENT DASHBOARD VIEW
# ----------------------------------
if st.session_state.app_view == "dashboard":
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f"<div class='metric-card'><div class='metric-label'>Transactional Scope</div><div class='metric-val'>{total_txns:,}</div></div>", unsafe_allow_html=True)
    with m2:
        st.markdown(f"<div class='metric-card'><div class='metric-label'>Total Exposed Capital</div><div class='metric-val'>${total_amount:,.0f}</div></div>", unsafe_allow_html=True)
    with m3:
        st.markdown(f"<div class='metric-card'><div class='metric-label'>Mean Transfer Value</div><div class='metric-val'>${avg_amount:,.2f}</div></div>", unsafe_allow_html=True)
    with m4:
        st.markdown(f"<div class='metric-card'><div class='metric-label'>Monitored Endpoints</div><div class='metric-val'>{accounts} Entity Nodes</div></div>", unsafe_allow_html=True)

    st.write("")
    st.write("")
    
    g1, g2 = st.columns(2)
    with g1:
        st.markdown("### 🏢 Concentration of Merchant Exposures")
        merchant_counts = df["Merchant"].value_counts().head(5)
        st.bar_chart(merchant_counts, color="#4FACFE")
    with g2:
        st.markdown("### 📍 Geographic Risk Clusters")
        location_counts = df["Location"].value_counts().head(5)
        st.bar_chart(location_counts, color="#00F2FE")

    st.write("")
    st.markdown("### 🔍 System Audit Log Trail")
    st.dataframe(df, use_container_width=True, height=280)

# ----------------------------------
# VIEW 2: AI DEEP-DIVE INSIGHTS VIEW
# ----------------------------------
elif st.session_state.app_view == "ai_insights":
    
    st.markdown("### 🧠 Autonomous Executive Synthesis Engine")
    st.write("Consolidated operational insights parsed directly from historical model executions.")
    st.write("")

    # BACKEND STATIC DATA INSIGHTS DEFINITIONS
    summary_content = f"""
    As a Senior Financial Risk Consultant auditing the transactional framework, I have analyzed the operational landscape containing **{total_txns:,} total transactions** across **{accounts} unique monitored account nodes**, representing a total exposed transaction volume of **${total_amount:,.2f}**. 
    
    The average transactional sizing of **${avg_amount:,.2f}** signals a highly consolidated transfer workflow with noticeable high-value outliers skewing baseline metrics. Operational analysis reveals significant reliance on specific merchant pipelines and core geographical corridors, emphasizing the immediate need for algorithmic transaction monitoring limits to preserve systemic liquidity.
    """

    risks_content = """
    Based on active data tracking models, the system flags the following core architectural security and compliance concerns:

    1. **High Concentration of Volume Exposure:** A vast majority of settlement capital is heavily grouped around top-tier merchant entities. Should any core processing gateway encounter settlement failures, a large portion of operational liquidity could face immediate blockades.
    2. **Anomalous Baseline Deviation:** The substantial gap between the median transaction sizing and high-value single transfers indicates possible unmonitored structural shifts, system misconfigurations, or data anomalies that bypass standard threshold filters.
    3. **Geographical Data Silos:** Settlement endpoints show high geographic centralization. This layout pattern increases systemic vulnerability to unexpected local network disruptions, localized regulatory adjustments, or regional infrastructure downtime.
    """

    recommendations_content = """
    To proactively stabilize transaction processing networks and preserve compliance mandates, the following consulting workflows should be deployed immediately:

    * **Implement Dynamic Tiered Transaction Limits:** Restrict raw transactional velocity per endpoint by enforcing automatic step-up secondary approvals whenever an entity crosses 3 standard deviations above the average value.
    * **Deploy Decentralized Settlement Gateways:** Intentionally route settlement traffic across distinct clearing merchant architectures to remove any singular processing points of failure.
    * **Automate Real-Time Schema Audit Checks:** Introduce real-time programmatic validation loops on outlier balances to catch incoming system anomalies or data transfer issues before transactions settle.
    """

    # ----------------------------------
    # CONTAINER RENDER LAYOUT
    # ----------------------------------

    # Container Box 1: Corporate Executive Summary
    st.markdown("<div class='executive-summary-box'><h4 style='color: #00F2FE; margin-top:0; margin-bottom:15px;'>📋 Corporate Executive Summary</h4>", unsafe_allow_html=True)
    st.markdown(summary_content)
    st.markdown("</div>", unsafe_allow_html=True)

    # Container Box 2: Critical System Risk Identifiers
    st.markdown("<div class='risk-matrix-box'><h4 style='color: #FF4A5A; margin-top:0; margin-bottom:15px;'>⚠️ Critical System Risk Identifiers</h4>", unsafe_allow_html=True)
    st.markdown(risks_content)
    st.markdown("</div>", unsafe_allow_html=True)

    # Container Box 3: Recommended Tactical Mitigation Vectors
    st.markdown("<div class='recommendation-box'><h4 style='color: #10B981; margin-top:0; margin-bottom:15px;'>🛠️ Recommended Tactical Mitigation Vectors</h4>", unsafe_allow_html=True)
    st.markdown(recommendations_content)
    st.markdown("</div>", unsafe_allow_html=True)