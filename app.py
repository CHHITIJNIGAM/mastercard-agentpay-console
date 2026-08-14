import streamlit as st
import pandas as pd
import random
import time
from agent_engine import run_agentic_workflow_with_llm

st.set_page_config(page_title="TrustPay | Mastercard Agentic Commerce", layout="wide", page_icon="💳")

# Custom CSS styling
st.markdown("""
    <style>
    .main-header { font-size: 26px; font-weight: 700; color: #EB001B; margin-bottom: 2px; }
    .sub-header { font-size: 14px; color: #F79E1B; margin-bottom: 15px; }
    .reasoning-box { background-color: #f0f2f6; padding: 12px; border-radius: 8px; border-left: 4px solid #F79E1B; margin-top: 10px; font-style: italic; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">Mastercard Agent Pay & KYA Governance Console</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Tokenized Rails & Verifiable Intent for Autonomous AI Agents</div>', unsafe_allow_html=True)

# Initialize Session State
if "audit_ledger" not in st.session_state:
    st.session_state.audit_ledger = []
if "disputes" not in st.session_state:
    st.session_state.disputes = []

# Navigation Tabs
tab1, tab2 = st.tabs(["💳 Agentic Purchase & Audit Ledger", "⚖️ Dispute & Chargeback Simulator"])

with tab1:
    # Sidebar: Governance & LLM Config
    st.sidebar.header("🛡️ Agent Identity & Governance")
    groq_api_key = st.sidebar.text_input("Groq API Key (Free LLM)", type="password", placeholder="gsk_...")
    st.sidebar.caption("Powered by **Llama 3.3 70B Versatile** via Groq")
    
    agent_id = st.sidebar.text_input("Agent Identity (KYA ID)", value="AGT-MC-2026-X8", key="tab1_agent_id")
    delegated_owner = st.sidebar.text_input("Delegated Human Principal", value="Cardholder: C. Nigam", key="tab1_owner")
    spending_cap = st.sidebar.slider("Delegated Spend Limit ($)", min_value=10.0, max_value=300.0, value=100.0, step=5.0, key="tab1_slider")

    st.sidebar.markdown("---")
    st.sidebar.caption("Mastercard Tokenization Rails: **Active (MDES-Ready)**")
    st.sidebar.caption("Protocol: **Know Your Agent (KYA) v2.1**")

    # Main Input
    user_prompt = st.text_input(
        "Enter Natural Language Purchase Intent:", 
        value="Find a dermatologist-recommended anti-dandruff shampoo with tea tree oil under $40."
    )

    col_btn, col_clear = st.columns([2, 8])
    with col_btn:
        execute_clicked = st.button("🚀 Execute Autonomous Purchase", type="primary")
    with col_clear:
        if st.button("🗑️ Clear Audit Ledger"):
            st.session_state.audit_ledger = []
            st.rerun()

    if execute_clicked:
        with st.status("Executing Agentic Pipeline & Mastercard Guardrails...", expanded=True) as status:
            st.write("🧠 **LLM Agent Reasoning:** Contacting Llama-3.3-70B to evaluate product catalogs & intent match...")
            
            res = run_agentic_workflow_with_llm(
                user_intent=user_prompt, 
                max_budget=spending_cap, 
                agent_id=agent_id, 
                groq_api_key=groq_api_key
            )
            time.sleep(0.6)
            
            st.write(f"⚖️ **KYA Risk Evaluator:** Checking trust credentials against spending cap (${spending_cap:.2f})...")
            time.sleep(0.6)
            
            if res.is_approved:
                st.write(f"🔒 **Mastercard Token Engine:** Minting single-use Agentic Token `{res.token_id}`...")
                time.sleep(0.6)
                st.write("⚡ **Settlement Network:** Verifying cryptogram with merchant acquirer...")
                time.sleep(0.4)
                status.update(label="Transaction Authorized & Settled on Rails!", state="complete", expanded=False)
            else:
                status.update(label="Transaction Blocked by Guardrail Policy", state="error", expanded=False)

        # Log into Ledger
        st.session_state.audit_ledger.insert(0, {
            "ID": f"TXN-{len(st.session_state.audit_ledger)+101}",
            "Timestamp": res.timestamp,
            "Agent ID": agent_id,
            "Item": res.selected_item["name"],
            "Price ($)": res.selected_item['price'],
            "KYA Score": f"{res.kya_trust_score}/100",
            "Decision": "APPROVED" if res.is_approved else "DECLINED",
            "Token / Cryptogram": res.token_id if res.is_approved else res.rejection_reason,
            "Cryptogram Hash": res.cryptogram if res.is_approved else "N/A"
        })

        # Summary Cards
        st.subheader("Latest Execution Result")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Selected Item (LLM Match)", res.selected_item["name"])
            st.metric("Price", f"${res.selected_item['price']:.2f}")
        with col2:
            st.metric("KYA Trust Score", f"{res.kya_trust_score}/100")
            st.metric("Governance Decision", "APPROVED" if res.is_approved else "REJECTED")
        with col3:
            st.metric("Mastercard Token ID", res.token_id if res.is_approved else "N/A")
            st.metric("Settlement Status", "Settled on Rails" if res.is_approved else "Declined")

        # Agent Reasoning Display
        st.markdown(f'<div class="reasoning-box">💡 <b>Agent Thought Process:</b> {res.agent_reasoning}</div>', unsafe_allow_html=True)

        if not res.is_approved:
            st.error(f"**Policy Block:** {res.rejection_reason}")
        else:
            st.success(f"**Proof of Intent Verified:** Single-use cryptogram `{res.cryptogram}` successfully cleared.")

    # Live Audit Ledger Table
    st.markdown("---")
    st.subheader("📜 Real-Time Network Audit Ledger")
    if len(st.session_state.audit_ledger) > 0:
        df_ledger = pd.DataFrame(st.session_state.audit_ledger)
        st.dataframe(df_ledger, use_container_width=True)
    else:
        st.info("No transactions logged yet. Run a purchase above to generate audit entries.")

with tab2:
    st.subheader("⚖️ Mastercard Agentic Dispute & Chargeback Simulator")
    st.markdown("If a human principal claims an autonomous agent violated instructions, exceeded behavioral intent, or made an unauthorized purchase, initiate a chargeback claim here.")

    approved_txns = [t for t in st.session_state.audit_ledger if t["Decision"] == "APPROVED"]

    if len(approved_txns) == 0:
        st.warning("No approved transactions available to dispute. Please execute a successful purchase in Tab 1 first.")
    else:
        txn_options = {f"{t['ID']} - {t['Item']} (${t['Price ($)']:.2f}) [Token: {t['Token / Cryptogram']}]": t for t in approved_txns}
        selected_txn_label = st.selectbox("Select Transaction to Dispute:", list(txn_options.keys()))
        selected_txn = txn_options[selected_txn_label]

        dispute_reason = st.selectbox("Select Dispute / Chargeback Reason Code:", [
            "RC-44: Agent Intent Mismatch (Purchased item outside user prompt instructions)",
            "RC-48: Unauthorized Delegation Bounds (Exceeded contextual policy limit)",
            "RC-52: Merchant Fraud / Non-Delivery by Agentic API"
        ])

        dispute_evidence = st.text_area("Human Principal Statement / Evidence Notes:", value="Agent misinterpreted prompt parameters and purchased a higher-tier item without explicit secondary confirmation.")

        if st.button("🚨 File Agentic Chargeback Claim", type="primary"):
            with st.spinner("Submitting chargeback claim to Mastercard Dispute Resolution (MDR)..."):
                time.sleep(1.0)
                
            rand_suffix = random.randint(1000, 9999)
            claim_id = f"CHGBK-{rand_suffix}-{len(st.session_state.disputes)+1}"
            
            dispute_record = {
                "Claim ID": claim_id,
                "Txn ID": selected_txn["ID"],
                "Item": selected_txn["Item"],
                "Amount": f"${selected_txn['Price ($)']:.2f}",
                "Reason": dispute_reason.split(":")[0],
                "Cryptogram Verified": selected_txn["Cryptogram Hash"],
                "Status": "PROVISIONAL CREDIT ISSUED (Under Arbitration)"
            }
            st.session_state.disputes.insert(0, dispute_record)
            st.success(f"Chargeback successfully filed! Claim ID: `{claim_id}`. Provisional credit issued to cardholder.")

        st.markdown("---")
        st.subheader("📂 Active Dispute & Chargeback Registry")
        if len(st.session_state.disputes) > 0:
            df_disputes = pd.DataFrame(st.session_state.disputes)
            st.dataframe(df_disputes, use_container_width=True)
        else:
            st.info("No active disputes filed.")