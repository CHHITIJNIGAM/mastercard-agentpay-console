import streamlit as st
import time
from agent_engine import process_circular_query

st.set_page_config(page_title="GenAI Branch Knowledge Copilot", layout="wide")

st.markdown("""
    <style>
    .main-header { font-size: 30px; font-weight: 800; color: #0f52ba; margin-bottom: 5px; }
    .sub-text { font-size: 15px; color: #444; margin-bottom: 25px; }
    .response-card { background-color: #f8f9fa; padding: 22px; border-radius: 8px; border-left: 5px solid #0f52ba; margin-top: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .insight-card { background-color: #fff3cd; padding: 18px; border-radius: 8px; border-left: 5px solid #ffc107; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">Enterprise GenAI Branch Copilot</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">AI-powered retrieval of Master Circulars, Documentation Requirements, and Scheme Updates to empower front-line staff.</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])
with col1:
    query_type = st.selectbox(
        "Select Query Category:", 
        ["Documentation & KYC", "Scheme Updates & Facilities", "Exceptions & Error Handling"]
    )
    
with col2:
    if query_type == "Documentation & KYC":
        default_q = "What is the updated documentation required to open an NRE account for an HNI client residing in the UAE?"
    elif query_type == "Scheme Updates & Facilities":
        default_q = "What are the latest limit enhancements and withdrawal rules for the Senior Citizen Savings Scheme (SCSS)?"
    else:
        default_q = "A rural customer's PM Kisan scheme DBT failed due to an Aadhaar-NPCI mapping error. How do I resolve this?"
        
    user_query = st.text_area("Describe your operational question:", value=default_q, height=85)

if st.button("⚡ Query Internal Knowledge Base", type="primary"):
    with st.spinner("AI parsing query, retrieving internal Master Circulars, and synthesizing guidelines..."):
        time.sleep(1.2)
        res = process_circular_query(query_type, user_query)
        
    m1, m2 = st.columns(2)
    m1.metric("Operational Domain", res["category"])
    m2.metric("Retrieval Confidence", f"{res['confidence']}%")
    
    st.markdown('<div class="response-card">', unsafe_allow_html=True)
    st.markdown(f"**📑 Sourced from Internal Policy:** `{res['circular_ref']}`")
    st.markdown("**✅ Synthesized Guidelines:**")
    st.text(res["resolution"])
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="insight-card">', unsafe_allow_html=True)
    st.markdown("**🚀 Architect's Insight (To-Be Automation):**")
    st.markdown(res["automation_insight"])
    st.markdown('</div>', unsafe_allow_html=True)
