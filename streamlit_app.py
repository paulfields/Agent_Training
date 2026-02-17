import streamlit as st

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="AI Agent Susceptibility Assessment",
    layout="wide"
)

# -------------------------------------------------
# Custom Styling (Professional Tone)
# -------------------------------------------------

st.markdown("""
<style>
body {
    background-color: #F5F7FA;
}
.main {
    background-color: #F5F7FA;
}
.section-card {
    background-color: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
    margin-bottom: 2rem;
}
.section-title {
    font-size: 1.4rem;
    font-weight: 600;
    margin-bottom: 1rem;
}
.helper-text {
    color: #5f6b7a;
    font-size: 0.9rem;
    margin-bottom: 0.75rem;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Header
# -------------------------------------------------

st.markdown("## AI Agent Structural Susceptibility Assessment")
st.markdown(
    "This demo models structural exposure based on agent configuration choices. "
    "It is intentionally simplified to stimulate structured team discussion."
)

st.markdown("---")

# -------------------------------------------------
# Configuration Section
# -------------------------------------------------

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">1. Agent Configuration</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    st.markdown("**Autonomy Level**")
    st.markdown(
        '<div class="helper-text">'
        "Degree to which the agent acts independently without human review. "
        "Higher autonomy increases systemic exposure."
        "</div>",
        unsafe_allow_html=True
    )

    autonomy = st.selectbox(
        "",
        ["Human-in-the-loop", "Semi-autonomous", "Fully autonomous"]
    )

    st.markdown("**Tool Invocation Capability**")
    st.markdown(
        '<div class="helper-text">'
        "Ability for the agent to execute external tools, APIs, or system actions. "
        "Tool access materially increases operational risk."
        "</div>",
        unsafe_allow_html=True
    )

    tool_access = st.checkbox("Agent can call external APIs or tools")

    st.markdown("**External Exposure**")
    st.markdown(
        '<div class="helper-text">'
        "Whether the agent accepts untrusted or public-facing input. "
        "External exposure increases prompt injection and misuse risk."
        "</div>",
        unsafe_allow_html=True
    )

    public_input = st.checkbox("Agent accepts public or untrusted input")

with col2:

    st.markdown("**Data Sensitivity Level**")
    st.markdown(
        '<div class="helper-text">'
        "Nature of data the agent processes. "
        "Higher sensitivity increases regulatory and reputational exposure."
        "</div>",
        unsafe_allow_html=True
    )

    data_sensitivity = st.selectbox(
        "",
        [
            "Low (non-sensitive)",
            "Moderate (internal business data)",
            "High (regulated / confidential)"
        ]
    )

    st.markdown("**Decision Criticality**")
    st.markdown(
        '<div class="helper-text">'
        "Degree to which agent outputs influence or execute business actions. "
        "Execution authority significantly increases risk exposure."
        "</div>",
        unsafe_allow_html=True
    )

    decision_impact = st.selectbox(
        "",
        ["Advisory only", "Operational influence", "Automated execution"]
    )

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# Scoring Logic
# -------------------------------------------------

risk_score = 0

if autonomy == "Fully autonomous":
    risk_score += 3
elif autonomy == "Semi-autonomous":
    risk_score += 2
else:
    risk_score += 1

if tool_access:
    risk_score += 3

if public_input:
    risk_score += 2

if data_sensitivity == "High (regulated / confidential)":
    risk_score += 3
elif data_sensitivity == "Moderate (internal business data)":
    risk_score += 2
else:
    risk_score += 1

if decision_impact == "Automated execution":
    risk_score += 3
elif decision_impact == "Operational influence":
    risk_score += 2
else:
    risk_score += 1

if risk_score <= 6:
    exposure = "Low"
elif risk_score <= 11:
    exposure = "Moderate"
else:
    exposure = "High"

# -------------------------------------------------
# Results Section
# -------------------------------------------------

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">2. Structural Exposure Assessment</div>', unsafe_allow_html=True)

colA, colB = st.columns(2)

with colA:
    st.metric("Exposure Level", exposure)

with colB:
    st.metric("Composite Risk Score", risk_score)

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# Control Posture Section
# -------------------------------------------------

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">3. Required Control Posture</div>', unsafe_allow_html=True)

if exposure == "Low":
    st.success(
        "Baseline Controls Recommended:\n\n"
        "- Prompt version control\n"
        "- Logging and traceability\n"
        "- Basic input validation\n"
    )

elif exposure == "Moderate":
    st.warning(
        "Enhanced Controls Required:\n\n"
        "- Guardrail layer (policy enforcement)\n"
        "- Human approval for high-impact outputs\n"
        "- Tool invocation restrictions\n"
        "- Structured output validation\n"
    )

else:
    st.error(
        "High-Risk Configuration:\n\n"
        "Deployment should not proceed without:\n"
        "- Policy enforcement gateway\n"
        "- Strong human oversight\n"
        "- Tool sandboxing constraints\n"
        "- Output validation framework\n"
        "- Audit and rollback capability\n"
    )

st.markdown('</div>', unsafe_allow_html=True)

st.caption(
    "This model is illustrative. Weighting assumptions are intentionally transparent to enable refinement."
)
