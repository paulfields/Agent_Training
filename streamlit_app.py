import streamlit as st

st.set_page_config(page_title="AI Agent Susceptibility Demo", layout="wide")

st.title("AI Agent Susceptibility Assessment")
st.markdown("Structured evaluation of agent exposure based on configuration profile.")

st.divider()

# ------------------------
# Configuration Inputs
# ------------------------

st.header("1. Agent Configuration")

col1, col2 = st.columns(2)

with col1:
    autonomy = st.selectbox(
        "Autonomy Level",
        ["Human-in-the-loop", "Semi-autonomous", "Fully autonomous"]
    )

    tool_access = st.checkbox("Agent can call external APIs or tools")

    public_input = st.checkbox("Agent accepts public or untrusted input")

with col2:
    data_sensitivity = st.selectbox(
        "Data Sensitivity Level",
        ["Low (non-sensitive)", "Moderate (internal business data)", "High (regulated / confidential)"]
    )

    decision_impact = st.selectbox(
        "Decision Criticality",
        ["Advisory only", "Operational influence", "Automated execution"]
    )

st.divider()

# ------------------------
# Scoring Logic
# ------------------------

risk_score = 0

# Autonomy
if autonomy == "Fully autonomous":
    risk_score += 3
elif autonomy == "Semi-autonomous":
    risk_score += 2
else:
    risk_score += 1

# Tool Access
if tool_access:
    risk_score += 3

# Public Input
if public_input:
    risk_score += 2

# Data Sensitivity
if data_sensitivity == "High (regulated / confidential)":
    risk_score += 3
elif data_sensitivity == "Moderate (internal business data)":
    risk_score += 2
else:
    risk_score += 1

# Decision Impact
if decision_impact == "Automated execution":
    risk_score += 3
elif decision_impact == "Operational influence":
    risk_score += 2
else:
    risk_score += 1

# ------------------------
# Risk Categorization
# ------------------------

if risk_score <= 6:
    exposure = "Low"
elif risk_score <= 11:
    exposure = "Moderate"
else:
    exposure = "High"

st.header("2. Susceptibility Assessment")

st.metric("Structural Exposure Level", exposure)
st.metric("Composite Risk Score", risk_score)

st.divider()

# ------------------------
# Control Recommendations
# ------------------------

st.header("3. Required Control Posture")

if exposure == "Low":
    st.success("""
    **Baseline Controls Recommended**
    - Prompt version control
    - Logging and traceability
    - Basic input validation
    """)

elif exposure == "Moderate":
    st.warning("""
    **Enhanced Controls Required**
    - Guardrail layer (content filtering / policy engine)


