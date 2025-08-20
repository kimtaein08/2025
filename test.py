import streamlit as st
import random

st.set_page_config(page_title="Mood Playlist 🎶", layout="wide")

# CSS로 배경 꾸미기
page_bg = """
<style>
.stApp {
    background-image: url("https://i.pinimg.com/736x/ed/f5/3a/edf53a24ab4d142e5075b83175f66338.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
.song-card {
    background: rgba(255, 255, 255, 0.8);
    border-radius: 20px;
    padding: 20px;
    margin: 10px;
    box-shadow: 3px 3px 10px rgba(0,0,0,0.2);
    text-align: center;
    font-size: 18px;
}
.song-title {
    font-weight: bold;
    font-size: 20px;
    color: #ff4b6e;
}
.song-link {
    font-size: 16px;
    color: #3366cc;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

st.title("🌈 Mood Playlist Generator 🎶")
st.write("오늘 너의 기분에 맞는 노래를 랜덤으로 추천해줄게!")

# 감정 선택
mood = st.radio(
    "지금 기분은 어때? 🐰",
    ["기분 좋을 때", "슬플 때", "설렐 때", "화날 때", "차분할 때"]
)

# 노래 데이터 (K-POP / Pop / J-POP 섞기)
songs = {
    "기분 좋을 때": [
        {"title": "New Jeans - Super Shy (K-POP)", "url": "https://youtu.be/ArmDp-zijuc"},
        {"title": "Pharrell Williams - Happy (Pop)", "url": "https://youtu.be/ZbZSe6N_BXs"},
        {"title": "YOASOBI - Idol (J-POP)", "url": "https://youtu.be/z2X1dT7B7hQ"},
    ],
    "슬플 때": [
        {"title": "아이유 - 밤편지 (K-POP)", "url": "https://youtu.be/BzYnNdJhZQw"},
        {"title": "Billie Eilish - when the party's over (Pop)", "url": "https://youtu.be/pbMwTqkKSps"},
        {"title": "Aimer - Ref:rain (J-POP)", "url": "https://youtu.be/2QxCz6UxeXU"},
    ],
    "설렐 때": [
        {"title": "세븐틴 - Very Nice (K-POP)", "url": "https://youtu.be/cEZx9hS6-qU"},
        {"title": "Carly Rae Jepsen - Call Me Maybe (Pop)", "url": "https://youtu.be/fWNaR-rxAic"},
        {"title": "LiSA - Gurenge (J-POP)", "url": "https://youtu.be/CwkzK-F0Y00"},
    ],
    "화날 때": [
        {"title": "방탄소년단 - MIC Drop (K-POP)", "url": "https://youtu.be/kTlv5_Bs8aw"},
        {"title": "Linkin Park - Numb (Pop)", "url": "https://youtu.be/kXYiU_JCYtU"},
        {"title": "UVERworld - Core Pride (J-POP)", "url": "https://youtu.be/t0D2az4w93A"},
    ],
    "차분할 때": [
        {"title": "태연 - 사계 (K-POP)", "url": "https://youtu.be/4HG_CJZYX6A"},
        {"title": "Coldplay - Fix You (Pop)", "url": "https://youtu.be/k4V3Mo61fJM"},
        {"title": "Radwimps - Sparkle (J-POP)", "url": "https://youtu.be/Mt1bPzSGTf0"},
    ],
}

if st.button("✨ 나만의 플레이리스트 추천받기 ✨"):
    selected_songs = random.sample(songs[mood], k=3)  # 랜덤 3곡
    st.subheader(f"☁️ 오늘의 [{mood}] 플레이리스트")
    for song in selected_songs:
        st.markdown(
            f"""
            <div class="song-card">
                <div class="song-title">🎵 {song['title']}</div>
                <a class="song-link" href="{song['url']}" target="_blank">🔗 듣기</a>
            </div>
            """,
            unsafe_allow_html=True
        )
