"""
CornScan AI · ui/landing.py
Rebuilt with perfect spacing and hierarchy.
"""
import streamlit as st
import streamlit.components.v1 as components
import time
from styles.styles import inject_css


def show_landing():
    inject_css()

    html_content = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { 
    margin: 0; 
    padding: 0; 
    box-sizing: border-box; 
}

body { 
    background: #000000;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', sans-serif;
    overflow: hidden;
    width: 100vw;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0;
    padding: 0;
}

/* Cinematic background */
.background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
        radial-gradient(ellipse at center, rgba(0,255,174,0.06) 0%, transparent 60%),
        linear-gradient(rgba(0,255,174,0.002) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,255,174,0.002) 1px, transparent 1px);
    background-size: 100% 100%, 150px 150px, 150px 150px;
    background-position: center, 0 0, 0 0;
    animation: gridMove 40s linear infinite;
    z-index: 0;
    pointer-events: none;
}

.background::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 1000px;
    height: 1000px;
    background: radial-gradient(circle, rgba(0,255,174,0.08) 0%, transparent 70%);
    filter: blur(120px);
    animation: breathe 12s ease-in-out infinite;
    pointer-events: none;
}

.background::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(ellipse at center, transparent 20%, rgba(0,0,0,0.9) 100%);
    pointer-events: none;
}

@keyframes gridMove {
    0% { background-position: center, 0 0, 0 0; }
    100% { background-position: center, 150px 150px, 150px 150px; }
}

@keyframes breathe {
    0%, 100% {
        opacity: 1;
        transform: translate(-50%, -50%) scale(1);
    }
    50% {
        opacity: 0.7;
        transform: translate(-50%, -50%) scale(1.08);
    }
}

/* Main Layout Container */
.layout-container {
    position: relative;
    z-index: 5;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 26px;
    width: 100%;
    max-width: 800px;
    height: 80vh;
    animation: fadeIn 1.2s ease-out;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

/* 1. TITLE */
.title {
    font-size: 72px;
    font-weight: 800;
    letter-spacing: -2px;
    text-align: center;
    line-height: 1;
    margin: 0;
    animation: slideDown 1s ease-out;
}

@keyframes slideDown {
    from {
        opacity: 0;
        transform: translateY(-30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.title-corn {
    color: #e5e5e5;
}

.title-ji {
    color: #00ffae;
    text-shadow: 0 0 20px rgba(0,255,174,0.5);
}

/* 2. SPACE AFTER TITLE - REMOVED */

/* 3. BADGES GRID */
.badges-grid {
    display: grid;
    grid-template-columns: repeat(2, 240px);
    gap: 18px 22px;
    animation: scaleIn 1s ease-out 0.3s both;
}

@keyframes scaleIn {
    from {
        opacity: 0;
        transform: scale(0.9);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

.badge {
    position: relative;
    padding: 16px 40px;
    height: 58px;
    border-radius: 30px;
    background: rgba(0,255,174,0.04);
    border: 1px solid rgba(0,255,174,0.1);
    color: rgba(255,255,255,0.9);
    font-size: 18px;
    font-weight: 600;
    text-align: center;
    backdrop-filter: blur(20px);
    cursor: pointer;
    transition: all 0.25s ease-out;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    white-space: nowrap;
    display: flex;
    align-items: center;
    justify-content: center;
}

.badge:hover {
    transform: translateY(-4px) scale(1.05);
    border-color: rgba(0,255,174,0.3);
    box-shadow: 0 0 30px rgba(0,255,174,0.3);
}

.badge.active {
    background: rgba(0,255,174,0.12);
    border-color: rgba(0,255,174,0.4);
    animation: pulseActive 3s ease-in-out infinite;
}

@keyframes pulseActive {
    0%, 100% {
        box-shadow: 0 0 25px rgba(0,255,174,0.4);
    }
    50% {
        box-shadow: 0 0 40px rgba(0,255,174,0.6);
    }
}

.badges-grid:has(.badge.active) .badge:not(.active) {
    opacity: 0.5;
}

.badge.blight {
    background: rgba(60,30,10,0.15);
    border-color: rgba(210,140,60,0.12);
}

.badge.blight:hover {
    box-shadow: 0 0 25px rgba(210,140,60,0.3);
    border-color: rgba(210,140,60,0.4);
}

.badge.blight.active {
    background: rgba(60,30,10,0.25);
    box-shadow: 0 0 35px rgba(210,140,60,0.5);
}

.badge.rust {
    background: rgba(70,30,5,0.15);
    border-color: rgba(255,130,30,0.12);
}

.badge.rust:hover {
    box-shadow: 0 0 25px rgba(255,130,30,0.3);
    border-color: rgba(255,130,30,0.4);
}

.badge.rust.active {
    background: rgba(70,30,5,0.25);
    box-shadow: 0 0 35px rgba(255,130,30,0.5);
}

.badge.spot {
    background: rgba(40,40,40,0.15);
    border-color: rgba(170,170,170,0.12);
}

.badge.spot:hover {
    box-shadow: 0 0 25px rgba(170,170,170,0.25);
    border-color: rgba(170,170,170,0.4);
}

.badge.spot.active {
    background: rgba(40,40,40,0.25);
    box-shadow: 0 0 35px rgba(170,170,170,0.4);
}

.badge.healthy {
    background: rgba(10,50,30,0.15);
    border-color: rgba(0,255,174,0.12);
}

.badge.healthy:hover {
    box-shadow: 0 0 25px rgba(0,255,174,0.3);
    border-color: rgba(0,255,174,0.4);
}

.badge.healthy.active {
    background: rgba(10,50,30,0.25);
    box-shadow: 0 0 35px rgba(0,255,174,0.5);
}

/* Badge Tooltip - ABSOLUTE POSITIONING */
.badge-tooltip {
    position: absolute;
    left: 50%;
    bottom: calc(100% + 10px);
    transform: translateX(-50%);
    background: rgba(8,24,18,0.96);
    backdrop-filter: blur(25px);
    border: 1px solid rgba(0,255,174,0.28);
    border-radius: 14px;
    padding: 10px 16px;
    min-width: 240px;
    max-width: 280px;
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
    transition: all 0.2s ease-out;
    box-shadow: 
        0 0 30px rgba(0,255,174,0.15),
        0 8px 30px rgba(0,0,0,0.7);
    z-index: 100;
    text-align: center;
    white-space: normal;
}

.badge:hover .badge-tooltip {
    opacity: 1;
    visibility: visible;
}

.tooltip-title {
    color: #00ffae;
    font-size: 0.95rem;
    font-weight: 700;
    margin-bottom: 4px;
}

.tooltip-desc {
    color: rgba(255,255,255,0.75);
    font-size: 0.8rem;
    line-height: 1.4;
}

/* 4. BUTTON WRAPPER */
.button-wrapper {
    margin-top: 8px;
    display: flex;
    justify-content: center;
}

.cta-button {
    width: 300px;
    height: 64px;
    border: none;
    border-radius: 999px;
    font-size: 20px;
    font-weight: 700;
    color: #03150f;
    background: linear-gradient(180deg, #22f5b5, #10d995);
    box-shadow: 0 0 30px rgba(25,245,179,0.35);
    cursor: pointer;
    transition: all 0.25s ease-out;
    animation: fadeInUp 1s ease-out 0.5s both;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.cta-button:hover {
    transform: translateY(-4px) scale(1.05);
    box-shadow: 0 0 40px rgba(25,245,179,0.5);
}

.cta-button:active {
    transform: translateY(0) scale(0.98);
}

/* Left Icon Strip */
.icon-strip {
    position: fixed;
    left: 50px;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: 32px;
    z-index: 10;
    animation: fadeInLeft 1s ease-out 0.7s both;
}

@keyframes fadeInLeft {
    from {
        opacity: 0;
        transform: translateY(-50%) translateX(-30px);
    }
    to {
        opacity: 1;
        transform: translateY(-50%) translateX(0);
    }
}

.icon-wrapper {
    position: relative;
}

.icon {
    width: 56px;
    height: 56px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8rem;
    background: rgba(0,255,174,0.015);
    border: 1px solid rgba(0,255,174,0.04);
    border-radius: 16px;
    cursor: pointer;
    transition: all 0.25s ease-out;
    backdrop-filter: blur(10px);
    opacity: 0.7;
}

.icon:hover {
    transform: scale(1.1);
    background: rgba(0,255,174,0.06);
    border-color: rgba(0,255,174,0.25);
    box-shadow: 0 0 30px rgba(0,255,174,0.25);
    opacity: 1;
}

.icon-tooltip {
    position: absolute;
    left: 80px;
    top: 50%;
    transform: translateY(-50%) translateX(-15px);
    background: rgba(10,30,25,0.96);
    backdrop-filter: blur(25px);
    border: 1px solid rgba(0,255,174,0.25);
    border-radius: 12px;
    padding: 12px 18px;
    min-width: 220px;
    opacity: 0;
    pointer-events: none;
    transition: all 0.25s ease-out;
    box-shadow: 
        0 0 30px rgba(0,255,174,0.15),
        0 8px 30px rgba(0,0,0,0.7);
    z-index: 100;
}

.icon-wrapper:hover .icon-tooltip {
    opacity: 1;
    transform: translateY(-50%) translateX(0);
}

/* Responsive */
@media (max-width: 768px) {
    .title {
        font-size: 3rem;
    }
    
    .space-title {
        height: 60px;
    }
    
    .space-button {
        height: 120px;
    }
    
    .badges-grid {
        grid-template-columns: 1fr;
        gap: 16px;
    }
    
    .badge {
        padding: 14px 32px;
    }
    
    .cta-button {
        padding: 18px 50px;
        font-size: 1.3rem;
    }
    
    .icon-strip {
        left: 25px;
        gap: 24px;
    }
    
    .icon {
        width: 48px;
        height: 48px;
        font-size: 1.5rem;
    }
}
</style>
</head>
<body>
    <div class="background"></div>
    
    <!-- Left Icon Strip -->
    <div class="icon-strip">
        <div class="icon-wrapper">
            <div class="icon">🔥</div>
            <div class="icon-tooltip">
                <div class="tooltip-title">Vision AI</div>
                <div class="tooltip-desc">AI-powered detection engine</div>
            </div>
        </div>
        <div class="icon-wrapper">
            <div class="icon">🧠</div>
            <div class="icon-tooltip">
                <div class="tooltip-title">Expert Mode</div>
                <div class="tooltip-desc">Advanced insights for agronomists</div>
            </div>
        </div>
        <div class="icon-wrapper">
            <div class="icon">⚡</div>
            <div class="icon-tooltip">
                <div class="tooltip-title">Fast Scan</div>
                <div class="tooltip-desc">Instant disease detection</div>
            </div>
        </div>
        <div class="icon-wrapper">
            <div class="icon">📋</div>
            <div class="icon-tooltip">
                <div class="tooltip-title">Treatment Plan</div>
                <div class="tooltip-desc">Actionable recommendations</div>
            </div>
        </div>
        <div class="icon-wrapper">
            <div class="icon">🌤️</div>
            <div class="icon-tooltip">
                <div class="tooltip-title">Weather Forecast</div>
                <div class="tooltip-desc">Risk prediction system</div>
            </div>
        </div>
        <div class="icon-wrapper">
            <div class="icon">📄</div>
            <div class="icon-tooltip">
                <div class="tooltip-title">Export Reports</div>
                <div class="tooltip-desc">Download detailed analysis</div>
            </div>
        </div>
    </div>
    
    <!-- Main Layout -->
    <div class="layout-container">
        <!-- 1. TITLE -->
        <h1 class="title">
            <span class="title-corn">Corn</span><span class="title-ji"> Ji</span>
        </h1>
        
        <!-- 2. BADGES -->
        <div class="badges-grid">
            <div class="badge blight" onclick="toggleBadge(this)">
                🍂 Blight
                <div class="badge-tooltip">
                    <div class="tooltip-title">Northern Leaf Blight</div>
                    <div class="tooltip-desc">Fungal disease causing long grey lesions</div>
                </div>
            </div>
            <div class="badge rust" onclick="toggleBadge(this)">
                🟠 Common Rust
                <div class="badge-tooltip">
                    <div class="tooltip-title">Common Rust</div>
                    <div class="tooltip-desc">Orange pustules on leaf surface</div>
                </div>
            </div>
            <div class="badge spot" onclick="toggleBadge(this)">
                🩶 Gray Leaf Spot
                <div class="badge-tooltip">
                    <div class="tooltip-title">Gray Leaf Spot</div>
                    <div class="tooltip-desc">Rectangular lesions with grey centers</div>
                </div>
            </div>
            <div class="badge healthy" onclick="toggleBadge(this)">
                ✅ Healthy
                <div class="badge-tooltip">
                    <div class="tooltip-title">Healthy Leaf</div>
                    <div class="tooltip-desc">No disease symptoms detected</div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
    function toggleBadge(element) {
        const allBadges = document.querySelectorAll('.badge');
        if (element.classList.contains('active')) {
            element.classList.remove('active');
        } else {
            allBadges.forEach(badge => badge.classList.remove('active'));
            element.classList.add('active');
        }
    }
    </script>
</body>
</html>
    """
    
    # Display the HTML component with reduced height
    components.html(html_content, height=800, scrolling=False)
    
    # Add small delay to ensure HTML loads
    time.sleep(0.1)
    
    # REAL STREAMLIT BUTTON (perfectly centered at bottom)
    if st.button("🚀 Let's Go", key="hero_go", type="primary"):
        st.session_state.page = "main"
        st.session_state.active_page = "scan_leaf"
        st.rerun()
    
    # STYLE THE BUTTON TO MATCH DESIGN
    st.markdown("""
    <style>
    /* Full page reset - Remove ALL default spacing */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        margin: 0 !important;
        padding: 0 !important;
        height: 100vh !important;
        overflow: hidden !important;
        background: radial-gradient(circle at center, rgba(0,255,140,0.18) 0%, rgba(0,0,0,1) 55%),
                    linear-gradient(rgba(0,255,120,0.08) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(0,255,120,0.08) 1px, transparent 1px),
                    #000 !important;
        background-size: auto, 48px 48px, 48px 48px, auto !important;
        background-position: center center !important;
    }
    
    /* Remove Streamlit default block container padding */
    [data-testid="block-container"] {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    
    /* Remove top header spacing */
    [data-testid="stHeader"] {
        background: transparent !important;
        height: 0 !important;
        display: none !important;
    }
    
    /* Main area full screen */
    section.main {
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Remove app view block container padding */
    [data-testid="stAppViewContainer"] > .main {
        padding-top: 0rem !important;
    }
    
    [data-testid="stAppViewBlockContainer"] {
        padding-top: 0rem !important;
    }
    
    /* Remove toolbar spacing */
    div[data-testid="stToolbar"] {
        right: 1rem !important;
    }
    
    /* Perfect center bottom button */
    div.stButton {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        position: fixed !important;
        bottom: 40px !important;
        left: 0 !important;
        right: 0 !important;
        width: 100% !important;
        z-index: 1000 !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    div.stButton > button {
        width: 320px !important;
        height: 64px !important;
        border: none !important;
        border-radius: 999px !important;
        font-size: 20px !important;
        font-weight: 700 !important;
        color: #03150f !important;
        background: linear-gradient(180deg, #22f5b5, #10d995) !important;
        box-shadow: 0 0 30px rgba(25,245,179,0.35) !important;
        transition: 0.2s !important;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 0 40px rgba(25,245,179,0.5) !important;
    }
    
    div.stButton > button:active {
        transform: translateY(0) scale(0.98) !important;
    }
    </style>
    """, unsafe_allow_html=True)
