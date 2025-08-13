import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="Mood Music 🎶", page_icon="🎵", layout="wide")

# CSS 스타일
st.markdown("""
<style>
body {
    background-color: #fffafc;
}
h1 {
    color: #ff6699;
    text-align: center;
    font-family: 'Comic Sans MS', cursive;
    font-size: 48px;
    margin-bottom: 20px;
}
.stSelectbox label {
    font-size: 22px;
    color: #ff6699;
    font-weight: bold;
}
.stSelectbox div[data-baseweb="select"] {
    font-size: 20px;
}
.stButton>button {
    background-color: #ffb6c1;
    color: white;
    border-radius: 25px;
    padding: 15px 30px;
    border: none;
    font-size: 20px;
    width: 100%;
}
.stButton>button:hover {
    background-color: #ff8da1;
}
.song-card {
    background-color: white;
    border-radius: 20px;
    padding: 25px;
    box-shadow: 4px 4px 15px rgba(0,0,0,0.15);
    margin: 15px 0;
    font-size: 20px;
    width: 100%;
}
.song-title {
    font-size: 24px;
    font-weight: bold;
    color: #ff6699;
}
.song-artist {
    font-size: 18px;
    color: gray;
}
.song-link a {
    font-size: 18px;
    color: #ff6699;
    font-weight: bold;
    text-decoration: none;
}
.song-link a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# 페이지 제목
st.title("🎵 Mood Music - 기분별 노래 추천 🎶")

# 기분별 노래 데이터 (팝송 + 케이팝)
moods = {
    "😄 행복": [
        {"title": "Happy", "artist": "Pharrell Williams", "link": "https://youtu.be/ZbZSe6N_BXs"},
        {"title": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "link": "https://youtu.be/OPf0YbXqDm0"},
        {"title": "Dynamite", "artist": "BTS", "link": "https://youtu.be/gdZLi9oWNZg"},
        {"title": "Cheer Up", "artist": "TWICE", "link": "https://youtu.be/c7rCyll5AeY"},
        {"title": "As It Was", "artist": "Harry Styles", "link": "https://youtu.be/H5v3kku4y6Q"},
        {"title": "LOVE DIVE", "artist": "IVE", "link": "https://youtu.be/Y8JFxS1HlDo"}
    ],
    "😢 슬픔": [
        {"title": "Someone Like You", "artist": "Adele", "link": "https://youtu.be/hLQl3WQQoQ0"},
        {"title": "Fix You", "artist": "Coldplay", "link": "https://youtu.be/k4V3Mo61fJM"},
        {"title": "Love Poem", "artist": "아이유 (IU)", "link": "https://youtu.be/0-q1KafFCLU"},
        {"title": "Lonely", "artist": "2NE1", "link": "https://youtu.be/8TS0CtgLtM0"},
        {"title": "When I Was Your Man", "artist": "Bruno Mars", "link": "https://youtu.be/ekzHIouo8Q4"},
        {"title": "그때 그 순간 그대로", "artist": "너드커넥션", "link": "https://youtu.be/n5DGuzGT8-E"}
    ],
    "💕 설렘": [
        {"title": "Lover", "artist": "Taylor Swift", "link": "https://youtu.be/-BjZmE2gtdo"},
        {"title": "Adore You", "artist": "Harry Styles", "link": "https://youtu.be/V2hlQkVJZhE"},
        {"title": "LOVE SCENARIO", "artist": "iKON", "link": "https://youtu.be/vecSVX1QYbQ"},
        {"title": "Love Me Like This", "artist": "NMIXX", "link": "https://youtu.be/Yi3ywxF2C9o"},
        {"title": "Just The Way You Are", "artist": "Bruno Mars", "link": "https://youtu.be/LjhCEhWiKXk"},
        {"title": "Candy", "artist": "NCT DREAM", "link": "https://youtu.be/FwmvPq1QhD0"}
    ],
    "😡 화남": [
        {"title": "Smells Like Teen Spirit", "artist": "Nirvana", "link": "https://youtu.be/hTWKbfoikeg"},
        {"title": "Rap God", "artist": "Eminem", "link": "https://youtu.be/XbGs_qK2PQA"},
        {"title": "Kill This Love", "artist": "BLACKPINK", "link": "https://youtu.be/2S24-y0Ij3Y"},
        {"title": "MIC Drop", "artist": "BTS", "link": "https://youtu.be/kTlv5_Bs8aw"},
        {"title": "Believer", "artist": "Imagine Dragons", "link": "https://youtu.be/7wtfhZwyrcc"},
        {"title": "God's Menu", "artist": "Stray Kids", "link": "https://youtu.be/TQTlCHxyuu8"}
    ],
    "😌 차분함": [
        {"title": "Weightless", "artist": "Marconi Union", "link": "https://youtu.be/UfcAVejslrU"},
        {"title": "River Flows in You", "artist": "Yiruma", "link": "https://youtu.be/7maJOI3QMu0"},
        {"title": "밤편지", "artist": "아이유 (IU)", "link": "https://youtu.be/BzYnNdJhZQw"},
        {"title": "All of Me", "artist": "John Legend", "link": "https://youtu.be/450p7goxZqg"},
        {"title": "Through the Night", "artist": "아이유 (IU)", "link": "https://youtu.be/BzYnNdJhZQw"},
        {"title": "이제 나만 믿어요", "artist": "임영웅", "link": "https://youtu.be/7JjI_l68gUg"}
    ]
}

# 기분 선택
mood = st.selectbox("💖 오늘 기분을 선택하세요!", list(moods.keys()))

# 추천곡 저장용 세션 상태 초기화
if "recommended_songs" not in st.session_state:
    st.session_state.recommended_songs = []

# 추천 버튼
if st.button("🌟 노래 추천 받기 🌟"):
    st.session_state.recommended_songs = random.sample(moods[mood], 5)  # 매번 새로운 곡 5개 뽑기

# 추천곡 출력
for song in st.session_state.recommended_songs:
    st.markdown(
        f"""
        <div class="song-card">
            <div class="song-title">{song['title']}</div>
            <div class="song-artist">{song['artist']}</div>
            <div class="song-link"><a href="{song['link']}" target="_blank">🎧 듣기</a></div>
        </div>
        """,
        unsafe_allow_html=True
    )
