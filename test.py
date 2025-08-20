import streamlit as st
import random

st.set_page_config(page_title="Mood Song Recommender", page_icon="🎶", layout="wide")

st.title("🌸 기분에 따라 노래 추천 🎧")
st.write("당신의 기분을 선택하면 딱 맞는 노래를 랜덤으로 추천해드려요! 💕")

# 기분 리스트
moods = ["😊 기분 좋을 때", "😢 슬플 때", "💓 설렐 때", "😡 화날 때", "🌙 차분할 때"]

# 선택창
mood = st.selectbox("👉 지금 기분을 골라주세요!", moods)

# 노래 데이터베이스 (앨범커버 + 유튜브링크)
songs = {
    "😊 기분 좋을 때": [
        {"title": "BTS - Dynamite", "img": "https://i.scdn.co/image/ab67616d0000b2738b3e8ed4a47d18495df90c29", "url": "https://youtu.be/gdZLi9oWNZg"},
        {"title": "Red Velvet - Red Flavor", "img": "https://i.scdn.co/image/ab67616d0000b273648efa7a4182a26c6f9f3ebf", "url": "https://youtu.be/WyiIGEHQP8o"},
        {"title": "Pharrell Williams - Happy", "img": "https://i.scdn.co/image/ab67616d0000b2733b3c8a5e0c5d0ff9a9a90e02", "url": "https://youtu.be/ZbZSe6N_BXs"},
        {"title": "TWICE - What is Love?", "img": "https://i.scdn.co/image/ab67616d0000b273a1e1f98d342fcf0a3ee9bb11", "url": "https://youtu.be/i0p1bmr0EmE"},
        {"title": "Bruno Mars - 24K Magic", "img": "https://i.scdn.co/image/ab67616d0000b273fa1f3a1962fa2a343b3b0a06", "url": "https://youtu.be/UqyT8IEBkvY"},
    ],
    "😢 슬플 때": [
        {"title": "Adele - Someone Like You", "img": "https://i.scdn.co/image/ab67616d0000b273d0c7e3f4f3d04c9a1b3e0b79", "url": "https://youtu.be/hLQl3WQQoQ0"},
        {"title": "AKMU - 어떻게 이별까지 사랑하겠어", "img": "https://i.scdn.co/image/ab67616d0000b273bcd2f4d3f37c0c2f1f4d21b5", "url": "https://youtu.be/mv2R5Fp92zQ"},
        {"title": "Billie Eilish - when the party's over", "img": "https://i.scdn.co/image/ab67616d0000b273f8bb9a8e5d0c3573e70c6e1f", "url": "https://youtu.be/pbMwTqkKSps"},
        {"title": "IU - 밤편지", "img": "https://i.scdn.co/image/ab67616d0000b27353c585dd49007f4619052a9e", "url": "https://youtu.be/BzYnNdJhZQw"},
        {"title": "Coldplay - Fix You", "img": "https://i.scdn.co/image/ab67616d0000b2735f6f9f64f2a7af38d5c4b8b2", "url": "https://youtu.be/k4V3Mo61fJM"},
    ],
    "💓 설렐 때": [
        {"title": "SEVENTEEN - Pretty U", "img": "https://i.scdn.co/image/ab67616d0000b273baf2231f1d6b4a5905a9d3f6", "url": "https://youtu.be/J-wFp43XOrA"},
        {"title": "Taylor Swift - Love Story", "img": "https://i.scdn.co/image/ab67616d0000b2732b93e3d1d40f4bc69d5c6f1d", "url": "https://youtu.be/8xg3vE8Ie_E"},
        {"title": "TWICE - Cheer Up", "img": "https://i.scdn.co/image/ab67616d0000b2732cc5a2ddcaad419acf680cf7", "url": "https://youtu.be/c7rCyll5AeY"},
        {"title": "Justin Bieber - Baby", "img": "https://i.scdn.co/image/ab67616d0000b273267f68d05ac9f94e5b0e8d07", "url": "https://youtu.be/kffacxfA7G4"},
        {"title": "IVE - Love Dive", "img": "https://i.scdn.co/image/ab67616d0000b27380f9f9ce59efc2f2e81c4e4f", "url": "https://youtu.be/Y8JFxS1HlDo"},
    ],
    "😡 화날 때": [
        {"title": "Eminem - Lose Yourself", "img": "https://i.scdn.co/image/ab67616d0000b27360eaf6d3eab1ddf1b0b0b812", "url": "https://youtu.be/_Yhyp-_hX2s"},
        {"title": "Stray Kids - God's Menu", "img": "https://i.scdn.co/image/ab67616d0000b273e2e2e86e5b78a1e1c4e3b9f5", "url": "https://youtu.be/TQTlCHxyuu8"},
        {"title": "Linkin Park - Numb", "img": "https://i.scdn.co/image/ab67616d0000b273a4e6f1b1f94c3b7f7d98b5a8", "url": "https://youtu.be/kXYiU_JCYtU"},
        {"title": "BLACKPINK - Kill This Love", "img": "https://i.scdn.co/image/ab67616d0000b273ccf7ea50ccaa43d562e8d7aa", "url": "https://youtu.be/2S24-y0Ij3Y"},
        {"title": "Imagine Dragons - Believer", "img": "https://i.scdn.co/image/ab67616d0000b27357f6a184044c10f2e0cfdce9", "url": "https://youtu.be/7wtfhZwyrcc"},
    ],
    "🌙 차분할 때": [
        {"title": "Lauv - I Like Me Better", "img": "https://i.scdn.co/image/ab67616d0000b273a21658d2b96c6f6d5e2a8d9e", "url": "https://youtu.be/BcqxLCWn-CE"},
        {"title": "백예린 - Square", "img": "https://i.scdn.co/image/ab67616d0000b273e6a28a3f0f6f964c563e1ee2", "url": "https://youtu.be/hZmoMyFXDoI"},
        {"title": "Ed Sheeran - Perfect", "img": "https://i.scdn.co/image/ab67616d0000b2737a3b293b2b1c06e453997a79", "url": "https://youtu.be/2Vv-BfVoq4g"},
        {"title": "EXO - Universe", "img": "https://i.scdn.co/image/ab67616d0000b27384ad5e72982f90217c4f39f8", "url": "https://youtu.be/Brbtm88vkA0"},
        {"title": "John Legend - All of Me", "img": "https://i.scdn.co/image/ab67616d0000b273c07f7a6e9f2a1b3f5e2d73b2", "url": "https://youtu.be/450p7goxZqg"},
    ]
}

# 버튼 클릭 시 추천
if st.button("🎁 노래 추천받기"):
    selected_songs = random.sample(songs[mood], 5)
    cols = st.columns(5)
    for idx, song in enumerate(selected_songs):
        with cols[idx]:
            st.image(song["img"], use_container_width=True)
            st.markdown(f"**{song['title']}**")
            st.markdown(f"[▶️ 듣기]({song['url']})")
