import streamlit as st
import random

st.set_page_config(page_title="🎵 기분별 노래 추천", layout="wide")

# 감정 리스트
emotions = ["😊 기분 좋을 때", "😢 슬플 때", "💓 설렐 때", "😡 화날 때", "🍵 차분할 때"]

# 노래 데이터 (K-POP + POP)
songs = {
    "😊 기분 좋을 때": [
        ("NewJeans - Super Shy", "https://youtu.be/ArmDp-zijuc"),
        ("Red Velvet - Red Flavor", "https://youtu.be/WyiIGEHQP8o"),
        ("Bruno Mars - Treasure", "https://youtu.be/nPvuNsRccVw"),
        ("Dua Lipa - Don't Start Now", "https://youtu.be/oygrmJFKYZY"),
        ("SEVENTEEN - Very Nice", "https://youtu.be/cMNw9ianE9M"),
        ("Pharrell Williams - Happy", "https://youtu.be/ZbZSe6N_BXs"),
    ],
    "😢 슬플 때": [
        ("Adele - Someone Like You", "https://youtu.be/hLQl3WQQoQ0"),
        ("IU - 밤편지", "https://youtu.be/BzYnNdJhZQw"),
        ("Baekhyun - UN Village", "https://youtu.be/-mBge5RzxFg"),
        ("Billie Eilish - lovely", "https://youtu.be/V1Pl8CzNzCw"),
        ("Paul Kim - 모든 날, 모든 순간", "https://youtu.be/OMgPQwr2z-k"),
        ("Sam Smith - Too Good At Goodbyes", "https://youtu.be/J_ub7Etch2U"),
    ],
    "💓 설렐 때": [
        ("Taylor Swift - Love Story", "https://youtu.be/8xg3vE8Ie_E"),
        ("IVE - LOVE DIVE", "https://youtu.be/Y8JFxS1HlDo"),
        ("Justin Bieber - Baby", "https://youtu.be/kffacxfA7G4"),
        ("TWICE - What is Love?", "https://youtu.be/i0p1bmr0EmE"),
        ("BTS - Boy With Luv", "https://youtu.be/XsX3ATc3FbA"),
        ("Shawn Mendes - There's Nothing Holdin’ Me Back", "https://youtu.be/dT2owtxkU8k"),
    ],
    "😡 화날 때": [
        ("Eminem - Lose Yourself", "https://youtu.be/_Yhyp-_hX2s"),
        ("BLACKPINK - Kill This Love", "https://youtu.be/2S24-y0Ij3Y"),
        ("ITZY - WANNABE", "https://youtu.be/fE2h3lGlOsk"),
        ("Linkin Park - Numb", "https://youtu.be/kXYiU_JCYtU"),
        ("Doja Cat - Boss Bitch", "https://youtu.be/jQK7JbL0wU4"),
        ("Stray Kids - Maniac", "https://youtu.be/OvioeS1ZZ7o"),
    ],
    "🍵 차분할 때": [
        ("Dean - Instagram", "https://youtu.be/wKyMIrBClYw"),
        ("Lauv - I Like Me Better", "https://youtu.be/BcqxLCWn-CE"),
        ("IU - Palette", "https://youtu.be/d9IxdwEFk1c"),
        ("Crush - 잊을만하면", "https://youtu.be/_eeMdzKu5iU"),
        ("Ed Sheeran - Perfect", "https://youtu.be/2Vv-BfVoq4g"),
        ("Sam Smith - Stay With Me", "https://youtu.be=pB-5XG-DbAA"),
    ],
}

# 제목
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🎶 오늘의 기분별 노래 추천 🎶</h1>", unsafe_allow_html=True)

# 감정 선택
emotion = st.selectbox("👉 지금 기분을 골라주세요!", emotions)

# 추천 버튼
if st.button("🌟 노래 추천받기 🌟"):
    st.markdown(f"<h3 style='text-align: center;'>당신의 기분에 맞는 노래 추천 리스트 💖</h3>", unsafe_allow_html=True)

    # 노래 5개 랜덤 추출
    recommended = random.sample(songs[emotion], 5)

    # 카드 스타일 추천 표시
    for title, link in recommended:
        st.markdown(
            f"""
            <div style='
                background-color:#FFF0F5;
                border-radius:15px;
                padding:15px;
                margin:10px 0;
                box-shadow:2px 2px 8px rgba(0,0,0,0.1);
                font-size:18px;
            '>
                🎧 <b>{title}</b><br>
                👉 <a href="{link}" target="_blank">유튜브에서 듣기</a>
            </div>
            """,
            unsafe_allow_html=True
        )
