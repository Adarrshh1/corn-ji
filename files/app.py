"""
CornScan AI  ·  v7.0 APEX Edition
══════════════════════════════════════════════════════
app.py — PAGE ROUTER (brain)

  This file only controls which page to show.
  All UI logic lives in ui/ and utils/.

  PAGE FLOW:
    loading  →  2.2s cinematic splash  →  landing
    landing  →  "Let's Go" CTA         →  main
    main     →  full premium dashboard

  TO ADD A NEW PAGE:
    1. Create  ui/my_page.py  with a show_my_page() function
    2. Add a new session_state default below
    3. Add an elif branch in the router at the bottom
"""

import streamlit as st

# ── Page config (must be first Streamlit call) ────────────────────
st.set_page_config(
    page_title="CornScan AI",
    page_icon="🌽",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Remove ALL Streamlit padding and gaps ─────────────────────────
st.markdown("""
<style>
/* Remove top space */
.block-container {
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
}

/* Remove extra margin */
.css-18e3th9 {
    padding-top: 0rem !important;
}

/* Full height layout */
html, body, .main {
    height: 100%;
    overflow: hidden;
}

/* Remove blank space above */
header {visibility: hidden;}
footer {visibility: hidden;}

/* Keep sidebar always visible */
[data-testid="stSidebar"] {
    display: block !important;
    visibility: visible !important;
}

[data-testid="stSidebar"][aria-expanded="false"] {
    margin-left: 0px !important;
}

/* Sidebar toggle button */
button[kind="header"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# ── Session state defaults ────────────────────────────────────────
for key, default in [
    ("page",         "loading"),
    ("user_mode",    "farmer"),     # farmer or admin
    ("active_page",  "scan_leaf"),  # For main app navigation
    ("history",      []),
    ("results",      []),
    ("scanned",      0),
    ("expert_mode",  False),
    ("compare_idx",  None),
    ("loading_done", False),
]:
    if key not in st.session_state:
        st.session_state[key] = default

# ── Page imports ──────────────────────────────────────────────────
from ui.loading  import show_loading
from ui.landing  import show_landing
from ui.main_app import show_main_app

# ── Router ────────────────────────────────────────────────────────
print(f"[ROUTER DEBUG] Current page: {st.session_state.page}")

if st.session_state.page == "loading":
    show_loading()

elif st.session_state.page == "landing":
    show_landing()

elif st.session_state.page == "main":
    print("[ROUTER DEBUG] Calling show_main_app()")
    show_main_app()

# To add more pages:
# elif st.session_state.page == "settings":
#     from ui.settings import show_settings
#     show_settings()
