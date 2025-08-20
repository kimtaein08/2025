import streamlit as st
import random

st.set_page_config(page_title="Mood-based Music Recommender", layout="wide")

st.title("🎧 기분에 따라 노래 추천해주는 사이트 🎶")
st.markdown("오늘 기분은 어때? 아래에서 골라봐! 😆🥲🤩😌🔥")

# -----------------------
# 기분 선택 UI (이모지 버튼 스타일)
# -----------------------
moods = {
    "행복해요 😆": "happy",
    "슬퍼요 🥲": "sad",
    "신나요 🤩": "excited",
    "차분해요 😌": "calm",
    "열정적이에요 🔥": "energetic"
}

selected_mood = st.session_state.get("selected_mood", None)

cols = st.columns(len(moods))
for idx, (emoji_label, mood_value) in enumerate(moods.items()):
    if cols[idx].button(emoji_label):
        st.session_state.selected_mood = mood_value
        selected_mood = mood_value

# -----------------------
# 노래 데이터베이스
# -----------------------
songs = {
    "happy": [
        "BTS - Dynamite", "Red Velvet - Red Flavor", "Bruno Mars - Treasure",
        "TWICE - Cheer Up", "Pharrell Williams - Happy",
        "SEVENTEEN - Very Nice", "Katy Perry - Firework",
        "IVE - I AM", "Taylor Swift - Shake It Off", "BLACKPINK - As If It’s Your Last"
    ],
    "sad": [
        "Adele - Someone Like You", "IU - Love Poem", "Billie Eilish - everything i wanted",
        "Baekhyun - UN Village", "Sam Smith - Too Good at Goodbyes",
        "Rosé - Gone", "Dean - instagram", "Coldplay - Fix You",
        "Heize - You, Clouds, Rain", "Justin Bieber - Ghost"
    ],
    "excited": [
        "Stray Kids - God’s Menu", "BLACKPINK - DDU-DU DDU-DU", "Imagine Dragons - Believer",
        "ITZY - Wannabe", "PSY - Gangnam Style",
        "aespa - Next Level", "EXO - Power", "Beyoncé - Run the World (Girls)",
        "NCT 127 - Kick It", "Lady Gaga - Poker Face"
    ],
    "calm": [
        "Paul Kim - Every Day, Every Moment", "AKMU - Melted", "Ed Sheeran - Perfect",
        "Taeyeon - Fine", "Lauv - I Like Me Better",
        "Baek Yerin - Square", "Shawn Mendes - In My Blood (Acoustic)",
        "IU - Through the Night", "John Legend - All of Me", "DAY6 - You Were Beautiful"
    ],
    "energetic": [
        "TWICE - Fancy", "BTS - MIC Drop", "Dua Lipa - Don’t Start Now",
        "SEVENTEEN - HIT", "BLACKPINK - BOOMBAYAH",
        "Zedd - Clarity", "NMIXX - O.O", "Calvin Harris - Summer",
        "BIGBANG - Bang Bang Bang", "David Guetta - Titanium"
    ]
}

# -----------------------
# 노래 추천
# -----------------------
if selected_mood:
    st.subheader("✨ 노래 추천 리스트 ✨")
    if st.button("노래 추천받기 🎶"):
        recommended = random.sample(songs[selected_mood], 5)
        for idx, song in enumerate(recommended, 1):
            st.markdown(f"**{idx}. {song}**")
