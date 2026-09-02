import random

def process_circular_query(query_type: str, query: str) -> dict:
    """
    Simulates a GenAI RAG engine retrieving and synthesizing Master Circulars, 
    SOPs, and Scheme Guidelines for branch operations.
    """
    text = query.lower()
    
    if query_type == "Documentation & KYC":
        category = "Retail & NRI Onboarding"
        circular = "Master Circular CIR/KYC/2026-14: Non-Resident & Trust Accounts"
        resolution = (
            "Required Documentation for NRI (NRE/NRO) Setup:\n"
            "1. Valid Passport and Overseas Resident Visa (or OCI card).\n"
            "2. FATCA/CRS declaration signed by the applicant.\n"
            "3. Overseas address proof (Utility bill or bank statement, attested by embassy or notary).\n"
            "4. PAN Card or Form 60."
        )
        to_be_recommendation = "Current As-Is process relies on physical attestation. Proposed To-Be architecture: Integrate digital Video-KYC (V-KYC) with automated OCR passport extraction to eliminate physical document routing."
        
    elif query_type == "Scheme Updates & Facilities":
        category = "Government Schemes & Term Deposits"
        circular = "CIR/GOVT/2026-42: Revised Guidelines for Senior Citizen Savings Scheme (SCSS)"
        resolution = (
            "Latest Updates to SCSS:\n"
            "1. Maximum investment limit has been enhanced from ₹15 Lakh to ₹30 Lakh.\n"
            "2. Spouses can now open joint accounts with the entire amount attributed to the primary senior citizen.\n"
            "3. Premature withdrawal penalty reduced to 1% if closed after 2 years."
        )
        to_be_recommendation = "Currently, tellers must manually identify eligible customers. Proposed To-Be architecture: Implement an automated trigger in Customer 360 that pushes SMS notifications to customers turning 60, offering instant SCSS conversion via mobile banking."
        
    else:
        category = "Exceptions & Error Handling"
        circular = "CIR/RBIA/2026-09: DBT Mandate Mapping & Exceptions"
        resolution = (
            "Resolution for NPCI/Aadhaar Mapping Failure:\n"
            "1. Verify customer's Aadhaar seeding status on the centralized NPCI mapper.\n"
            "2. If 'Inactive', capture biometric consent via the branch micro-ATM.\n"
            "3. Push the E-mandate update XML file to the clearing house (T+1 resolution)."
        )
        to_be_recommendation = "Recommend integrating a real-time NPCI status-check API directly into the front-end tablet to pre-validate mappings before initiating scheme enrollment."

    return {
        "category": category,
        "circular_ref": circular,
        "resolution": resolution,
        "automation_insight": to_be_recommendation,
        "confidence": random.randint(94, 99)
    }
