import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="Mood Music 🎶", page_icon="🎵", layout="centered")

# CSS로 귀엽게 스타일 적용
st.markdown("""
<style>
body {
    background-color: #fffafc;
}
h1 {
    color: #ff6699;
    text-align: center;
    font-family: 'Comic Sans MS', cursive;
}
.stButton>button {
    background-color: #ffb6c1;
    color: white;
    border-radius: 20px;
    padding: 10px 20px;
    border: none;
    font-size: 16px;
}
.stButton>button:hover {
    background-color: #ff8da1;
}
.song-card {
    background-color: white;
    border-radius: 15px;
    padding: 15px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    margin: 10px 0;
}
.song-title {
    font-size: 18px;
    font-weight: bold;
    color: #ff6699;
}
.song-artist {
    font-size: 14px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# 페이지 제목
st.title("🎵 Mood Music - 기분별 노래 추천 🎶")

# 기분 리스트 & 노래 데이터
moods = {
    "😄 행복": [
        {"title": "Happy", "artist": "Pharrell Williams", "link": "https://youtu.be/ZbZSe6N_BXs"},
        {"title": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "link": "https://youtu.be/OPf0YbXqDm0"}
    ],
    "😢 슬픔": [
        {"title": "Someone Like You", "artist": "Adele", "link": "https://youtu.be/hLQl3WQQoQ0"},
        {"title": "Fix You", "artist": "Coldplay", "link": "https://youtu.be/k4V3Mo61fJM"}
    ],
    "💕 설렘": [
        {"title": "Lover", "artist": "Taylor Swift", "link": "https://youtu.be/-BjZmE2gtdo"},
        {"title": "Adore You", "artist": "Harry Styles", "link": "https://youtu.be/V2hlQkVJZhE"}
    ],
    "😡 화남": [
        {"title": "Smells Like Teen Spirit", "artist": "Nirvana", "link": "https://youtu.be/hTWKbfoikeg"},
        {"title": "Rap God", "artist": "Eminem", "link": "https://youtu.be/XbGs_qK2PQA"}
    ],
    "😌 차분함": [
        {"title": "Weightless", "artist": "Marconi Union", "link": "https://youtu.be/UfcAVejslrU"},
        {"title": "River Flows in You", "artist": "Yiruma", "link": "https://youtu.be/7maJOI3QMu0"}
    ]
}

# 기분 선택
mood = st.selectbox("💖 오늘 기분을 선택하세요!", list(moods.keys()))

# 추천 버튼
if st.button("🌟 노래 추천 받기 🌟"):
    selected_song = random.choice(moods[mood])
    st.markdown(
        f"""
        <div class="song-card">
            <div class="song-title">{selected_song['title']}</div>
            <div class="song-artist">{selected_song['artist']}</div>
            <a href="{selected_song['link']}" target="_blank">🎧 듣기</a>
        </div>
        """,
        unsafe_allow_html=True
    )
