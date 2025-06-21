import streamlit as st
from PIL import Image

# Load the profile picture
pfp = Image.open("pfp.jpg")

# Inject professional custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(to bottom right, #fff0f3, #ffe4e9);
        color: #333;
    }

    .main {
        padding: 2rem 1rem;
    }

    h1 {
        color: #e63946;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 0.2em;
    }

    .birthday-card {
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
        border: 4px solid #e63946;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }

    .birthday-card p {
        font-size: 1.2rem;
        line-height: 1.6;
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
st.markdown("<h1>🎂 Happy Birthday Kiran! 🎉</h1>", unsafe_allow_html=True)

# Profile Picture
st.markdown('<div style="text-align:center;">', unsafe_allow_html=True)
st.image(pfp, caption="", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Birthday Message
st.markdown("""
    <div class="birthday-card">
        <p><strong>Dear Kiran,</strong></p>
        <p>Wishing you a day as beautiful and unforgettable as you are. May this year bring you endless happiness, success, and all the love your heart can hold.</p>
        <p>Here’s to glowing moments, sweet memories, and dreams fulfilled. You deserve the absolute best. 🎈</p>
        <p><strong>Happy Birthday!</strong> 💖</p>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Ordinary gift by 💐 Taru Saad</div>', unsafe_allow_html=True)
