import time
import streamlit as st
import streamlit.components.v1 as components

def show_loading():
    # ── Kill ALL Streamlit chrome + force true fullscreen ──────────────────
    st.markdown("""
    <style>
    /* Remove ALL Streamlit padding/margins */
    .main .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
        width: 100% !important;
    }
    [data-testid="stAppViewContainer"] {
        padding: 0 !important;
        margin: 0 !important;
        background: #020d0a !important;
    }
    [data-testid="stAppViewBlockContainer"] {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    /* Hide header, footer, sidebar toggle */
    header[data-testid="stHeader"] { display: none !important; }
    footer { display: none !important; }
    #MainMenu { display: none !important; }
    /* Make the iframe truly fullscreen */
    iframe {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        z-index: 9999 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
      *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

      html, body {
        width: 100%; height: 100%;
        background: #020d0a;
        overflow: hidden;
      }

      .cj-root {
        width: 100vw;
        height: 100vh;
        background: radial-gradient(ellipse 80% 80% at 50% 50%, #4a2d5e 0%, #2d1b3d 35%, #1a0f26 65%, #0d0515 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: 'Inter', sans-serif;
        overflow: hidden;
        position: relative;
      }

      /* Subtle animated ambient glow */
      .ambient {
        position: absolute;
        inset: 0;
        background: radial-gradient(ellipse 55% 55% at 50% 48%, rgba(0,230,130,0.07) 0%, transparent 65%);
        pointer-events: none;
        animation: ambientPulse 4s ease-in-out infinite;
      }
      @keyframes ambientPulse {
        0%, 100% { opacity: 0.7; }
        50% { opacity: 1; }
      }

      /* Frame wrapper — content block */
      .frame-wrap {
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 52px 64px 48px;
        margin-top: -40px;
      }

      /* Corner brackets */
      .corner { position: absolute; width: 26px; height: 26px; }
      .corner-tl { top: 0; left: 0;
        border-top: 1.5px solid rgba(0,230,130,0.6);
        border-left: 1.5px solid rgba(0,230,130,0.6); }
      .corner-tr { top: 0; right: 0;
        border-top: 1.5px solid rgba(0,230,130,0.6);
        border-right: 1.5px solid rgba(0,230,130,0.6); }
      .corner-bl { bottom: 0; left: 0;
        border-bottom: 1.5px solid rgba(0,230,130,0.6);
        border-left: 1.5px solid rgba(0,230,130,0.6); }
      .corner-br { bottom: 0; right: 0;
        border-bottom: 1.5px solid rgba(0,230,130,0.6);
        border-right: 1.5px solid rgba(0,230,130,0.6); }

      /* Icon box — uses inline SVG corn instead of emoji */
      .icon-box {
        width: 86px;
        height: 86px;
        background: rgba(0,230,130,0.07);
        border: 1.5px solid rgba(0,230,130,0.22);
        border-radius: 22px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 8px;
        position: relative;
        font-size: 48px;
        line-height: 1;
      }
      .icon-box svg {
        width: 46px;
        height: 46px;
      }
      .icon-ping {
        position: absolute;
        top: -4px; right: -4px;
        width: 10px; height: 10px;
        border-radius: 50%;
        background: #b366ff;
        box-shadow: 0 0 8px rgba(179,102,255,0.8);
      }
      .icon-ping::after {
        content: '';
        position: absolute;
        inset: -5px;
        border-radius: 50%;
        border: 1.5px solid rgba(179,102,255,0.45);
        animation: ping 2.2s ease-out infinite;
      }
      @keyframes ping {
        0%   { transform: scale(1); opacity: 1; }
        100% { transform: scale(2.5); opacity: 0; }
      }

      /* Small dot separator */
      .dot-accent {
        width: 6px; height: 6px;
        border-radius: 50%;
        background: #00e682;
        margin-bottom: 16px;
        opacity: 0.75;
        box-shadow: 0 0 8px rgba(0,230,130,0.6);
      }

      /* Title */
      .title {
        font-size: 58px;
        font-weight: 800;
        letter-spacing: -2px;
        line-height: 1;
        color: #ffffff;
        margin-bottom: 22px;
        text-align: center;
      }
      .title .green {
        color: #00e682;
        text-shadow:
          0 0 20px rgba(0,230,130,0.55),
          0 0 50px rgba(0,230,130,0.25),
          0 0 90px rgba(0,230,130,0.1);
      }

      /* Status label */
      .status-text {
        font-size: 13px;
        font-weight: 400;
        letter-spacing: 0.07em;
        color: rgba(255,255,255,0.5);
        margin-bottom: 22px;
        min-height: 18px;
        text-align: center;
        transition: opacity 0.3s ease;
      }

      /* Progress section */
      .progress-wrap {
        width: 360px;
        margin-bottom: 16px;
      }
      .progress-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 9px;
        font-size: 10.5px;
        letter-spacing: 0.1em;
        color: rgba(255,255,255,0.3);
        font-weight: 600;
      }
      .progress-pct {
        color: rgba(0,230,130,0.7);
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.05em;
      }
      .progress-track {
        width: 100%;
        height: 5px;
        background: rgba(255,255,255,0.07);
        border-radius: 99px;
        overflow: hidden;
      }
      .progress-fill {
        height: 100%;
        border-radius: 99px;
        background: linear-gradient(90deg, #00a65a 0%, #00e682 100%);
        box-shadow: 0 0 12px rgba(0,230,130,0.65), 0 0 4px rgba(0,230,130,0.4);
        width: 0%;
        transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);
      }

      /* Progress dots */
      .dots-row {
        display: flex;
        gap: 7px;
        margin-top: 6px;
        margin-bottom: 22px;
      }
      .pdot {
        width: 7px; height: 7px;
        border-radius: 50%;
        background: rgba(0,230,130,0.2);
        transition: background 0.3s ease;
      }
      .pdot.on  { background: #00e682; box-shadow: 0 0 6px rgba(0,230,130,0.7); }
      .pdot.blink { animation: blink 1s ease-in-out infinite; }
      @keyframes blink {
        0%, 100% { opacity: 1; }
        50%       { opacity: 0.3; }
      }

      /* Chips */
      .chips {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        justify-content: center;
      }
      .chip {
        font-size: 10.5px;
        font-weight: 700;
        letter-spacing: 0.11em;
        color: rgba(0,230,130,0.8);
        border: 1px solid rgba(0,230,130,0.22);
        border-radius: 99px;
        padding: 7px 18px;
        background: rgba(0,230,130,0.05);
        white-space: nowrap;
      }
    </style>
    </head>
    <body>
    <div class="cj-root">
      <div class="ambient"></div>
      <div class="frame-wrap">
        <div class="corner corner-tl"></div>
        <div class="corner corner-tr"></div>
        <div class="corner corner-bl"></div>
        <div class="corner corner-br"></div>

        <!-- Icon box with inline SVG corn (no emoji dependency) -->
        <div class="icon-box">
          🪾
          <div class="icon-ping"></div>
        </div>

        <div class="dot-accent"></div>

        <div class="title">Corn <span class="green">Ji</span></div>

        <div class="status-text" id="statusText">Initializing Neural Vision</div>

        <div class="progress-wrap">
          <div class="progress-header">
            <span>AI SCAN PROGRESS</span>
            <span class="progress-pct" id="pct">0%</span>
          </div>
          <div class="progress-track">
            <div class="progress-fill" id="bar"></div>
          </div>
        </div>

        <div class="dots-row">
          <div class="pdot" id="pd1"></div>
          <div class="pdot" id="pd2"></div>
          <div class="pdot" id="pd3"></div>
          <div class="pdot" id="pd4"></div>
          <div class="pdot" id="pd5"></div>
          <div class="pdot" id="pd6"></div>
        </div>

        <div class="chips">
          <div class="chip">CNN ACTIVE</div>
          <div class="chip">GRAD-CAM READY</div>
          <div class="chip">PRIVATE LOCAL SCAN</div>
        </div>
      </div>
    </div>

    <script>
      const stages = [
        { pct: 12,  label: "Initializing Neural Vision"  },
        { pct: 28,  label: "Loading CNN Weights"          },
        { pct: 45,  label: "Preprocessing Image Data"     },
        { pct: 62,  label: "Classifying Disease Pattern"  },
        { pct: 78,  label: "Generating Grad-CAM Map"      },
        { pct: 91,  label: "Finalizing Results"           },
        { pct: 100, label: "Analysis Complete"            }
      ];

      const bar    = document.getElementById('bar');
      const pctEl  = document.getElementById('pct');
      const stEl   = document.getElementById('statusText');
      const dots   = ['pd1','pd2','pd3','pd4','pd5','pd6'].map(id => document.getElementById(id));
      let cur = 0;

      function updateDots(p) {
        const filled = Math.round((p / 100) * dots.length);
        dots.forEach((d, i) => {
          d.classList.remove('on', 'blink');
          if (i < filled)      d.classList.add('on');
          else if (i === filled) d.classList.add('blink');
        });
      }

      function tick() {
        if (cur >= stages.length) cur = 0;
        const s = stages[cur];
        bar.style.width    = s.pct + '%';
        pctEl.textContent  = s.pct + '%';
        stEl.style.opacity = '0';
        setTimeout(() => {
          stEl.textContent  = s.label;
          stEl.style.opacity = '1';
        }, 200);
        updateDots(s.pct);
        cur++;
        const delay = cur < stages.length ? 1300 : 2500;
        setTimeout(tick, delay);
      }

      setTimeout(tick, 400);
    </script>
    </body>
    </html>
    """

    components.html(html_code, height=800, scrolling=False)
    time.sleep(9)
    st.session_state.page = "landing"
    st.rerun()