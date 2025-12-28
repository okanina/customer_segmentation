import pandas as pd
import streamlit as st

# Must be first Streamlit call
st.set_page_config(
    page_title="People's Shop",
    page_icon="🛒",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={"Report a bug": "mailto:kjjkhanyi@gmail.com"}
)

# ---------- Custom CSS ----------
page_bg = """
<style>
/* App background */
[data-testid="stAppViewContainer"] {
    
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Overlay container */
.block-container {
    background: rgba(255, 255, 255, 0.85);
    padding: 3rem 2.5rem;
    border-radius: 20px;
    max-width: 550px;
    margin: 5rem auto;
    box-shadow: 0 12px 40px rgba(0,0,0,0.2);
}

/* Center text */
h1, h2, h3 {
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
}

/* Button styling */
.stButton > button {
    width: 100%;
    border-radius: 12px;
    padding: 0.75rem;
    font-size: 1.1rem;
    font-weight: 600;
    background: linear-gradient(135deg, #ff7eb3, #ff758c);
    border: none;
    color: white;
    transition: all 0.2s ease-in-out;
}

.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0 8px 20px rgba(255, 117, 140, 0.5);
}

/* Subtitle style */
.subtitle {
    text-align: center;
    font-size: 1.1rem;
    color: #444;
    margin-bottom: 2rem;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ---------- Content ----------
st.title("🛍️ Welcome to People's Shop")
st.markdown('<div class="subtitle">Discover products made just for you</div>', unsafe_allow_html=True)

st.write(
    """
    Create your account to receive personalized recommendations, exclusive discounts, and tailored shopping experiences.
    """
)

st.markdown("### Ready to begin?")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("✨ Create your account"):
        st.switch_page("pages/account_creation.py")

