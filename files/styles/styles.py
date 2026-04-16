"""
CornScan AI · styles/styles.py
Premium CSS for vertical timeline/stacked feature layout.
"""

import streamlit as st


def inject_css():
    st.markdown("""
<style>
header, footer {visibility: hidden;}
.stDeployButton {display:none;}

.stApp {
    background:
        linear-gradient(rgba(0,255,120,0.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,255,120,0.035) 1px, transparent 1px),
        radial-gradient(circle at center, rgba(0,255,120,0.08), transparent 42%),
        #020706;
    background-size: 60px 60px, 60px 60px, 100% 100%, 100% 100%;
    color: white;
    overflow-x: hidden;
}

.block-container {
    max-width: 100% !important;
    padding-top: 1rem !important;
    padding-bottom: 2rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}

.hero-wrap {
    display: flex;
    justify-content: center;
    text-align: center;
    padding-top: 2rem;
    padding-bottom: 1rem;
}

.hero-content {
    width: 100%;
    max-width: 900px;
    margin: 0 auto;
}

.hero-title {
    font-size: 5.4rem;
    line-height: 0.95;
    font-weight: 900;
    letter-spacing: -3px;
    color: #ffffff;
    margin: 0;
}

.hero-title .accent {
    color: #18f2b2;
    text-shadow: 0 0 16px rgba(24,242,178,0.22);
}

.hero-sub {
    margin-top: 0.8rem;
    margin-bottom: 2rem;
    font-size: 1.08rem;
    color: rgba(255,255,255,0.72);
}

.stack-flow {
    display: flex;
    flex-direction: column;
    gap: 14px;
    align-items: center;
}

.flow-row {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.center-row {
    justify-content: center;
}

.split-row {
    justify-content: center;
    gap: 16px;
}

.feature-card {
    position: relative;
    overflow: hidden;
    width: 235px;
    min-height: 125px;
    background: linear-gradient(180deg, rgba(8,40,26,0.72), rgba(4,24,16,0.78));
    border: 1px solid rgba(24,242,178,0.14);
    border-radius: 20px;
    padding: 18px 16px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    backdrop-filter: blur(10px);
    box-shadow:
        0 0 0 1px rgba(255,255,255,0.02) inset,
        0 12px 30px rgba(0,0,0,0.22);
    transition: all 0.28s ease;
    cursor: pointer;
}

.feature-card:hover {
    transform: translateY(-6px);
    border-color: rgba(24,242,178,0.34);
    box-shadow:
        0 0 20px rgba(24,242,178,0.08),
        0 18px 36px rgba(0,0,0,0.28);
}

.emoji {
    font-size: 2rem;
    margin-bottom: 10px;
    z-index: 2;
    transition: transform 0.3s ease;
}

.card-title {
    color: #ffffff;
    font-size: 1.05rem;
    font-weight: 700;
    line-height: 1.35;
    z-index: 2;
    transition: transform 0.3s ease;
}

.hover-info {
    position: absolute;
    left: 16px;
    right: 16px;
    bottom: 14px;
    font-size: 0.8rem;
    line-height: 1.35;
    color: rgba(255,255,255,0.78);
    opacity: 0;
    transform: translateY(12px);
    transition: all 0.35s ease;
    pointer-events: none;
}

.feature-card:hover .hover-info {
    opacity: 1;
    transform: translateY(0);
}

.feature-card:hover .emoji {
    transform: translateY(-8px) scale(1.05);
}

.feature-card:hover .card-title {
    transform: translateY(-6px);
}

.badge-stack {
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
}

.class-badge {
    min-width: 165px;
    text-align: left;
    padding: 10px 16px;
    border-radius: 14px;
    border: 1px solid rgba(24,242,178,0.18);
    background: rgba(0, 60, 40, 0.34);
    color: rgba(255,255,255,0.9);
    font-size: 0.92rem;
    font-weight: 700;
    transition: all 0.25s ease;
    box-shadow: 0 0 10px rgba(24,242,178,0.04);
}

.class-badge:hover {
    transform: translateX(4px);
    border-color: rgba(24,242,178,0.42);
}

.blight:hover {
    box-shadow: 0 0 14px rgba(210,140,60,0.28);
}

.rust:hover {
    box-shadow: 0 0 14px rgba(255,130,30,0.28);
}

.spot:hover {
    box-shadow: 0 0 14px rgba(170,170,170,0.24);
}

.healthy:hover {
    box-shadow: 0 0 14px rgba(80,255,140,0.28);
}

.cta-wrap {
    height: 18px;
}

div[data-testid="stButton"] {
    display: flex;
    justify-content: center;
    margin-top: 1rem;
}

div[data-testid="stButton"] > button {
    width: 320px;
    height: 58px;
    border-radius: 18px;
    border: 1px solid rgba(24,242,178,0.22);
    background: linear-gradient(90deg, rgba(0,110,66,0.88), rgba(0,70,42,0.95));
    color: #18f2b2;
    font-size: 1.08rem;
    font-weight: 800;
    box-shadow: 0 0 24px rgba(24,242,178,0.08);
    transition: all 0.25s ease;
}

div[data-testid="stButton"] > button:hover {
    color: white;
    border-color: rgba(24,242,178,0.48);
    transform: translateY(-2px);
    box-shadow: 0 0 30px rgba(24,242,178,0.14);
}

@media (max-width: 900px) {
    .hero-title {
        font-size: 3.6rem;
        letter-spacing: -1.5px;
    }

    .split-row {
        flex-direction: column;
        gap: 12px;
    }

    .badge-stack {
        align-items: center;
    }

    .class-badge {
        min-width: 220px;
        text-align: center;
    }

    .feature-card {
        width: 240px;
    }
}
</style>
""", unsafe_allow_html=True)
