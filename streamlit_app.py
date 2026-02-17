import streamlit as st
import time

st.set_page_config(
    page_title="AI Agent Susceptibility Assessment",
    layout="centered"
)

# ---------------------------
# State Initialization
# ---------------------------

if "step" not in st.session_state:
    st.session_state.step = 1

total_steps = 5

def next_step():
    st.session_state.step += 1
    st.rerun()

def prev_step():
    st.session_state.step -= 1
    st.rerun()

def restart():
    st.session_state.clear()
    st.session_state.step = 1
    st.rerun()

# ---------------------------
# Header
# ---------------------------

st.title("AI Agent Structural Susceptibility Assessment")
st.write("A guided structural exposure diagnostic for AI agents.")

st.progress((st.session_state.step - 1) / total_steps)

# ---------------------------
# STEP 1 – Autonomy
# ---------------------------

if st.session_state.step == 1:

    st.header("Autonomy Level")
    st.write(
        "Degree to which the agent operates independently without human review. "
        "Higher autonomy increases systemic exposure."
    )

    st.session_state.autonomy = st.radio(
        "",
        ["Human-in-the-loop", "Semi-autonomous", "Fully autonomous"]
    )

    if st.button("Continue"):
        next_step()

# ---------------------------
# STEP 2 – Tool Access
# ---------------------------

elif st.session_state.step == 2:

    st.header("Tool Invocation Capability")
    st.write(
        "Ability for the agent to execute APIs or system actions. "
        "Tool access materially increases operational risk."
    )

    st.session_state.tool_access = st.checkbox(
        "Agent can call external APIs or tools"
    )

    col1, col2 = st.columns(2)

    if col1.button("Back"):
        prev_step()

    if col2.button("Continue"):
        next_step()

# ---------------------------
# STEP 3 – External Exposure
# ---------------------------

elif st.session_state.step == 3:

    st.header("External Exposure")
    st.write(
        "Whether the agent accepts public or untrusted input. "
        "This increases prompt injection and misuse risk."
    )

    st.session_state.public_input = st.checkbox(
        "Agent accepts public or untrusted input"
    )

    col1, col2 = st.columns(2)

    if col1.button("Back"):
        prev_step()

    if col2.button("Continue"):
        next_step()

# ---------------------------
# STEP 4 – Data Sensitivity
# ---------------------------

elif st.session_state.step == 4:

    st.header("Data Sensitivity Level")
    st.write(
        "Nature of data processed. Higher sensitivity increases "
        "regulatory and reputational exposure."
    )

    st.session_state.data_sensitivity = st.radio(
        "",
        [
            "Low (non-sensitive)",
            "Moderate (internal business data)",
            "High (regulated / confidential)"
        ]
    )

    col1, col2 = st.columns(2)

    if col1.button("Back"):
        prev_step()

    if col2.button("Continue"):
        next_step()

# ---------------------------
# STEP 5 – Decision Authority
# ---------------------------

elif st.session_state.step == 5:

    st.header("Decision Criticality")
    st.write(
        "Degree to which agent outputs influence or directly execute "
        "business actions."
    )

    st.session_state.decision_impact = st.radio(
        "",
        ["Advisory only", "Operational influence", "Automated execution"]
    )

    col1, col2 = st.columns(2)

    if col1.button("Back"):
        prev_step()

    if col2.button("Generate Assessment"):
        next_step()

# ---------------------------
# RESULTS
# ---------------------------

elif st.session_state.step == 6:

    score = 0

    if st.session_state.autonomy == "Fully autonomous":
        score += 3
    elif st.session_state.autonomy == "Semi-autonomous":
        score += 2
    else:
        score += 1

    if st.session_state.tool_access:
        score += 3

    if st.session_state.public_input:
        score += 2

    if st.session_state.data_sensitivity == "High (regulated / confidential)":
        score += 3
    elif st.session_state.data_sensitivity == "Moderate (internal business data)":
        score += 2
    else:
        score += 1

    if st.session_state.decision_impact == "Automated execution":
        score += 3
    elif st.session_state.decision_impact == "Operational influence":
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

    with st.spinner("Analyzing structural exposure..."):
        time.sleep(1)

    st.header("Structural Exposure Level")
    st.markdown(f"<h1 style='color:{color}'>{exposure}</h1>", unsafe_allow_html=True)
    st.write(f"Composite Risk Score: **{score}**")

    st.button("Restart Assessment", on_click=restart)
