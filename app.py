import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time
from agent_engine import (
    evaluate_digital_onboarding, 
    get_core_banking_fitgap_matrix, 
    calculate_transformation_roi
)

st.set_page_config(page_title="FinReinvent AI | BFSI Architecture Suite", layout="wide", page_icon="🏦")

# Custom enterprise styling
st.markdown("""
    <style>
    .main-title { font-size: 28px; font-weight: 800; color: #4B0082; margin-bottom: 2px; }
    .sub-title { font-size: 14px; color: #555555; margin-bottom: 18px; }
    .kpi-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 15px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    .callout-box { background-color: #F3E8FF; border-left: 5px solid #7B00FF; padding: 12px; border-radius: 4px; font-size: 14px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">FinReinvent AI | Enterprise Banking Transformation Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Core Banking Modernization, Process Re-Engineering (As-Is / To-Be) & Digital Architecture Suite</div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs([
    "⚡ Digital CASA & e-KYC Pipeline", 
    "💼 HNI Portfolio & Risk Engine", 
    "🏛️ CBS Mainframe Fit-Gap Matrix", 
    "📊 Executive ROI & Governance"
])

# ----------------- TAB 1: CASA PIPELINE -----------------
with tab1:
    st.markdown("""
    <div class="callout-box">
    <b>Operational Context:</b> Re-engineering high-volume rural and semi-urban CASA onboarding workflows from manual branch verification to an automated AI-driven straight-through-processing (STP) architecture.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Simulate Account Application")
        channel = st.selectbox("Acquisition Channel", ["Rural Business Correspondent (BC)", "Mobile Banking App", "Branch Walk-in", "HNI Desk"])
        customer_segment = st.selectbox("Customer Segment", ["Standard CASA", "Rural / Financial Inclusion", "High Net-Worth Individual (HNI)", "High Risk"])
        init_deposit = st.number_input("Initial Deposit Amount (₹)", min_value=500, max_value=5000000, value=25000, step=5000)
        
        btn_process = st.button("🚀 Run Architecture Pipeline", type="primary")

    with col2:
        st.subheader("Process Performance Telemetry")
        if btn_process:
            with st.status("Executing Multi-Stage Verification Pipeline...", expanded=True) as status:
                st.write("1. 📡 Ingesting application payload via API Gateway...")
                time.sleep(0.3)
                st.write("2. 🔍 Real-time biometric Aadhaar/PAN OCR parsing...")
                time.sleep(0.3)
                st.write("3. ⚖️ Evaluating automated AML & credit rules...")
                time.sleep(0.3)
                status.update(label="Onboarding Pipeline Executed!", state="complete", expanded=False)

            res = evaluate_digital_onboarding(channel, customer_segment, init_deposit)
            
            m1, m2, m3 = st.columns(3)
            m1.metric("Application ID", res.applicant_id)
            m2.metric("KYC Processing SLA", res.processing_time, delta="-94% vs Legacy")
            m3.metric("AML Fraud Trust Score", f"{res.fraud_risk_score}/100")

            st.success(f"**Pipeline Status:** {res.kyc_status}")
            st.info(f"**Audit & Traceability Log:** {res.audit_trail}")

        # Benchmark comparison chart
        df_sla = pd.DataFrame({
            "Stage": ["Document Sourcing", "Physical Verification", "AML/Risk Scrub", "CBS Account Creation"],
            "Legacy As-Is (Hours)": [24, 24, 18, 6],
            "Modern To-Be (Minutes)": [1.5, 0.8, 1.2, 0.5]
        })
        fig = px.bar(df_sla, x="Stage", y=["Legacy As-Is (Hours)"], title="Legacy As-Is Bottleneck Analysis (Hours per Step)", barmode="group", color_discrete_sequence=["#EF4444"])
        st.plotly_chart(fig, use_container_width=True)

# ----------------- TAB 2: HNI PORTFOLIO -----------------
with tab2:
    st.markdown("""
    <div class="callout-box">
    <b>Operational Context:</b> Systematic portfolio allocation and credit underwriting for HNI relationships (calibrated to ₹4.5 Cr annual mobilization targets).
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 2])
    with c1:
        st.subheader("HNI Client Profile")
        hni_networth = st.slider("Relationship Portfolio Value (₹ Lakhs)", 25, 500, 150)
        risk_profile = st.select_slider("Risk Appetite", options=["Conservative", "Moderate", "Growth", "Aggressive"])
        product_mix = st.multiselect("Active Products", ["Term Deposits (FD)", "Mutual Fund SIPs", "Sovereign Gold Bonds", "Commercial Credit Line"], default=["Term Deposits (FD)", "Mutual Fund SIPs"])
        
    with c2:
        st.subheader("Automated Asset Allocation & Yield Optimization")
        if risk_profile == "Conservative":
            alloc = [60, 20, 15, 5]
        elif risk_profile == "Moderate":
            alloc = [40, 35, 15, 10]
        elif risk_profile == "Growth":
            alloc = [20, 50, 15, 15]
        else:
            alloc = [10, 65, 10, 15]

        fig_pie = px.pie(
            values=alloc, 
            names=["Fixed Income / CASA", "Equity / Mutual Funds", "Government Securities", "Alternate / Liquid"], 
            title=f"Optimized Asset Mix ({risk_profile} Strategy)",
            color_discrete_sequence=px.colors.sequential.Purp
        )
        st.plotly_chart(fig_pie, use_container_width=True)

# ----------------- TAB 3: FIT-GAP MATRIX -----------------
with tab3:
    st.subheader("🏛️ Core Banking (CBS / Mainframe) Modernization Matrix")
    st.markdown("Functional fit-gap evaluation for transitioning legacy monolith CBS modules to private cloud microservices (OpenShift/IBM Red Hat architecture).")

    matrix_data = get_core_banking_fitgap_matrix()
    df_matrix = pd.DataFrame(matrix_data)
    st.dataframe(df_matrix, use_container_width=True)

    st.markdown("---")
    st.subheader("Transformation Cutover Risk Summary")
    r1, r2, r3 = st.columns(3)
    r1.metric("Target Architecture Fit", "84.4%", "Enterprise Standard")
    r2.metric("High-Severity Gaps", "1 Domain", "BRMS Integration")
    r3.metric("Modernization Readiness", "Stage 3 (Cutover Ready)")

# ----------------- TAB 4: ROI & GOVERNANCE -----------------
with tab4:
    st.subheader("📊 Executive Business Case & Transformation ROI")
    
    g1, g2 = st.columns(2)
    with g1:
        volume = st.number_input("Annual CASA Onboarding Volume", min_value=1000, max_value=1000000, value=50000, step=5000)
        curr_cost = st.slider("Current As-Is Cost per Account (₹)", 200, 1200, 650)
        target_cost = st.slider("Projected To-Be Cost per Account (₹)", 25, 200, 65)

    roi = calculate_transformation_roi(volume, curr_cost, target_cost)

    with g2:
        st.markdown("**Executive Transformation Metrics**")
        st.metric("Annual Operational Savings", f"₹ {roi['annual_savings_inr']:,.0f}")
        st.metric("Process Turnaround Reduction", f"{roi['sla_reduction_pct']}%")
        st.metric("Estimated Payback Period", f"{roi['payback_period_months']} Months")

    st.markdown("---")
    st.markdown("""
    ### 💼 C-Level Leadership Readout
    > **Strategic Recommendation:** Migrating from legacy branch-tethered CASA processing to a cloud-native API architecture delivers an estimated **₹ 2.92+ Cr** in annual operational efficiency, reduces onboarding SLA from **72 hours to under 5 minutes**, and completely mitigates manual audit reconciliation discrepancies.
    """)
