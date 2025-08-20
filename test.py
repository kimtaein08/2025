import streamlit as st
import random

st.set_page_config(page_title="Mood Music Recommender", page_icon="🎶", layout="wide")

# 감정별 노래 데이터 (Pop + K-pop 다양하게 확장)
songs = {
    "😊 행복": [
        "BTS - Dynamite", "Red Velvet - Happiness", "Pharrell Williams - Happy",
        "세븐틴 - 아주 NICE", "Bruno Mars - 24K Magic", "아이유 - 좋은 날",
        "TWICE - Cheer Up", "Katy Perry - Firework", "Zico - Any Song", "ITZY - DALLA DALLA"
    ],
    "😢 슬픔": [
        "Adele - Someone Like You", "백현 - 두근거려 (Beautiful)", "Billie Eilish - when the party's over",
        "아이유 - 밤편지", "Coldplay - Fix You", "폴킴 - 모든 날, 모든 순간",
        "Sam Smith - Too Good at Goodbyes", "G-DRAGON - 무제(無題)", "김광석 - 이등병의 편지", "Taeyeon - Fine"
    ],
    "😡 화남": [
        "Eminem - Lose Yourself", "방탄소년단 - MIC Drop", "Linkin Park - Numb",
        "BLACKPINK - Kill This Love", "Stray Kids - God’s Menu", "Nirvana - Smells Like Teen Spirit",
        "이승윤 - 들려주고 싶었던", "Doja Cat - Boss Bitch", "TWICE - I CAN’T STOP ME", "EXO - Monster"
    ],
    "😌 차분": [
        "IU - Palette", "Lauv - I Like Me Better", "백예린 - Square", "Dean - instagram",
        "Ed Sheeran - Perfect", "폴킴 - 비", "Sam Smith - Stay With Me", 
        "BOL4 - 우주를 줄게", "Shawn Mendes - Wonder", "태연 - 그대라는 시"
    ],
    "🤩 신남": [
        "PSY - 강남스타일", "BIGBANG - Bang Bang Bang", "Kesha - Tik Tok",
        "TWICE - Dance The Night Away", "BTS - Idol", "Bruno Mars - Uptown Funk",
        "ITZY - Wannabe", "KARINA - Hot & Cold", "Lady Gaga - Just Dance", "SEVENTEEN - Super"
    ]
}

st.title("🎶 기분별 랜덤 노래 추천기 🎶")
st.markdown("✨ 지금 기분에 맞는 노래를 랜덤으로 추천해줄게요! ✨")

# 감정 선택
mood = st.radio(
    "지금 기분은 어떤가요? 😍",
    list(songs.keys()),
    horizontal=True
)

if st.button("🎵 노래 추천받기"):
    # 해당 감정에서 랜덤으로 5곡 뽑기
    recommended = random.sample(songs[mood], 5)
    
    st.subheader(f"{mood} 기분일 때 추천하는 노래 🎧")
    
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.markdown(f"""
            <div style='background-color:#fef6ff;
                        border-radius:15px;
                        padding:20px;
                        text-align:center;
                        box-shadow:2px 2px 8px rgba(0,0,0,0.1);'>
                <h3>🎵</h3>
                <p style='font-size:16px;'>{recommended[i]}</p>
            </div>
            """, unsafe_allow_html=True)
