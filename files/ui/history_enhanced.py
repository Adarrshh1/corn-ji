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
    
    # IMPROVED: Header with enhanced controls
    col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
    with col1:
        search_query = st.text_input("🔍 Search by filename", key="history_search", placeholder="Type to search...")
    with col2:
        disease_types = ["All"] + sorted(list(set([r['label'] for r in st.session_state.history])))
        filter_disease = st.selectbox("🦠 Filter by disease", disease_types, key="filter_disease")
    with col3:
        sort_by = st.selectbox("📊 Sort by", ["Newest", "Oldest", "Confidence ↑", "Confidence ↓"], key="sort_by")
    with col4:
        if st.button("📥 Export All", use_container_width=True, key="export_all_history"):
            export_history_csv(st.session_state.history)
    
    # Clear all button
    if st.button("🗑️ Clear All History", key="clear_all_history"):
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
        st.warning("⚠️ Are you sure? Click 'Clear All History' again to confirm.")
    
    # Filter results
    filtered_history = st.session_state.history.copy()
    
    # Apply search filter
    if search_query:
        filtered_history = [r for r in filtered_history if search_query.lower() in r['fname'].lower()]
    
    # Apply disease filter
    if filter_disease != "All":
        filtered_history = [r for r in filtered_history if r['label'] == filter_disease]
    
    # IMPROVED: Apply sorting
    if sort_by == "Newest":
        filtered_history.sort(key=lambda x: x['ts'], reverse=True)
    elif sort_by == "Oldest":
        filtered_history.sort(key=lambda x: x['ts'])
    elif sort_by == "Confidence ↑":
        filtered_history.sort(key=lambda x: x['conf'])
    elif sort_by == "Confidence ↓":
        filtered_history.sort(key=lambda x: x['conf'], reverse=True)
    
    # IMPROVED: Statistics summary
    if filtered_history:
        st.markdown("")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("📊 Total Scans", len(filtered_history))
        with col2:
            healthy = len([r for r in filtered_history if r['label'] == 'Healthy'])
            st.metric("✅ Healthy", healthy)
        with col3:
            diseased = len(filtered_history) - healthy
            st.metric("⚠️ Diseased", diseased)
        with col4:
            avg_conf = sum(r['conf'] for r in filtered_history) / len(filtered_history)
            st.metric("🎯 Avg Confidence", f"{avg_conf*100:.1f}%")
    
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
    
    if st.session_state.history_page > total_pages:
        st.session_state.history_page = 1
    
    if total_pages > 1:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("⬅️ Previous", disabled=st.session_state.history_page == 1, key="prev_page"):
                st.session_state.history_page -= 1
                st.rerun()
        with col2:
            st.markdown(f"<div style='text-align:center; font-weight:600; color:#ffb6c1;'>Page {st.session_state.history_page} of {total_pages}</div>", unsafe_allow_html=True)
        with col3:
            if st.button("Next ➡️", disabled=st.session_state.history_page == total_pages, key="next_page"):
                st.session_state.history_page += 1
                st.rerun()
        st.markdown("---")
    
    # Display results with enhanced thumbnails
    start_idx = (st.session_state.history_page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    
    for idx, result in enumerate(filtered_history[start_idx:end_idx]):
        actual_idx = st.session_state.history.index(result)
        
        # IMPROVED: Enhanced card layout
        with st.container():
            col_thumb, col_info, col_actions = st.columns([1, 3, 1])
            
            with col_thumb:
                if 'img' in result and result['img']:
                    st.image(result['img'], use_container_width=True)
                elif 'img_path' in result:
                    try:
                        img = Image.open(result['img_path'])
                        st.image(img, use_container_width=True)
                    except:
                        st.markdown("🖼️ No preview")
            
            with col_info:
                label_color = {
                    "Healthy": "#00c853",
                    "Northern Leaf Blight": "#ff5252",
                    "Blight": "#ff5252",
                    "Common Rust": "#ffca28",
                    "Gray Leaf Spot": "#40c4ff"
                }.get(result['label'], "#ffffff")
                
                st.markdown(f"""<div style="background:rgba(255,182,193,0.05); padding:15px; border-radius:10px; border-left:4px solid {label_color};">
                    <div style="font-size:1.2rem; font-weight:700; color:{label_color}; margin-bottom:8px;">{result['label']}</div>
                    <div style="color:rgba(255,255,255,0.7); margin-bottom:5px;">📁 {result['fname']}</div>
                    <div style="color:rgba(255,255,255,0.7); margin-bottom:5px;">🎯 Confidence: <span style="color:#40c4ff; font-weight:600;">{result['conf']*100:.1f}%</span></div>
                    <div style="color:rgba(255,255,255,0.5);">🕐 {result['ts'].strftime('%Y-%m-%d %H:%M:%S')}</div>
                </div>""", unsafe_allow_html=True)
            
            with col_actions:
                st.markdown("")
                st.markdown("")
                if st.button("📥 Download", key=f"download_{actual_idx}", use_container_width=True):
                    download_single_result(result)
                
                if st.button("🗑️ Delete", key=f"delete_{actual_idx}", use_container_width=True):
                    st.session_state.history.pop(actual_idx)
                    st.session_state.scanned -= 1
                    from ui.main_app import save_scan_history
                    save_scan_history()
                    st.rerun()
            
            st.markdown("---")

def export_history_csv(history):
    """Export entire history to CSV"""
    import csv
    from io import StringIO
    from datetime import datetime
    
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['Filename', 'Disease', 'Confidence', 'Timestamp'])
    
    for r in history:
        writer.writerow([
            r['fname'],
            r['label'],
            f"{r['conf']*100:.2f}%",
            r['ts'].strftime('%Y-%m-%d %H:%M:%S')
        ])
    
    st.download_button(
        label="💾 Save History CSV",
        data=output.getvalue(),
        file_name=f"corn_ji_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv",
        use_container_width=True
    )
    st.success("✅ CSV file ready! Click above to download.")

def download_single_result(result):
    """Download single result as HTML card"""
    from datetime import datetime
    
    label = result['label']
    conf = result['conf']
    ts = result['ts'].strftime('%Y-%m-%d %H:%M:%S')
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Corn Ji - {label}</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #1a0f0d; color: #e8f5e9; padding: 40px; }}
            .card {{ background: rgba(255,182,193,0.08); border: 2px solid rgba(255,182,193,0.2); border-radius: 20px; padding: 40px; max-width: 600px; margin: 0 auto; }}
            .title {{ font-size: 2rem; font-weight: 700; color: #ffb6c1; text-align: center; margin-bottom: 20px; }}
            .info {{ margin: 15px 0; padding: 15px; background: rgba(0,0,0,0.2); border-radius: 10px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="title">🌽 Corn Ji - Scan Result</div>
            <div class="info"><strong>Disease:</strong> {label}</div>
            <div class="info"><strong>Confidence:</strong> {conf*100:.1f}%</div>
            <div class="info"><strong>Filename:</strong> {result['fname']}</div>
            <div class="info"><strong>Timestamp:</strong> {ts}</div>
        </div>
    </body>
    </html>
    """
    
    st.download_button(
        label="💾 Save Result Card",
        data=html_content,
        file_name=f"corn_ji_{result['fname'].split('.')[0]}_{result['ts'].strftime('%Y%m%d_%H%M%S')}.html",
        mime="text/html",
        use_container_width=True
    )
    st.success("✅ Result card ready!")
