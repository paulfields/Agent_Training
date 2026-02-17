import streamlit as st
import time

# -------------------------------------------------
# Page Setup
# -------------------------------------------------
st.set_page_config(
    page_title="AI Agent Susceptibility Assessment",
    layout="centered",
)

# -------------------------------------------------
# Styling (light, clean; no harsh dividers)
# -------------------------------------------------
st.markdown("""
<style>
/* Slightly wider centered container */
.block-container {max-width: 860px; padding-top: 2.2rem;}

/* Make helper/descriptive text larger and easier to read */
.big-desc {
    font-size: 1.05rem;
    line-height: 1.55;
    color: #374151; /* gray-700 */
    margin-top: 0.25rem;
    margin-bottom: 1.0rem;
}

/* Card-like panels */
.card {
    padding: 1.25rem 1.25rem 1.1rem 1.25rem;
    border-radius: 14px;
    background: #FFFFFF;
    border: 1px solid #E5E7EB; /* gray-200 */
    box-shadow: 0 8px 24px rgba(17,24,39,0.05);
    margin-bottom: 1rem;
}

/* Subtle label */
.kicker {
    font-size: 0.85rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #6B7280; /* gray-500 */
    margin-bottom: 0.35rem;
}

/* Big exposure text */
.exposure {
    font-size: 2.4rem;
    font-weight: 800;
    margin: 0.25rem 0 0.25rem 0;
}

/* Small muted text */
.muted { color: #6B7280; font-size: 0.95rem; }

/* Button row spacing */
button[kind="primary"], button[kind="secondary"] { border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# State Initialization
# -------------------------------------------------
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

# Ensure defaults exist (prevents missing attr errors if user refreshes mid-flow)
st.session_state.setdefault("autonomy", "Human-in-the-loop")
st.session_state.setdefault("tool_access", False)
st.session_state.setdefault("public_input", False)
st.session_state.setdefault("data_sensitivity", "Low (non-sensitive)")
st.session_state.setdefault("decision_impact", "Advisory only")

# -------------------------------------------------
# Header
# -------------------------------------------------
st.title("AI Agent Structural Susceptibility Assessment")
st.write("A guided structural exposure diagnostic for AI agents.")

st.progress((st.session_state.step - 1) / total_steps)

# -------------------------------------------------
# Helper: common layout for each step
# -------------------------------------------------
def step_shell(step_title: str, desc: str):
    st.markdown(f"""
    <div class="card">
      <div class="kicker">Step {st.session_state.step} of {total_steps}</div>
      <h2 style="margin-top:0.25rem;">{step_title}</h2>
      <div class="big-desc">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

def nav_row(next_label="Continue", show_back=True, next_is_primary=True):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if show_back:
            if st.button("Back", use_container_width=True):
                prev_step()
    with col3:
        if next_is_primary:
            if st.button(next_label, type="primary", use_container_width=True):
                next_step()
        else:
            if st.button(next_label, use_container_width=True):
                next_step()

# -------------------------------------------------
# STEP 1 – Autonomy
# -------------------------------------------------
if st.session_state.step == 1:
    step_shell(
        "Autonomy Level",
        "Degree to which the agent operates independently without human review. "
        "Higher autonomy increases systemic exposure."
    )

    st.session_state.autonomy = st.radio(
        "Select an autonomy level",
        ["Human-in-the-loop", "Semi-autonomous", "Fully autonomous"],
        index=["Human-in-the-loop", "Semi-autonomous", "Fully autonomous"].index(st.session_state.autonomy),
        label_visibility="collapsed",
    )

    nav_row(show_back=False)

# -------------------------------------------------
# STEP 2 – Tool Access
# -------------------------------------------------
elif st.session_state.step == 2:
    step_shell(
        "Tool Invocation Capability",
        "Ability for the agent to execute external tools, APIs, or system actions. "
        "Tool access materially increases operational risk because the agent can affect real systems."
    )

    st.session_state.tool_access = st.checkbox(
        "Agent can call external APIs or tools",
        value=st.session_state.tool_access
    )

    nav_row()

# -------------------------------------------------
# STEP 3 – External Exposure
# -------------------------------------------------
elif st.session_state.step == 3:
    step_shell(
        "External Exposure",
        "Whether the agent accepts untrusted or public-facing input. "
        "External exposure increases prompt injection risk, manipulation risk, and abuse potential."
    )

    st.session_state.public_input = st.checkbox(
        "Agent accepts public or untrusted input",
        value=st.session_state.public_input
    )

    nav_row()

# -------------------------------------------------
# STEP 4 – Data Sensitivity
# -------------------------------------------------
elif st.session_state.step == 4:
    step_shell(
        "Data Sensitivity Level",
        "Nature of the data the agent processes. Higher sensitivity increases regulatory, privacy, and reputational exposure "
        "and raises the bar for monitoring, auditing, and access controls."
    )

    options = [
        "Low (non-sensitive)",
        "Moderate (internal business data)",
        "High (regulated / confidential)"
    ]
    st.session_state.data_sensitivity = st.radio(
        "Select the sensitivity of data the agent touches",
        options,
        index=options.index(st.session_state.data_sensitivity),
        label_visibility="collapsed",
    )

    nav_row()

# -------------------------------------------------
# STEP 5 – Decision Authority
# -------------------------------------------------
elif st.session_state.step == 5:
    step_shell(
        "Decision Criticality",
        "Degree to which the agent’s outputs influence or directly execute business actions. "
        "Execution authority significantly increases risk because errors propagate immediately into operations."
    )

    opts = ["Advisory only", "Operational influence", "Automated execution"]
    st.session_state.decision_impact = st.radio(
        "Select the level of decision authority",
        opts,
        index=opts.index(st.session_state.decision_impact),
        label_visibility="collapsed",
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("Back", use_container_width=True):
            prev_step()
    with col3:
        if st.button("Generate Assessment", type="primary", use_container_width=True):
            next_step()

# -------------------------------------------------
# RESULTS
# -------------------------------------------------
elif st.session_state.step == 6:

    # ---- Score
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

    ds = st.session_state.data_sensitivity
    if ds == "High (regulated / confidential)":
        score += 3
    elif ds == "Moderate (internal business data)":
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

    # ---- Banding
    if score <= 6:
        exposure = "Low"
        color = "#166534"  # green-800
        meaning = (
            "The agent’s structure suggests limited systemic risk. The primary focus should be on baseline hygiene: "
            "traceability, guardrails on inputs/outputs, and clear accountability for how recommendations are used."
        )
        controls = [
            "Prompt and configuration version control",
            "Logging, traceability, and basic monitoring",
            "Structured output validation for critical fields",
            "Basic input validation and safe defaults",
        ]
        next_moves = [
            "Add lightweight policy checks (e.g., restricted topics, PII redaction triggers).",
            "Introduce an assessment record (who ran it, when, for what use case).",
        ]
    elif score <= 11:
        exposure = "Moderate"
        color = "#A16207"  # amber-700
        meaning = (
            "The agent’s structure creates meaningful exposure. The control posture should shift from “hygiene” to "
            "“managed operation”: guardrails, approval gates for higher-impact actions, and tighter tool/data boundaries."
        )
        controls = [
            "Guardrail layer (policy + safety checks before responses/actions)",
            "Human approval for defined high-impact scenarios",
            "Tool invocation constraints (allow-list, scope limits, timeouts)",
            "Output validation + safe fallback behaviors",
            "Audit logging for prompts, tool calls, and decisions",
        ]
        next_moves = [
            "Add a control-gap checklist and compute residual risk after mitigations.",
            "Add role-based access (viewer vs. admin) for governance ownership.",
        ]
    else:
        exposure = "High"
        color = "#9F1239"  # rose-800
        meaning = (
            "The agent’s structure is high-exposure. This configuration should be treated like a production system with "
            "material operational and reputational risk. Strong human oversight, strict tool boundaries, and rigorous auditing "
            "are required before deployment."
        )
        controls = [
            "Policy enforcement gateway before any tool call or external action",
            "Strong human-in-the-loop oversight for impactful outcomes",
            "Tool sandboxing (scoped credentials, constrained permissions, allow-lists)",
            "Rigorous output validation + rollback/containment plan",
            "Comprehensive audit logging and monitoring with alerting",
            "Red-team / adversarial testing for prompt injection + misuse cases",
        ]
        next_moves = [
            "Add a formal ‘Go / Conditional / No-Go’ recommendation with rationale.",
            "Create an escalation workflow (exceptions, risk acceptance, sign-off).",
        ]

    # ---- Reveal
    with st.spinner("Analyzing structural exposure..."):
        time.sleep(0.8)

    st.markdown(f"""
    <div class="card">
      <div class="kicker">Results</div>
      <div class="muted">Structural Exposure Level</div>
      <div class="exposure" style="color:{color};">{exposure}</div>
      <div class="big-desc"><b>What this means:</b> {meaning}</div>
      <div class="muted">Composite Risk Score: <b>{score}</b></div>
    </div>
    """, unsafe_allow_html=True)

    # ---- Summary of selections
    st.markdown("""
    <div class="card">
      <div class="kicker">Summary</div>
    </div>
    """, unsafe_allow_html=True)

    st.write(
        f"**Autonomy:** {st.session_state.autonomy}\n\n"
        f"**Tool Invocation:** {'Enabled' if st.session_state.tool_access else 'Not enabled'}\n\n"
        f"**External Exposure:** {'Accepts untrusted/public input' if st.session_state.public_input else 'No public/untrusted input'}\n\n"
        f"**Data Sensitivity:** {st.session_state.data_sensitivity}\n\n"
        f"**Decision Criticality:** {st.session_state.decision_impact}\n"
    )

    # ---- Controls
    st.markdown("""
    <div class="card">
      <div class="kicker">Recommended Control Posture</div>
    </div>
    """, unsafe_allow_html=True)
    for c in controls:
        st.write(f"- {c}")

    # ---- Next moves
    st.markdown("""
    <div class="card">
      <div class="kicker">Where we can take this next</div>
    </div>
    """, unsafe_allow_html=True)
    for n in next_moves:
        st.write(f"- {n}")

    # ---- Actions
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Back", use_container_width=True):
            st.session_state.step = 5
            st.rerun()
    with col2:
        st.button("Restart Assessment", type="primary", on_click=restart, use_container_width=True)

