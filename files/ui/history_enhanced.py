"""
Enhanced History Page with Search, Filter, and Thumbnails
"""
import streamlit as st
from datetime import datetime
from PIL import Image

def render_history_page_enhanced():
    st.markdown("### 📋 Scan History")
    
    if not st.session_state.history:
        st.info("No scans yet — upload leaf images to begin")
        return
    
    # Header with controls
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        # Search box
        search_query = st.text_input("🔍 Search by filename", key="history_search", placeholder="Type to search...")
    with col2:
        # Filter by disease type
        disease_types = ["All"] + list(set([r['label'] for r in st.session_state.history]))
        filter_disease = st.selectbox("Filter by disease", disease_types, key="filter_disease")
    with col3:
        # Clear all button
        if st.button("🗑️ Clear All", use_container_width=True, key="clear_all_history"):
            if st.session_state.get('confirm_clear', False):
                st.session_state.history = []
                st.session_state.scanned = 0
                from ui.main_app import save_scan_history
                save_scan_history()
                st.session_state.confirm_clear = False
                st.success("✅ History cleared!")
                st.rerun()
            else:
                st.session_state.confirm_clear = True
                st.rerun()
    
    if st.session_state.get('confirm_clear', False):
        st.warning("⚠️ Are you sure? Click 'Clear All' again to confirm.")
    
    # Filter results
    filtered_history = st.session_state.history
    
    # Apply search filter
    if search_query:
        filtered_history = [r for r in filtered_history if search_query.lower() in r['fname'].lower()]
    
    # Apply disease filter
    if filter_disease != "All":
        filtered_history = [r for r in filtered_history if r['label'] == filter_disease]
    
    st.caption(f"Showing {len(filtered_history)} of {len(st.session_state.history)} scans")
    st.markdown("---")
    
    if not filtered_history:
        st.info("No results found")
        return
    
    # Pagination
    items_per_page = 10
    total_pages = (len(filtered_history) - 1) // items_per_page + 1
    
    if 'history_page' not in st.session_state:
        st.session_state.history_page = 1
    
    # Reset page if filter changes
    if st.session_state.history_page > total_pages:
        st.session_state.history_page = 1
    
    if total_pages > 1:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("⬅️ Previous", disabled=st.session_state.history_page == 1, key="prev_page"):
                st.session_state.history_page -= 1
                st.rerun()
        with col2:
            st.markdown(f"<div style='text-align:center'>Page {st.session_state.history_page} of {total_pages}</div>", unsafe_allow_html=True)
        with col3:
            if st.button("Next ➡️", disabled=st.session_state.history_page == total_pages, key="next_page"):
                st.session_state.history_page += 1
                st.rerun()
        st.markdown("---")
    
    # Display results with thumbnails
    start_idx = (st.session_state.history_page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    
    for idx, result in enumerate(filtered_history[start_idx:end_idx]):
        actual_idx = st.session_state.history.index(result)
        
        # Create thumbnail view
        col_thumb, col_info, col_actions = st.columns([1, 3, 1])
        
        with col_thumb:
            if 'img' in result:
                st.image(result['img'], use_container_width=True)
        
        with col_info:
            # Disease label with color coding
            label_color = {
                "Healthy": "#00c853",
                "Northern Leaf Blight": "#ff5252",
                "Common Rust": "#ffca28",
                "Gray Leaf Spot": "#40c4ff"
            }.get(result['label'], "#ffffff")
            
            st.markdown(f"**<span style='color:{label_color}'>{result['label']}</span>**", unsafe_allow_html=True)
            st.caption(f"📁 {result['fname']}")
            st.caption(f"🎯 Confidence: {result['conf']*100:.1f}%")
            st.caption(f"🕐 {result['ts'].strftime('%Y-%m-%d %H:%M:%S')}")
        
        with col_actions:
            if st.button("🗑️", key=f"delete_{actual_idx}", help="Delete this scan"):
                st.session_state.history.pop(actual_idx)
                st.session_state.scanned -= 1
                from ui.main_app import save_scan_history
                save_scan_history()
                st.rerun()
            
            if st.button("📥", key=f"download_{actual_idx}", help="Download image"):
                # Trigger download
                st.info("Download feature coming soon")
        
        st.markdown("---")
