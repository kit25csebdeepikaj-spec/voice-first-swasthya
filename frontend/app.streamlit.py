import streamlit as st
import requests
import os

# Page Configuration
st.set_page_config(
    page_title="Voice-First Swasthya | AI Tele-Triage",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Ultra-Antigravity Cyber-Medical CSS
st.markdown("""
    <style>
    /* Global Theme & Deep Obsidian Background */
    .stApp {
        background-color: #07090E;
        color: #F8FAFC;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* Hero Typography */
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        background: linear-gradient(135deg, #FFFFFF 0%, #94A3B8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: #64748B;
        margin-bottom: 30px;
        line-height: 1.5;
    }

    /* Glassmorphic Container Card */
    .glass-card {
        background: rgba(17, 24, 39, 0.7);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
        margin-top: 20px;
    }

    /* Live Neon Pulse Badge */
    .pulse-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background-color: rgba(16, 185, 129, 0.1);
        color: #10B981;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        border: 1px solid rgba(16, 185, 129, 0.3);
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Futuristic Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%);
        color: white;
        border: none;
        border-radius: 14px;
        font-weight: 600;
        padding: 0.85rem 1.5rem;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.3);
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        width: 100%;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(16, 185, 129, 0.5);
    }
    
    /* Text Area Styling */
    .stTextArea textarea {
        background-color: #0B0F17 !important;
        color: #F8FAFC !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 14px !important;
        padding: 14px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Live Status Indicator
st.markdown('<div class="pulse-badge">● Gnani AI Tele-Triage Engine Online</div>', unsafe_allow_html=True)

# Hero Header
st.markdown('<p class="hero-title">Describe your symptoms.<br>Hear what to do next.</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Multilingual rural health guidance in Hindi, Tamil, Kannada, and English — powered by Prisma STT, Evon 30B, and Timbre TTS.</p>', unsafe_allow_html=True)

# Interactive Form Grid
col1, col2 = st.columns([1.1, 1.0], gap="large")

with col1:
    language_choice = st.selectbox(
        "Select Regional Language Dialect",
        ["hi-IN (Hindi)", "ta-IN (Tamil)", "kn-IN (Kannada)", "en-IN (English)"],
        index=0
    )
    lang_code = language_choice.split(" ")[0]

    user_input = st.text_area(
        "Type or speak patient symptoms:",
        placeholder="e.g., Mujhe pichle do din se severe fever aur body pain hai...",
        height=130
    )

    st.markdown("<div style='height: 5px;'></div>", unsafe_allow_html=True)
    submit_btn = st.button("🚀 Run AI Triage & Synthesize Voice")

with col2:
    st.markdown("### 📊 Diagnostic & Voice Stream")
    
    output_slot = st.empty()

    if submit_btn:
        if not user_input.strip():
            with output_slot.container():
                st.warning("⚠️ Please provide symptoms or a transcript first.")
        else:
            with st.spinner("🔄 Processing multimodal clinical triage..."):
                try:
                    api_url = "http://127.0.0.1:8000/api/triage-text"
                    payload = {
                        "transcript": user_input,
                        "language_code": lang_code
                    }
                    
                    response = requests.post(api_url, json=payload, timeout=10)
                    
                    if response.status_code == 200:
                        data = response.json()
                        triage_cat = data["triage_category"]
                        advice = data["clinical_advice"]
                        
                        with output_slot.container():
                            st.markdown(f"""
                                <div class="glass-card">
                                    <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; color: {'#EF4444' if 'HIGH' in triage_cat else '#10B981'}; font-weight: 700; margin-bottom: 8px;">
                                        {triage_cat}
                                    </div>
                                    <div style="font-size: 1.2rem; font-weight: 500; line-height: 1.5; color: #F8FAFC; margin-bottom: 16px;">
                                        {advice}
                                    </div>
                                </div>
                            """, unsafe_allow_html=True)
                            
                            # Audio Player Stream
                            audio_file = "static_response.wav"
                            if os.path.exists(audio_file):
                                st.markdown("🔊 **Native Voice Output (Gnani Timbre TTS):**")
                                st.audio(audio_file, format="audio/wav")
                            else:
                                st.info("Voice synthesis stream completed.")
                    else:
                        with output_slot.container():
                            st.error(f"Backend Error [{response.status_code}]")
                except Exception as e:
                    with output_slot.container():
                        st.error(f"Connection error: Ensure FastAPI is active on port 8000.")
    else:
        with output_slot.container():
            st.markdown("""
                <div style="border: 1px dashed rgba(255,255,255,0.1); border-radius: 16px; padding: 30px; text-align: center; color: #475569; margin-top: 20px;">
                    <p style="font-size: 0.95rem; margin: 0;">Awaiting symptom input.<br>Results and native voice output will render here instantly.</p>
                </div>
            """, unsafe_allow_html=True)