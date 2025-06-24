import streamlit as st
from PIL import Image

# Load the profile picture
pfp = Image.open("pfp.jpg")  # Update the path to Ayesha's image

# Inject custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(to bottom right, #fdf2f8, #fff0f5);
        color: #333;
    }

    .main {
        padding: 2rem 1rem;
    }

    h1 {
        color: #c9184a;
        text-align: center;
        font-size: 2.8rem;
        margin-bottom: 0.5em;
    }

    .empower-card {
        background: #fff;
        padding: 2.5rem 2rem;
        margin-top: 2rem;
        border-radius: 20px;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
        text-align: center;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }

    .pfp-img {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        object-fit: cover;
        margin-bottom: 1rem;
        border: 4px solid #c9184a;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }

    .empower-card p {
        font-size: 1.2rem;
        line-height: 1.6;
    }

    .hadith {
        background: #f8f9fa;
        border-left: 6px solid #c9184a;
        margin: 2rem auto;
        padding: 1rem 1.5rem;
        font-style: italic;
        max-width: 600px;
        color: #555;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border-radius: 12px;
    }

    .footer {
        text-align: center;
        margin-top: 3rem;
        font-size: 0.9rem;
        color: #999;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>🌹 To My Beloved Friend Ayesha 🌸</h1>", unsafe_allow_html=True)

# Profile Picture
st.markdown('<div style="text-align:center;">', unsafe_allow_html=True)
st.image(pfp, caption="", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Empowerment Message
st.markdown("""
    <div class="empower-card">
        <p><strong>Dear Ayesha,</strong></p>
        <p>You are a soul of immense strength, a heart of unmatched kindness, and a light that no darkness can dim.</p>
        <p>Even in the shadows of hardship, you’ve held on with grace — and that is a beauty no one can ever take from you.</p>
        <p>I pray that Allah fills your days with peace, heals every wound, and surrounds you with people who truly value your heart.</p>
        <p><strong>I love you, my beloved friend.</strong> 💖</p>
    </div>
""", unsafe_allow_html=True)

# Hadith Section
st.markdown("""
    <div class="hadith">
        The Prophet ﷺ said:<br>
        <em>“Verily, with hardship comes ease.”</em><br>
        — *Qur’an 94:6*
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">With deep care and love 💕 — Talha</div>', unsafe_allow_html=True)
