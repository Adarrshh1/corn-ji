"""
Tooltips and Help System
"""
import streamlit as st

TOOLTIPS = {
    "scan_leaf": "Upload images of corn leaves to detect diseases using AI",
    "take_picture": "Capture photos directly from your camera for instant analysis",
    "scan_history": "View all your previous scans with search and filter options",
    "reports": "Generate and download detailed PDF reports of your scans",
    "climate": "Check weather conditions and disease risk predictions",
    "confidence": "How sure the AI is about the diagnosis (higher is better)",
    "healthy": "No disease detected - your corn is in good condition",
    "blight": "Fungal disease causing grey lesions - needs immediate treatment",
    "rust": "Orange pustules on leaves - apply fungicide",
    "gray_spot": "Rectangular grey lesions - monitor and treat if spreading"
}

FAQ_DATA = [
    {
        "question": "How accurate is the disease detection?",
        "answer": "Our AI model has 98.4% accuracy based on thousands of corn leaf images. However, always consult an agronomist for critical decisions."
    },
    {
        "question": "What should I do if a disease is detected?",
        "answer": "Follow the treatment recommendations shown in the results. Apply fungicides as suggested and monitor your crops daily."
    },
    {
        "question": "Can I use this offline?",
        "answer": "Currently, the app requires internet connection. Offline mode is coming soon."
    },
    {
        "question": "How is my data stored?",
        "answer": "All data is stored locally on your device. Images are compressed and saved in the scan_data folder. We don't upload anything to external servers."
    },
    {
        "question": "Can I delete my scan history?",
        "answer": "Yes! Go to Scan History and use the delete button for individual scans or 'Clear All' to remove everything."
    }
]

def show_tooltip(key):
    """Get tooltip text for a feature"""
    return TOOLTIPS.get(key, "")

def render_help_page():
    """Render help and FAQ page"""
    st.markdown("### ❓ Help & FAQ")
    st.caption("Find answers to common questions")
    
    st.markdown("---")
    
    # Quick Start Guide
    with st.expander("🚀 Quick Start Guide", expanded=True):
        st.markdown("""
        **Getting Started with Corn Ji:**
        
        1. **Take or Upload Photo**
           - Use 📸 Take Picture to capture from camera
           - Or use 🔬 Scan Leaf to upload existing images
        
        2. **Wait for Analysis**
           - AI will analyze the leaf in seconds
           - Results show disease type and confidence
        
        3. **Follow Recommendations**
           - Read treatment suggestions carefully
           - Apply fungicides as recommended
           - Monitor your crops regularly
        
        4. **Track History**
           - All scans are saved automatically
           - View past results in 📋 Scan History
           - Search and filter by disease type
        
        5. **Check Weather**
           - Use 🌦️ Climate to see disease risks
           - Plan treatments based on weather
        """)
    
    # FAQ Section
    st.markdown("### 💬 Frequently Asked Questions")
    
    for faq in FAQ_DATA:
        with st.expander(f"❓ {faq['question']}"):
            st.markdown(faq['answer'])
    
    st.markdown("---")
    
    # Feature Guide
    st.markdown("### 📚 Feature Guide")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **📸 Take Picture**
        - Capture photos directly
        - Instant analysis
        - Best for field use
        
        **🔬 Scan Leaf**
        - Upload multiple images
        - Batch processing
        - Review before scanning
        
        **📋 Scan History**
        - View all past scans
        - Search by filename
        - Filter by disease type
        - Delete unwanted scans
        """)
    
    with col2:
        st.markdown("""
        **📄 Reports**
        - Generate PDF reports
        - Export scan data
        - Share with experts
        
        **🌦️ Climate**
        - Weather forecast
        - Disease risk alerts
        - Treatment timing
        - Seasonal advice
        """)
    
    st.markdown("---")
    
    # Contact Support
    st.markdown("### 📞 Need More Help?")
    st.info("For technical support or questions, contact your local agricultural extension office.")

def show_onboarding():
    """Show first-time user onboarding"""
    if 'onboarding_done' not in st.session_state:
        st.session_state.onboarding_done = False
    
    if not st.session_state.onboarding_done:
        st.markdown("""
        <div style='background: rgba(255,182,193,0.1); padding: 20px; border-radius: 10px; border: 1px solid rgba(255,182,193,0.3);'>
            <h3 style='color: #ffb6c1; margin-top: 0;'>👋 Welcome to Corn Ji!</h3>
            <p>Your AI-powered corn disease detection assistant</p>
            <p><strong>Quick Tips:</strong></p>
            <ul>
                <li>📸 Use Take Picture for instant field scans</li>
                <li>🔬 Upload multiple images for batch analysis</li>
                <li>📋 All scans are saved automatically</li>
                <li>🌦️ Check weather for disease risk alerts</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([3, 1])
        with col2:
            if st.button("Got it! ✅", use_container_width=True):
                st.session_state.onboarding_done = True
                st.rerun()
