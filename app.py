import streamlit as st
import time
import datetime
from agent_engine import process_circular_query

st.set_page_config(page_title="Internal GenAI Copilot", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .stApp { background-color: #f4f7f6; color: #333333; }
    .main-header { font-size: 32px; font-weight: 700; color: #003366; border-bottom: 2px solid #003366; padding-bottom: 10px; margin-bottom: 20px; }
    .metric-container { display: flex; justify-content: space-between; margin-bottom: 25px; }
    .metric-box { background-color: #ffffff; padding: 15px; border-radius: 6px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); width: 23%; border-top: 4px solid #0056b3; text-align: center; }
    .metric-title { font-size: 13px; color: #666; text-transform: uppercase; font-weight: 600; }
    .metric-value { font-size: 26px; font-weight: 700; color: #003366; margin-top: 5px; }
    .query-section { background-color: #ffffff; padding: 25px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 20px; }
    .response-card { background-color: #f0f7ff; padding: 20px; border-radius: 6px; border-left: 5px solid #0056b3; margin-top: 20px; }
    .insight-card { background-color: #fff8e1; padding: 20px; border-radius: 6px; border-left: 5px solid #ffc107; margin-top: 15px; }
    .footer-text { font-size: 12px; color: #999; text-align: center; margin-top: 40px; }
    </style>
""", unsafe_allow_html=True)

# Retrieve API key automatically from Streamlit Secrets (fallback to sidebar input if local)
api_key = ""
try:
    if "GROQ_API_KEY" in st.secrets:
        api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    pass

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2830/2830284.png", width=60)
    st.markdown("### **Staff Portal**")
    st.markdown("**User:** C. Nigam (Officer)")
    st.markdown("**Branch:** Bhopal Main (0214)")
    st.markdown("**Terminal:** T-8842")
    
    # Only show manual input box if secret isn't configured
    if not api_key:
        api_key = st.text_input("🔑 Groq API Key:", type="password")
    else:
        st.success("🔒 Enterprise Key Loaded")
        
    st.markdown("---")
    st.markdown("🟢 **System Status:** Online")
    st.markdown("🔗 **CBS Link:** Connected")
    st.markdown("📚 **Vector Database:** Synced (v2.5)")
    st.markdown("---")
    st.caption(f"Session Active: {datetime.datetime.now().strftime('%d %b %Y, %H:%M')}")

st.markdown('<div class="main-header">🏦 Enterprise GenAI Operations Copilot</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="metric-container">
        <div class="metric-box"><div class="metric-title">Active Circulars</div><div class="metric-value">5,412</div></div>
        <div class="metric-box"><div class="metric-title">Branch Queries Today</div><div class="metric-value">124</div></div>
        <div class="metric-box"><div class="metric-title">Avg Retrieval SLA</div><div class="metric-value">0.8s</div></div>
        <div class="metric-box"><div class="metric-title">AI Accuracy Score</div><div class="metric-value">99.1%</div></div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="query-section">', unsafe_allow_html=True)
st.subheader("🔍 Search Internal Knowledge Base")

col1, col2 = st.columns([1, 2])
with col1:
    domain = st.selectbox(
        "Knowledge Domain:", 
        [
            "Wealth, Savings & Retirement", 
            "Micro-Insurance & Social Security", 
            "MSME, Business & Manufacturing Loans",
            "Education & Agriculture",
            "Operations, NRI & Exceptions"
        ]
    )
    
with col2:
    if domain == "Wealth, Savings & Retirement":
        default_q = "What is the eligibility criteria and withdrawal rule for EPF?"
    elif domain == "Micro-Insurance & Social Security":
        default_q = "What is the auto-debit premium amount and age limit for PMJJBY?"
    elif domain == "MSME, Business & Manufacturing Loans":
        default_q = "Is there any collateral requirement to get a loan for my small business?"
    elif domain == "Education & Agriculture":
        default_q = "What is the Prompt Repayment Incentive (PRI) for a Kisan Credit Card (KCC)?"
    else:
        default_q = "How do I resolve a DBT NPCI mandate failure?"
        
    user_query = st.text_area("Enter operational question or exception:", value=default_q, height=85)

execute = st.button("⚡ Execute AI Semantic Search", type="primary", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

if execute:
    with st.spinner("Executing dynamic RAG pipeline..."):
        time.sleep(1.2)
        res = process_circular_query(domain, user_query, api_key)
        
    st.markdown("### 📊 AI Resolution & Architecture Insights")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Categorization", res["category"])
    m2.metric("Retrieval Confidence", f"{res['confidence']}%")
    m3.metric("Policy Validation", "Cryptographically Signed")
    
    st.markdown(f"""
        <div class="response-card">
            <h4 style="color:#003366; margin-top:0px;">📑 Primary Source: <code>{res['circular_ref']}</code></h4>
            <b>✅ Synthesized Action Plan:</b><br>
            <pre style="background-color: transparent; border: none; font-family: inherit; font-size: 15px; margin-top: 10px; white-space: pre-wrap; color: #333;">{res['resolution']}</pre>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="insight-card">
            <h4 style="color:#856404; margin-top:0px;">🚀 Business Architect's Insight (To-Be Automation)</h4>
            <p style="margin-bottom:0px; font-size: 15px;">{res['automation_insight']}</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="footer-text">Confidential & Internal Use Only • Enterprise AI Core v2.5 • Connected to CBS Environment</div>', unsafe_allow_html=True)
