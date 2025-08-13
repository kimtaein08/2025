import streamlit as st
import random

st.set_page_config(page_title="Mood Song Recommender 🎵", layout="wide")

# 제목
st.markdown(
    "<h1 style='text-align: center; color: #ff6f61;'>🎶 기분별 노래 추천 🎶</h1>",
    unsafe_allow_html=True
)
st.write(" ")

# 기분별 노래 데이터 (K-pop + Pop)
songs = {
    "😊 기분 좋아": [
        "BTS - Dynamite",
        "Red Velvet - Feel My Rhythm",
        "Bruno Mars - Treasure",
        "TWICE - Cheer Up",
        "Pharrell Williams - Happy",
        "IVE - Love Dive",
        "Taylor Swift - Shake It Off",
        "SEVENTEEN - Very Nice",
        "Doja Cat - Say So",
        "BLACKPINK - As If It's Your Last"
    ],
    "😢 슬플 때": [
        "Adele - Someone Like You",
        "Baekhyun - UN Village",
        "Billie Eilish - everything i wanted",
        "IU - Through the Night",
        "Coldplay - Fix You",
        "Paul Kim - Me After You",
        "Sam Smith - Too Good at Goodbyes",
        "AKMU - How can I love the heartbreak, you're the one I love",
        "Ed Sheeran - Photograph",
        "Heize - You, Clouds, Rain"
    ],
    "🔥 신나고 싶을 때": [
        "Stray Kids - God's Menu",
        "PSY - Gangnam Style",
        "Dua Lipa - Don't Start Now",
        "ZICO - Any Song",
        "BLACKPINK - DDU-DU DDU-DU",
        "ITZY - Wannabe",
        "Cardi B - I Like It",
        "Sunmi - Gashina",
        "Charlie Puth - Attention",
        "Jessi - NUNU NANA"
    ],
    "💤 차분하고 싶을 때": [
        "IU - Palette",
        "Lauv - I Like Me Better",
        "BTS - Blue & Grey",
        "DEAN - Instagram",
        "John Mayer - Gravity",
        "SHINee - View",
        "Billie Eilish - Ocean Eyes",
        "Baek Yerin - Square",
        "Coldplay - The Scientist",
        "Paul Kim - Every Day, Every Moment"
    ],
    "💪 자신감 뿜뿜": [
        "BTS - MIC Drop",
        "ITZY - Not Shy",
        "Ariana Grande - 7 rings",
        "BLACKPINK - Kill This Love",
        "Beyoncé - Run the World (Girls)",
        "TWICE - I Can't Stop Me",
        "Jessie J - Domino",
        "MAMAMOO - HIP",
        "Taylor Swift - The Man",
        "2NE1 - I Am The Best"
    ]
}

# 기분 선택
mood = st.selectbox("💖 지금 기분을 선택해주세요:", list(songs.keys()))

# 버튼 클릭 시 랜덤 추천
if st.button("🎁 노래 추천받기"):
    selected_songs = random.sample(songs[mood], 5)

    st.markdown(
        f"<h3 style='text-align: center; color: #4CAF50;'>✨ {mood} 기분에 어울리는 노래 ✨</h3>",
        unsafe_allow_html=True
    )
    cols = st.columns(5)
    for i, song in enumerate(selected_songs):
        with cols[i]:
            st.markdown(
                f"<div style='padding:15px; background-color:#fff3cd; border-radius:15px; text-align:center; font-size:16px;'>{song}</div>",
                unsafe_allow_html=True
            )
