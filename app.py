import streamlit as st
import pandas as pd
import random
import time
from agent_engine import run_transformation_agent

st.set_page_config(page_title="Accenture Reinvention Co-Pilot", layout="wide", page_icon="⚡")

st.markdown("""
    <style>
    .main-header { font-size: 26px; font-weight: 700; color: #A100FF; margin-bottom: 2px; }
    .sub-header { font-size: 14px; color: #4B0082; margin-bottom: 15px; }
    .reasoning-box { background-color: #f8f9fa; padding: 14px; border-radius: 8px; border-left: 4px solid #A100FF; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">Accenture Reinvention Co-Pilot | Functional Architecture Suite</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">AI-Accelerated As-Is/To-Be Process Decomposition, Fit-Gap Analysis & Program Governance</div>', unsafe_allow_html=True)

# Session State
if "transformation_ledger" not in st.session_state:
    st.session_state.transformation_ledger = []
if "cutover_risks" not in st.session_state:
    st.session_state.cutover_risks = []

tab1, tab2 = st.tabs(["🚀 As-Is to To-Be Architecture & Fit-Gap", "🛡️ Program Governance & Risk Ledger"])

with tab1:
    st.sidebar.header("⚙️ Architecture & Governance Controls")
    groq_api_key = st.sidebar.text_input("Groq API Key (Optional)", type="password", placeholder="gsk_...")
    st.sidebar.caption("Engine: **Llama 3.3 70B Versatile** via Groq")
    
    target_platform = st.sidebar.selectbox(
        "Target Enterprise Platform",
        ["Private Cloud Core (Red Hat / OpenShift)", "Hybrid Cloud Microservices", "Mainframe Modernization Layer", "Databricks & Multi-Cloud Lakehouse"]
    )
    budget_milestone = st.sidebar.slider("Program Milestone Allocation ($M)", min_value=0.5, max_value=10.0, value=2.5, step=0.5)

    st.sidebar.markdown("---")
    st.sidebar.caption("Accenture Methodology: **Reinvention Services v4.2**")
    st.sidebar.caption("Career Track: **Business & Functional Architect (CL10)**")

    # User Input
    user_process = st.text_area(
    "Current Business Problem (As-Is State):",
    value="During my tenure at Canara Bank, rural CASA onboarding and HNI client documentation required manual KYC verification and physical document routing. This created a 2-3 day lag in account activation, high error rates, and hindered our digital banking outreach targets.",
    height=110
)

    col_btn, col_clear = st.columns([3, 7])
    with col_btn:
        run_clicked = st.button("⚡ Generate To-Be Architecture & Fit-Gap", type="primary")
    with col_clear:
        if st.button("🗑️ Clear Architecture Ledger"):
            st.session_state.transformation_ledger = []
            st.rerun()

    if run_clicked:
        with st.status("Decomposing Requirements & Formulating To-Be Architecture...", expanded=True) as status:
            st.write("🔍 **Requirement & Bottleneck Decomposition:** Parsing legacy workflow constraints...")
            res = run_transformation_agent(
                business_use_case=user_process,
                target_platform=target_platform,
                budget_milestone_m=budget_milestone,
                groq_api_key=groq_api_key
            )
            time.sleep(0.5)
            
            st.write(f"📐 **Fit-Gap & Platform Mapping:** Aligning capabilities with {target_platform}...")
            time.sleep(0.5)
            st.write("📊 **Executive Storytelling Engine:** Synthesizing C-suite value proposition & risk posture...")
            time.sleep(0.4)
            status.update(label="Functional Architecture & Executive Readout Ready!", state="complete", expanded=False)

        # Log to ledger
        st.session_state.transformation_ledger.insert(0, {
            "Initiative ID": res.initiative_id,
            "Timestamp": res.timestamp,
            "Target Platform": res.target_platform,
            "Complexity": res.complexity_level,
            "Transformation Score": f"{res.transformation_score}/100",
            "Governance Status": res.governance_status,
            "Fit-Gap Summary": res.fit_gap_summary,
            "Executive Readout": res.executive_readout
        })

        # Summary Metrics
        st.subheader("Transformation Blueprint & Readout")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Initiative ID", res.initiative_id)
            st.metric("Transformation Readiness", f"{res.transformation_score}/100")
        with col2:
            st.metric("Modernization Complexity", res.complexity_level)
            st.metric("Governance Decision", res.governance_status)
        with col3:
            st.metric("Target Platform", res.target_platform.split()[0])
            st.metric("Delivery Mode", "Agile Sprints (CL10 Managed)")

        # Detailed cards
        st.markdown(f"**As-Is Operational Bottleneck:** {res.as_is_bottleneck}")
        st.markdown(f"**To-Be Future-State Design:** {res.to_be_architecture}")
        st.markdown(f"**Fit-Gap Analysis:** {res.fit_gap_summary}")
        
        st.markdown(f'<div class="reasoning-box">💼 <b>Executive Leadership Summary:</b><br>{res.executive_readout}<br><br><small><b>Functional Architecture Reasoning:</b> {res.architect_reasoning}</small></div>', unsafe_allow_html=True)

    # Historical Table
    st.markdown("---")
    st.subheader("📜 Enterprise Transformation Roadmap & History")
    if len(st.session_state.transformation_ledger) > 0:
        df_ledger = pd.DataFrame(st.session_state.transformation_ledger)
        st.dataframe(df_ledger, use_container_width=True)
    else:
        st.info("No transformation assessments logged yet. Run a workflow above to populate the ledger.")

with tab2:
    st.subheader("🛡️ Cutover Readiness & Program Risk Register")
    st.markdown("Manage migration cutover risks, data reconciliation dependencies, and platform change management tracking.")

    if len(st.session_state.transformation_ledger) == 0:
        st.warning("Generate at least one transformation assessment in Tab 1 to track cutover risks.")
    else:
        init_options = {f"{t['Initiative ID']} - {t['Target Platform']} ({t['Complexity']} Complexity)": t for t in st.session_state.transformation_ledger}
        selected_label = st.selectbox("Select Transformation Initiative:", list(init_options.keys()))
        selected_init = init_options[selected_label]

        risk_category = st.selectbox("Select Cutover Risk Category:", [
            "DATA-MIG: Data reconciliation & legacy field mapping discrepancies",
            "SEC-RBAC: Role-based access control and security compliance gap",
            "PERF-LAT: Latency during cutover parallel run phase",
            "CHG-ADOPT: User change resistance and training lag"
        ])

        mitigation_strategy = st.text_area("Proposed Mitigation & Governance Action Plan:", value="Execute automated parallel-run validation for 14 days and establish automated reconciliation triggers before full cutover.")

        if st.button("📌 Register Cutover Governance Action", type="primary"):
            with st.spinner("Updating program governance register..."):
                time.sleep(0.8)
            
            risk_id = f"RSK-{random.randint(100, 999)}"
            risk_entry = {
                "Risk ID": risk_id,
                "Initiative ID": selected_init["Initiative ID"],
                "Category": risk_category.split(":")[0],
                "Mitigation Strategy": mitigation_strategy,
                "Status": "MITIGATION IN PROGRESS"
            }
            st.session_state.cutover_risks.insert(0, risk_entry)
            st.success(f"Risk `{risk_id}` successfully registered in Program Governance Register.")

        st.markdown("---")
        st.subheader("📂 Program Cutover & Risk Matrix")
        if len(st.session_state.cutover_risks) > 0:
            df_risks = pd.DataFrame(st.session_state.cutover_risks)
            st.dataframe(df_risks, use_container_width=True)
        else:
            st.info("No active risk items logged.")
