import streamlit as st

# 페이지 제목
st.title("🎵 오늘의 기분에 맞는 노래 추천")

# 기분 리스트
moods = ["행복 😄", "슬픔 😢", "설렘 💕", "화남 😡", "차분함 😌"]

# 기분별 노래 추천 데이터
songs = {
    "행복 😄": [
        {"title": "Happy", "artist": "Pharrell Williams", "link": "https://youtu.be/ZbZSe6N_BXs"},
        {"title": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "link": "https://youtu.be/OPf0YbXqDm0"}
    ],
    "슬픔 😢": [
        {"title": "Someone Like You", "artist": "Adele", "link": "https://youtu.be/hLQl3WQQoQ0"},
        {"title": "Fix You", "artist": "Coldplay", "link": "https://youtu.be/k4V3Mo61fJM"}
    ],
    "설렘 💕": [
        {"title": "Lover", "artist": "Taylor Swift", "link": "https://youtu.be/-BjZmE2gtdo"},
        {"title": "Adore You", "artist": "Harry Styles", "link": "https://youtu.be/V2hlQkVJZhE"}
    ],
    "화남 😡": [
        {"title": "Smells Like Teen Spirit", "artist": "Nirvana", "link": "https://youtu.be/hTWKbfoikeg"},
        {"title": "Rap God", "artist": "Eminem", "link": "https://youtu.be/XbGs_qK2PQA"}
    ],
    "차분함 😌": [
        {"title": "Weightless", "artist": "Marconi Union", "link": "https://youtu.be/UfcAVejslrU"},
        {"title": "River Flows in You", "artist": "Yiruma", "link": "https://youtu.be/7maJOI3QMu0"}
    ]
}

# 사용자 기분 선택
mood = st.selectbox("오늘 기분은 어떤가요?", moods)

# 추천 버튼
if st.button("노래 추천 받기"):
    selected_songs = songs[mood]
    for song in selected_songs:
        st.markdown(f"**{song['title']}** - {song['artist']} [▶️ 듣기]({song['link']})")

