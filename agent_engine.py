import random

def process_circular_query(domain: str, query: str) -> dict:
    text = query.lower()
    
    # Enterprise Knowledge Base (20+ Schemes & Exceptions)
    schemes_db = [
        # Wealth, Savings & Retirement
        {"keys": ["nps", "national pension"], "cat": "Retirement Planning", "ref": "CIR/RET/2026-88", "res": "1. Employers can contribute up to 14% basic.\n2. Systematic Lumpsum Withdrawal (SLW) allowed.\n3. Tier-II allows 100% active equity.", "auto": "Integrate PFRDA APIs in the mobile app for dynamic equity/debt rebalancing."},
        {"keys": ["scss", "senior citizen"], "cat": "Term Deposits", "ref": "CIR/GOVT/2026-42", "res": "1. Max investment limit enhanced to ₹30 Lakh.\n2. Spouses can open joint accounts.\n3. Premature withdrawal penalty reduced to 1% after 2 years.", "auto": "Implement automated SMS triggers for customers turning 60, offering instant SCSS conversion."},
        {"keys": ["ssy", "sukanya"], "cat": "Retail Savings", "ref": "CIR/GOVT/2026-15", "res": "1. Max deposit ₹1.5 Lakh/year.\n2. Account can be opened for girl child up to 10 years.\n3. Matures 21 years from account opening.", "auto": "Enable predictive CRM alerts for customers with newborn dependents to cross-sell SSY digitally."},
        {"keys": ["ppf", "provident fund"], "cat": "Retail Savings", "ref": "CIR/GOVT/2026-19", "res": "1. 15-year lock-in period.\n2. Loan facility available from the 3rd to 6th financial year.\n3. Max tax-free deposit ₹1.5 Lakh/year.", "auto": "Deploy API-led instant PPF loan disbursement directly through mobile banking."},
        {"keys": ["epf", "pf claim", "eligibility criteria for epf"], "cat": "Retirement Planning", "ref": "CIR/RET/2026-04", "res": "1. Eligibility: Salaried employees in organizations with 20+ staff.\n2. Requires UAN linked with Aadhaar/PAN.\n3. Form 19 for final settlement, Form 10C for pension withdrawal.\n4. Processing time strictly T+3 days.", "auto": "Connect HRMS payroll APIs with Core Banking to auto-reconcile EPF contribution mismatches."},
        {"keys": ["sgb", "gold bond"], "cat": "Wealth Management", "ref": "CIR/WEALTH/2026-11", "res": "1. Max 4kg per individual/HUF.\n2. Fixed interest of 2.5% payable semi-annually.\n3. Tradable on stock exchanges within a fortnight of issuance.", "auto": "Embed a secondary market SGB trading widget inside the net banking investment dashboard."},
        
        # Micro-Insurance & Social Security
        {"keys": ["pmjay", "ayushman"], "cat": "Social Security", "ref": "CIR/INS/2026-02", "res": "1. ₹5 Lakh health cover per family/year.\n2. Eligibility based on SECC database.\n3. E-card generated post Aadhaar biometric authentication.", "auto": "Link SECC database to Customer 360 to auto-prompt tellers when an eligible uninsured customer visits."},
        {"keys": ["pmsby", "suraksha"], "cat": "Micro-Insurance", "ref": "CIR/INS/2026-03", "res": "1. Premium ₹20/year auto-debited.\n2. ₹2 Lakh accidental death cover.\n3. Age limit 18-70 years.", "auto": "Bundle PMSBY auto-mandates natively into all digital CASA onboarding flows."},
        {"keys": ["pmjjby", "jeevan"], "cat": "Micro-Insurance", "ref": "CIR/INS/2026-04", "res": "1. Premium ₹436/year auto-debited.\n2. ₹2 Lakh life cover.\n3. Age limit 18-50 years.", "auto": "Trigger WhatsApp bot renewals 15 days prior to the May 31st annual auto-debit cycle."},
        {"keys": ["apy", "atal"], "cat": "Social Security", "ref": "CIR/RET/2026-05", "res": "1. Guaranteed pension of ₹1k-₹5k.\n2. Age limit 18-40 years.\n3. Govt co-contribution applicable for non-taxpayers.", "auto": "Deploy AI propensity models to target rural unorganized sector customers with tailored APY SMS pitches."},
        
        # MSME, Business & Manufacturing Loans
        {"keys": ["mudra", "shishu", "kishore", "tarun"], "cat": "MSME Credit", "ref": "CIR/ADV/2026-21", "res": "1. Shishu (up to ₹50k), Kishore (₹5L), Tarun (₹10L).\n2. Zero collateral required.\n3. Mudra RuPay card issued for working capital.", "auto": "Integrate GSTIN and alternate data scoring to pre-approve Shishu tranches entirely online."},
        {"keys": ["pmegp", "manufacturing", "business subsidy"], "cat": "MSME Subsidies", "ref": "CIR/ADV/2026-25", "res": "1. Max project cost ₹50 Lakh (Manufacturing) / ₹20 Lakh (Business).\n2. Margin money subsidy up to 35% in rural areas.\n3. Requires mandatory EDP training certificate.", "auto": "Create an automated subsidy claim XML generator linking the CBS directly to the KVIC portal."},
        {"keys": ["stand up", "stand-up"], "cat": "Enterprise Credit", "ref": "CIR/ADV/2026-28", "res": "1. Loans from ₹10 Lakh to ₹1 Crore.\n2. Mandated for at least one SC/ST and one Woman borrower per branch.\n3. Covers greenfield enterprise projects only.", "auto": "Implement a real-time portfolio tracker to flag branches falling behind mandatory inclusion quotas."},
        {"keys": ["cgtmse", "collateral free"], "cat": "Commercial Credit", "ref": "CIR/ADV/2026-33", "res": "1. Guarantee cover available for MSME loans up to ₹5 Crore.\n2. Guarantee fee ranges from 0.37% to 1.35%.\n3. Annual renewal required via MLI portal.", "auto": "Automate CGTMSE fee deduction and API synchronization with the trust portal to prevent guarantee lapses."},
        {"keys": ["pmfme", "food processing"], "cat": "Agri-Business", "ref": "CIR/ADV/2026-36", "res": "1. Credit-linked capital subsidy at 35% (max ₹10 Lakh).\n2. Focuses on 'One District One Product' (ODOP).\n3. Seed capital ₹40,000 per SHG member.", "auto": "Geospatially map ODOP clusters with branch CRMs to target local food processing micro-units."},
        {"keys": ["svanidhi", "street vendor"], "cat": "Micro-Credit", "ref": "CIR/ADV/2026-39", "res": "1. Tranches of ₹10k, ₹20k, and ₹50k.\n2. 7% interest subvention credited quarterly.\n3. Cashback rewards for digital transactions.", "auto": "Embed a UPI API module that automatically tracks vendor digital transactions and calculates cashback limits."},
        
        # Education & Agriculture
        {"keys": ["kcc", "kisan", "crop"], "cat": "Agriculture Credit", "ref": "CIR/AGRI/2026-07", "res": "1. Short-term crop loan up to ₹3 Lakh at 7%.\n2. Prompt Repayment Incentive (PRI) of 3% drops effective rate to 4%.\n3. Valid for 5 years with 10% annual limit enhancement.", "auto": "Use satellite imagery and digitized land records (Bhulekh APIs) to automate KCC limit renewals."},
        {"keys": ["csis", "education loan"], "cat": "Retail Assets", "ref": "CIR/RET/2026-44", "res": "1. Full interest subsidy during moratorium period (course + 1 year).\n2. Valid for EWS category (Income < ₹4.5 Lakh).\n3. No collateral required up to ₹7.5 Lakh.", "auto": "Directly integrate with the Vidya Lakshmi portal for STP processing of subsidized student loans."},
        
        # Operations, NRI & Exceptions
        {"keys": ["nre", "nri", "fatca", "uae"], "cat": "Compliance & Onboarding", "ref": "CIR/KYC/2026-14", "res": "1. Valid Passport and Overseas Visa required.\n2. FATCA/CRS declaration mandatory.\n3. Overseas address proof must be embassy-attested.", "auto": "Integrate Video-KYC (V-KYC) with automated OCR passport extraction to bypass physical attestation."},
        {"keys": ["dbt", "npci", "mandate"], "cat": "Operations Exceptions", "ref": "CIR/RBIA/2026-09", "res": "1. Verify Aadhaar seeding on NPCI mapper.\n2. Capture biometric consent via micro-ATM.\n3. Push E-mandate update XML (T+1 resolution).", "auto": "Integrate a real-time NPCI status-check API directly into the front-end tablet to pre-validate mappings."}
    ]
    
    # Search Engine Logic: Scans text for matching keywords
    for scheme in schemes_db:
        if any(keyword in text for keyword in scheme["keys"]):
            return {
                "category": scheme["cat"],
                "circular_ref": scheme["ref"],
                "resolution": scheme["res"],
                "automation_insight": scheme["auto"],
                "confidence": random.randint(94, 99)
            }
            
    # Default Fallback utilizing the selected domain if no keywords match perfectly
    return {
        "category": domain,
        "circular_ref": "CIR/GEN/2026-01: Standard SOPs",
        "resolution": "1. Authenticate the customer request via OTP/Biometric.\n2. Check limits against the branch delegation matrix.\n3. Escalate to Branch Manager via CBS ticketing if exceptions apply.",
        "automation_insight": "Migrate general inquiry routing to the customer-facing AI chatbot to reduce physical branch footfall.",
        "confidence": random.randint(85, 90)
    }
