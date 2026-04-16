"""
Mobile Responsive CSS for Corn Ji
"""

MOBILE_CSS = """
<style>
/* Mobile Responsive Styles */

/* Base responsive adjustments */
@media (max-width: 768px) {
    /* Reduce padding on mobile */
    .block-container {
        padding: 1rem !important;
    }
    
    /* Stack columns vertically */
    .row-widget.stHorizontal {
        flex-direction: column !important;
    }
    
    /* Full width buttons */
    .stButton > button {
        width: 100% !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Larger touch targets */
    button, a, input {
        min-height: 44px !important;
        font-size: 16px !important;
    }
    
    /* Adjust metrics */
    [data-testid="stMetricValue"] {
        font-size: 1.5rem !important;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 0.9rem !important;
    }
    
    /* Sidebar adjustments */
    [data-testid="stSidebar"] {
        width: 100% !important;
        min-width: 100% !important;
    }
    
    /* Image adjustments */
    img {
        max-width: 100% !important;
        height: auto !important;
    }
    
    /* File uploader */
    [data-testid="stFileUploader"] {
        padding: 10px !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        font-size: 0.9rem !important;
    }
    
    /* Tables */
    table {
        font-size: 0.85rem !important;
    }
    
    /* Camera input */
    [data-testid="stCameraInput"] {
        width: 100% !important;
    }
}

/* Tablet adjustments */
@media (min-width: 769px) and (max-width: 1024px) {
    .block-container {
        padding: 1.5rem !important;
    }
    
    [data-testid="stSidebar"] {
        width: 18rem !important;
    }
}

/* Touch-friendly improvements */
@media (hover: none) and (pointer: coarse) {
    /* Larger tap targets */
    button, a, input, select {
        min-height: 48px !important;
        padding: 12px !important;
    }
    
    /* Remove hover effects on touch devices */
    button:hover {
        transform: none !important;
    }
    
    /* Better spacing for touch */
    .stButton {
        margin: 8px 0 !important;
    }
}

/* Landscape mobile */
@media (max-width: 768px) and (orientation: landscape) {
    /* Reduce vertical spacing */
    .block-container {
        padding: 0.5rem !important;
    }
    
    /* Compact metrics */
    [data-testid="stMetricValue"] {
        font-size: 1.2rem !important;
    }
}

/* Small phones */
@media (max-width: 375px) {
    /* Extra compact */
    h1 {
        font-size: 1.5rem !important;
    }
    
    h2 {
        font-size: 1.3rem !important;
    }
    
    h3 {
        font-size: 1.1rem !important;
    }
    
    /* Smaller buttons */
    .stButton > button {
        font-size: 0.9rem !important;
        padding: 8px 12px !important;
    }
}

/* Prevent zoom on input focus (iOS) */
@media screen and (max-width: 768px) {
    input[type="text"],
    input[type="number"],
    input[type="email"],
    textarea,
    select {
        font-size: 16px !important;
    }
}

/* Loading spinner mobile */
@media (max-width: 768px) {
    .loader {
        width: 40px !important;
        height: 40px !important;
    }
}

/* Grid adjustments for mobile */
@media (max-width: 768px) {
    /* 2-column grid becomes 1-column */
    .badges-grid {
        grid-template-columns: 1fr !important;
    }
    
    /* Forecast cards stack */
    .forecast-cols {
        flex-direction: column !important;
    }
}

/* Accessibility improvements */
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
    /* Already dark, but ensure consistency */
    body {
        background: #1a0f0d !important;
    }
}

/* High contrast mode */
@media (prefers-contrast: high) {
    button {
        border: 2px solid currentColor !important;
    }
    
    .stButton > button[kind="primary"] {
        border: 2px solid #ffb6c1 !important;
    }
}
</style>
"""

def inject_mobile_css():
    """Inject mobile responsive CSS"""
    import streamlit as st
    st.markdown(MOBILE_CSS, unsafe_allow_html=True)
