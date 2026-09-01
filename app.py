import streamlit as st
import time
from agent_engine import run_transformation_agent

st.set_page_config(page_title="AI Transformation Co-Pilot", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for a clean, bright, white/purple consulting aesthetic
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; color: #1E1E1E; }
    .main-header { font-size: 32px; font-weight: 800; color: #7B00FF; margin-bottom: 5px; }
    .sub-header { font-size: 16px; color: #555555; margin-bottom: 25px; }
    .instruction-card { background-color: #E8F0FE; padding: 18px; border-radius: 8px; border-left: 5px solid #1A73E8; margin-bottom: 25px; font-size: 15px; }
    .result-box { background-color: #FFFFFF; padding: 25px; border-radius: 8px; border: 1px solid #E0E0E0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-top: 20px;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">Enterprise Architecture & AI Co-Pilot</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Automated "As-Is" to "To-Be" Process Mapping for Business Architects</div>', unsafe_allow_html=True)

# Clear instructions for the user/recruiter
st.markdown("""
<div class="instruction-card">
<b>ℹ️ How to use this tool:</b><br>
1. Read the sample <b>Current Business Problem</b> in the text box below (or type a new one).<br>
2. Click the <b>Generate Future-State Architecture</b> button.<br>
3. The AI will analyze the legacy process and instantly generate a professional consulting blueprint.
</div>
""", unsafe_allow_html=True)

user_process = st.text_area(
    "Current Business Problem (As-Is State):",
    value="During my tenure at Canara Bank, rural CASA onboarding and HNI client documentation required manual KYC verification and physical document routing. This created a 2-3 day lag in account activation, high error rates, and hindered our digital banking outreach targets.",
    height=110
)

if st.button("⚡ Generate Future-State Architecture", type="primary"):
    with st.status("Analyzing business processes...", expanded=True) as status:
        st.write("🔍 Identifying operational bottlenecks...")
        time.sleep(1)
        st.write("📐 Formulating To-Be Cloud architecture...")
        time.sleep(1)
        st.write("📊 Generating Executive Summary...")
        time.sleep(1)
        res = run_transformation_agent(user_process)
        status.update(label="Consulting Blueprint Ready!", state="complete", expanded=False)

    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Transformation Score", f"{res['score']}/100")
    col2.metric("Implementation Complexity", res['complexity'])
    col3.metric("Target Platform", res['platform'])

    st.markdown("---")
    st.markdown(f"**🚨 As-Is Bottleneck Identified:**<br>{res['bottleneck']}", unsafe_allow_html=True)
    st.markdown(f"**✅ To-Be Architecture (Proposed):**<br>{res['architecture']}", unsafe_allow_html=True)
    st.markdown(f"**⚖️ Fit-Gap Summary:**<br>{res['fit_gap']}", unsafe_allow_html=True)
    
    st.info(f"**💼 Executive Readout for Client Leadership:**\n\n{res['executive_summary']}")
    
    st.markdown('</div>', unsafe_allow_html=True)
