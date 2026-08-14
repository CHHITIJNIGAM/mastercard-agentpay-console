import os
import json
import random
import time
from groq import Groq
from pydantic import BaseModel

class AgentTransactionResult(BaseModel):
    user_query: str
    selected_item: dict
    kya_status: str
    kya_trust_score: int
    spending_limit: float
    is_approved: bool
    rejection_reason: str = ""
    token_id: str = ""
    cryptogram: str = ""
    settlement_id: str = ""
    timestamp: str = ""
    agent_reasoning: str = ""

def run_agentic_workflow_with_llm(
    user_intent: str, 
    max_budget: float = 100.0, 
    agent_id: str = "AGT-MC-2026-X8", 
    groq_api_key: str = None
) -> AgentTransactionResult:
    """
    Executes live AI Agent reasoning via Groq LLM:
    1. Agent dynamically analyzes user intent and finds/recommends an optimal product.
    2. Enforces strict JSON structured outputs.
    3. Passes result through Mastercard KYA & Tokenization Guardrails.
    """
    
    # Fallback/Default system prompt if no API key is provided
    if not groq_api_key:
        api_key = os.environ.get("GROQ_API_KEY", "")
    else:
        api_key = groq_api_key

    # If no key is set, return a helpful notice
    if not api_key:
        return AgentTransactionResult(
            user_query=user_intent,
            selected_item={"id": "ERR-001", "name": "Groq API Key Missing", "price": 0.0},
            kya_status="FLAGGED",
            kya_trust_score=0,
            spending_limit=max_budget,
            is_approved=False,
            rejection_reason="Please enter your Groq API Key in the sidebar to activate live LLM reasoning.",
            timestamp=time.strftime("%Y-%m-%d %H:%M:%S UTC"),
            agent_reasoning="API Key not provided."
        )

    # 1. Initialize Groq Client
    client = Groq(api_key=api_key)

    system_prompt = """
    You are an autonomous Agentic Commerce Shopping Agent acting on behalf of a human principal.
    Your goal is to parse the user's intent, reason over merchant options, and select the single most appropriate item with realistic merchant pricing.

    You must respond ONLY with a strict JSON object with this exact structure:
    {
        "item_name": "Full descriptive name of the selected product",
        "price": 45.50,
        "category": "Product category",
        "reasoning": "Brief explanation (1-2 sentences) of why this exact item was chosen based on user requirements"
    }
    Do not include markdown codeblocks or conversational filler. Return only valid JSON.
    """

    try:
        # 2. Call the LLM (Llama 3.3 70B via Groq)
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"User Purchasing Intent: '{user_intent}'. Delegated User Spend Limit: ${max_budget:.2f}."}
            ],
            temperature=0.2,
            response_format={"type": "json_object"}
        )

        response_content = completion.choices[0].message.content
        parsed = json.loads(response_content)

        item_name = parsed.get("item_name", "Autonomous Purchase Item")
        price = float(parsed.get("price", 50.0))
        agent_reasoning = parsed.get("reasoning", "Item matched against intent criteria.")

        selected_item = {
            "id": f"MERCH-LLM-{random.randint(100, 999)}",
            "name": item_name,
            "price": price
        }

    except Exception as e:
        # Fallback if API fails
        selected_item = {
            "id": "ERR-LLM",
            "name": f"Item for: {user_intent[:30]}...",
            "price": round(random.uniform(25.0, max_budget * 1.1), 2)
        }
        agent_reasoning = f"LLM parsing fallback triggered: {str(e)}"

    # 3. KYA Policy & Spending Guardrail Check
    trust_score = random.randint(94, 99)
    approved = selected_item["price"] <= max_budget
    reason = "" if approved else f"Transaction rejected: LLM-selected item price (${selected_item['price']:.2f}) exceeds delegated spending limit (${max_budget:.2f})."

    # 4. Mastercard Tokenization & Cryptogram Generation
    token_id = f"TKN-MC-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}" if approved else ""
    cryptogram = f"CRYPTO-SHA256-{random.randint(100000, 999999)}" if approved else ""
    settlement_id = f"SETTLE-AUTH-{random.randint(1000000, 9999999)}" if approved else ""

    return AgentTransactionResult(
        user_query=user_intent,
        selected_item=selected_item,
        kya_status="KYA-VERIFIED (Level 3 Delegate)" if approved else "FLAGGED",
        kya_trust_score=trust_score,
        spending_limit=max_budget,
        is_approved=approved,
        rejection_reason=reason,
        token_id=token_id,
        cryptogram=cryptogram,
        settlement_id=settlement_id,
        timestamp=time.strftime("%Y-%m-%d %H:%M:%S UTC"),
        agent_reasoning=agent_reasoning
    )