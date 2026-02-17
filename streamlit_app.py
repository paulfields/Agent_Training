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

def restart():
    st.session_state.clear()
    st.session_state.step = 1

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

    with st.form("step1"):
        st.header("Autonomy Level")
        st.write(
            "Degree to which the agent operates independently without human review. "
            "Higher autonomy increases systemic exposure."
        )

        autonomy = st.radio(
            "",
            ["Human-in-the-loop", "Semi-autonomous", "Fully autonomous"]
        )

        submitted = st.form_submit_button("Continue")

        if submitted:
            st.session_state.autonomy = autonomy
            st.session_state.step = 2

# ---------------------------
# STEP 2 – Tool Access
# ---------------------------

elif st.session_state.step == 2:

    with st.form("step2"):
        st.header("Tool Invocation Capability")
        st.write(
            "Ability for the agent to execute APIs or system actions. "
            "Tool access materially increases operational risk."
        )

        tool_access = st.checkbox(
            "Agent can call external APIs or tools"
        )

        col1, col2 = st.columns(2)
        back = col1.form_submit_button("Back")
        submitted = col2.form_submit_button("Continue")

        if back:
            st.session_state.step = 1

        if submitted:
            st.session_state.tool_access = tool_access
            st.session_state.step = 3

# ---------------------------
# STEP 3 – External Exposure
# ---------------------------

elif st.session_state.step == 3:

    with st.form("step3"):
        st.header("External Exposure")
        st.write(
            "Whether the agent accepts public or untrusted input. "
            "This increases prompt injection and misuse risk."
        )

        public_input = st.checkbox(
            "Agent accepts public or untrusted input"
        )

        col1, col2 = st.columns(2)
        back = col1.form_submit_button("Back")
        submitted = col2.form_submit_button("Continue")

        if back:
            st.session_state.step = 2

        if submitted:
            st.session_state.public_input = public_input
            st.session_state.step = 4

# ---------------------------
# STEP 4 – Data Sensitivity
# ---------------------------

elif st.session_state.step == 4:

    with st.form("step4"):
        st.header("Data Sensitivity Level")
        st.write(
            "Nature of data processed. Higher sensitivity increases "
            "regulatory and reputational exposure."
        )

        data_sensitivity = st.radio(
            "",
            [
                "Low (non-sensitive)",
                "Moderate (internal business data)",
                "High (regulated / confidential)"
            ]
        )

        col1, col2 = st.columns(2)
        back = col1.form_submit_button("Back")
        submitted = col2.form_submit_button("Continue")

        if back:
            st.session_state.step = 3

        if submitted:
            st.session_state.data_sensitivity = data_sensitivity
            st.session_state.step = 5

# ---------------------------
# STEP 5 – Decision Authority
# ---------------------------

elif st.session_state.step == 5:

    with st.form("step5"):
        st.header("Decision Criticality")
        st.write(
            "Degree to which agent outputs influence or directly execute "
            "business actions."
        )

        decision_impact = st.radio(
            "",
            ["Advisory only", "Operational influence", "Automated execution"]
        )

        col1, col2 = st.columns(2)
        back = col1.form_submit_button("Back")
        submitted = col2.form_submit_button("Generate Assessment")

        if back:
            st.session_state.step = 4

        if submitted:
            st.session_state.decision_impact = decision_impact
            st.session_state.step = 6

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

    if st.session_state.get("tool_access"):
        score += 3

    if st.session_state.get("public_input"):
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
