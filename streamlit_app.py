import streamlit as st

st.set_page_config(
    page_title="AI Agent Susceptibility Assessment",
    layout="centered"
)

# ----------------------------
# Typography Styling Only
# ----------------------------

st.markdown("""
<style>
.helper {
    font-size: 1.05rem;
    color: #4B5563;
    margin-bottom: 1rem;
    line-height: 1.5;
}
.section-spacing {
    margin-top: 2.5rem;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Title
# ----------------------------

st.title("AI Agent Structural Susceptibility Assessment")

st.write(
    "This model evaluates structural exposure based on configuration choices. "
    "It is intentionally simplified to support structured team discussion."
)

# ----------------------------
# Section 1 – Configuration
# ----------------------------

st.markdown('<div class="section-spacing"></div>', unsafe_allow_html=True)
st.header("1. Agent Configuration")

st.subheader("Autonomy Level")
st.markdown(
    '<div class="helper">'
    "Degree to which the agent operates independently without human review. "
    "Higher autonomy increases systemic exposure."
    "</div>",
    unsafe_allow_html=True
)
autonomy = st.selectbox(
    "",
    ["Human-in-the-loop", "Semi-autonomous", "Fully autonomous"]
)

st.subheader("Tool Invocation Capability")
st.markdown(
    '<div class="helper">'
    "Ability for the agent to execute APIs or system actions. "
    "Tool access materially increases operational risk."
    "</div>",
    unsafe_allow_html=True
)
tool_access = st.checkbox("Agent can call external APIs or tools")

st.subheader("External Exposure")
st.markdown(
    '<div class="helper">'
    "Whether the agent accepts public or untrusted input. "
    "This increases prompt injection and misuse risk."
    "</div>",
    unsafe_allow_html=True
)
public_input = st.checkbox("Agent accepts public or untrusted input")

st.subheader("Data Sensitivity Level")
st.markdown(
    '<div class="helper">'
    "Nature of data processed. Higher sensitivity increases "
    "regulatory and reputational exposure."
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

st.subheader("Decision Criticality")
st.markdown(
    '<div class="helper">'
    "Degree to which agent outputs influence or directly execute "
    "business actions."
    "</div>",
    unsafe_allow_html=True
)
decision_impact = st.selectbox(
    "",
    ["Advisory only", "Operational influence", "Automated execution"]
)

# ----------------------------
# Scoring Logic
# ----------------------------

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

# ----------------------------
# Section 2 – Assessment
# ----------------------------

st.markdown('<div class="section-spacing"></div>', unsafe_allow_html=True)
st.header("2. Structural Exposure Assessment")

st.markdown(f"### Exposure Level: {exposure}")
st.markdown(f"Composite Risk Score: {risk_score}")

# ----------------------------
# Section 3 – Controls
# ----------------------------

st.markdown('<div class="section-spacing"></div>', unsafe_allow_html=True)
st.header("3. Required Control Posture")

if exposure == "Low":
    st.write(
        "- Prompt version control\n"
        "- Logging and traceability\n"
        "- Basic input validation"
    )
elif exposure == "Moderate":
    st.write(
        "- Guardrail layer (policy enforcement)\n"
        "- Human approval for high-impact outputs\n"
        "- Tool invocation restrictions\n"
        "- Structured output validation"
    )
else:
    st.write(
        "- Policy enforcement gateway\n"
        "- Strong human oversight\n"
        "- Tool sandboxing constraints\n"
        "- Output validation framework\n"
        "- Audit and rollback capability"
    )

st.markdown('<div class="section-spacing"></div>', unsafe_allow_html=True)
st.caption("Illustrative model – weighting assumptions are transparent for refinement.")
