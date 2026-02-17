import streamlit as st
import time

# -------------------------------------------------
# Page Setup
# -------------------------------------------------

st.set_page_config(
    page_title="AI Agent Susceptibility Assessment",
    layout="centered"
)

# -------------------------------------------------
# Styling
# -------------------------------------------------

st.markdown("""
<style>
.big-text {
    font-size: 1.15rem;
    color: #4B5563;
    line-height: 1.6;
}
.question-title {
    font-size: 1.6rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
}
.result-box {
    padding: 2rem;
    border-radius: 12px;
    background-color: #FFFFFF;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.05);
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Session State Initialization
# -------------------------------------------------

if "step" not in st.session_state:
    st.session_state.step = 1

if "risk_score" not in st.session_state:
    st.session_state.risk_score = 0

# -------------------------------------------------
# Header
# -------------------------------------------------

st.title("AI Agent Structural Susceptibility Assessment")
st.write("A guided structural exposure diagnostic for AI agents.")

total_steps = 5
progress = st.progress((st.session_state.step - 1) / total_steps)

# -------------------------------------------------
# Step Logic
# -------------------------------------------------

def next_step():
    st.session_state.step += 1

def restart():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.session_state.step = 1

# -------------------------------------------------
# Step 1 – Autonomy
# -------------------------------------------------

if st.session_state.step == 1:
    st.markdown('<div class="question-title">Autonomy Level</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="big-text">'
        "Degree to which the agent operates independently without human review. "
        "Higher autonomy increases systemic exposure."
        "</div>",
        unsafe_allow_html=True
    )

    st.session_state.autonomy = st.radio(
        "",
        ["Human-in-the-loop", "Semi-autonomous", "Fully autonomous"]
    )

    if st.button("Next"):
        next_step()

# -------------------------------------------------
# Step 2 – Tool Access
# -------------------------------------------------

elif st.session_state.step == 2:
    st.markdown('<div class="question-title">Tool Invocation Capability</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="big-text">'
        "Ability for the agent to execute APIs or system actions. "
        "Tool access materially increases operational risk."
        "</div>",
        unsafe_allow_html=True
    )

    st.session_state.tool_access = st.checkbox("Agent can call external APIs or tools")

    if st.button("Next"):
        next_step()

# -------------------------------------------------
# Step 3 – External Exposure
# -------------------------------------------------

elif st.session_state.step == 3:
    st.markdown('<div class="question-title">External Exposure</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="big-text">'
        "Whether the agent accepts public or untrusted input. "
        "This increases prompt injection and misuse risk."
        "</div>",
        unsafe_allow_html=True
    )

    st.session_state.public_input = st.checkbox("Agent accepts public or untrusted input")

    if st.button("Next"):
        next_step()

# -------------------------------------------------
# Step 4 – Data Sensitivity
# -------------------------------------------------

elif st.session_state.step == 4:
    st.markdown('<div class="question-title">Data Sensitivity Level</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="big-text">'
        "Nature of data processed. Higher sensitivity increases "
        "regulatory and reputational exposure."
        "</div>",
        unsafe_allow_html=True
    )

    st.session_state.data_sensitivity = st.radio(
        "",
        [
            "Low (non-sensitive)",
            "Moderate (internal business data)",
            "High (regulated / confidential)"
        ]
    )

    if st.button("Next"):
        next_step()

# -------------------------------------------------
# Step 5 – Decision Authority
# -------------------------------------------------

elif st.session_state.step == 5:
    st.markdown('<div class="question-title">Decision Criticality</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="big-text">'
        "Degree to which agent outputs influence or directly execute "
        "business actions."
        "</div>",
        unsafe_allow_html=True
    )

    st.session_state.decision_impact = st.radio(
        "",
        ["Advisory only", "Operational influence", "Automated execution"]
    )

    if st.button("Generate Assessment"):
        next_step()

# -------------------------------------------------
# Results
# -------------------------------------------------

elif st.session_state.step == 6:

    # Compute score
    score = 0

    autonomy = st.session_state.autonomy
    if autonomy == "Fully autonomous":
        score += 3
    elif autonomy == "Semi-autonomous":
        score += 2
    else:
        score += 1

    if st.session_state.tool_access:
        score += 3

    if st.session_state.public_input:
        score += 2

    data = st.session_state.data_sensitivity
    if data == "High (regulated / confidential)":
        score += 3
    elif data == "Moderate (internal business data)":
        score += 2
    else:
        score += 1

    impact = st.session_state.decision_impact
    if impact == "Automated execution":
        score += 3
    elif impact == "Operational influence":
        score += 2
    else:
        score += 1

    if score <= 6:
        exposure = "Low"
        color = "#2E7D32"
    elif score <= 11:
        exposure = "Moderate"
        color = "#F9A825"
    else:
        exposure = "High"
        color = "#C62828"

    # Animated reveal
    with st.spinner("Analyzing structural exposure..."):
        time.sleep(1.5)

    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.markdown(f"### Structural Exposure Level")
    st.markdown(f"<h1 style='color:{color}'>{exposure}</h1>", unsafe_allow_html=True)
    st.markdown(f"Composite Risk Score: **{score}**")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### Recommended Control Posture")

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

    st.button("Restart Assessment", on_click=restart)
