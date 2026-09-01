import random
import time
from pydantic import BaseModel

class OnboardingAssessment(BaseModel):
    applicant_id: str
    channel: str
    kyc_status: str
    fraud_risk_score: int
    processing_time: str
    legacy_sla: str
    stp_qualified: bool
    audit_trail: str

class FitGapItem(BaseModel):
    module: str
    legacy_cbs_state: str
    target_cloud_state: str
    fit_percentage: int
    gap_type: str
    remediation_strategy: str

def evaluate_digital_onboarding(channel: str, segment: str, deposit_amount: float) -> OnboardingAssessment:
    """Evaluates Straight-Through-Processing (STP) for digital CASA onboarding."""
    fraud_score = random.randint(92, 99) if segment != "High Risk" else random.randint(55, 78)
    stp = fraud_score >= 85 and deposit_amount <= 200000
    
    return OnboardingAssessment(
        applicant_id=f"APP-CNR-{random.randint(10000, 99999)}",
        channel=channel,
        kyc_status="VERIFIED (e-KYC Instant)" if stp else "MANUAL ESCALATION REQUIRED",
        fraud_risk_score=fraud_score,
        processing_time="4.2 minutes" if stp else "48 hours (Branch Hold)",
        legacy_sla="72.0 hours",
        stp_qualified=stp,
        audit_trail=f"Digital token generated via API Gateway. AML screening passed with confidence score {fraud_score}/100."
    )

def get_core_banking_fitgap_matrix():
    """Returns structured Fit-Gap assessment across core banking functional domains."""
    return [
        {
            "Domain": "CASA Deposit Engine",
            "Legacy CBS (As-Is)": "Overnight EOD batch calculation of interest; batch account ledger locks",
            "Target Architecture (To-Be)": "Real-time event streaming via Apache Kafka & Cloud Microservices",
            "Fit Score": "88%",
            "Gap Severity": "Medium",
            "Accenture Remediation": "Deploy Cloud API adapter layer to decouple EOD batch dependencies"
        },
        {
            "Domain": "KYC & Document Processing",
            "Legacy CBS (As-Is)": "Physical paper routing to branch hub; manual signature card scanning",
            "Target Architecture (To-Be)": "Automated OCR & biometric Aadhaar/PAN microservice verification",
            "Fit Score": "94%",
            "Gap Severity": "Low",
            "Accenture Remediation": "Standardized RESTful API integration into national UIDAI/NSDL pipelines"
        },
        {
            "Domain": "HNI Lending & Credit Approval",
            "Legacy CBS (As-Is)": "Static spreadsheet scoring with multi-desk physical file escalation",
            "Target Architecture (To-Be)": "Automated AI-driven decision engine with real-time bureau credit pulls",
            "Fit Score": "78%",
            "Gap Severity": "High",
            "Accenture Remediation": "Custom Business Rule Management System (BRMS) integration with CBS"
        },
        {
            "Domain": "Regulatory & Risk Reporting",
            "Legacy CBS (As-Is)": "T+3 manual data lake aggregation via SQL dumps and Excel consolidation",
            "Target Architecture (To-Be)": "Real-time multi-cloud data lakehouse telemetry with instant RBI compliance dashboards",
            "Fit Score": "82%",
            "Gap Severity": "Medium",
            "Accenture Remediation": "Implement Change Data Capture (CDC) pipeline directly into target cloud lake"
        },
        {
            "Domain": "Rural Financial Inclusion",
            "Legacy CBS (As-Is)": "Disconnected handheld POS terminals with periodic offline reconciliation sync",
            "Target Architecture (To-Be)": "Edge-optimized lightweight mobile banking microservice with offline sync tokens",
            "Fit Score": "90%",
            "Gap Severity": "Low",
            "Accenture Remediation": "Standardized private cloud container deployment for rural BC points"
        }
    ]

def calculate_transformation_roi(annual_volume: int, current_cost_per_acct: float, target_cost_per_acct: float):
    """Calculates quantitative financial & operational ROI for enterprise migration."""
    annual_savings = annual_volume * (current_cost_per_acct - target_cost_per_acct)
    sla_reduction_pct = 91.5
    error_reduction_pct = 84.0
    return {
        "annual_savings_inr": annual_savings,
        "sla_reduction_pct": sla_reduction_pct,
        "error_reduction_pct": error_reduction_pct,
        "payback_period_months": round((15000000 / max(annual_savings, 1)) * 12, 1)
    }
