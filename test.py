import streamlit as st
import random

st.set_page_config(page_title="Mood Music Recommender", page_icon="🎧", layout="wide")

st.title("🎶 기분 따라 노래 추천 🎶")
st.write("기분에 맞는 노래를 랜덤으로 추천해드려요! 💖")

# 감정 리스트
moods = ["😊 기분 좋을 때", "😢 슬플 때", "💓 설렐 때", "😡 화날 때", "🍵 차분할 때"]

# 감정 선택 (드롭다운)
selected_mood = st.selectbox("👉 지금 당신의 기분은?", moods)

# 감정별 노래 리스트
songs = {
    "😊 기분 좋을 때": [
        "K-POP: NewJeans - Hype Boy", "K-POP: IVE - I AM", "K-POP: ITZY - DALLA DALLA", 
        "POP: Pharrell Williams - Happy", "POP: Katy Perry - Firework", 
        "POP: Dua Lipa - Don’t Start Now", "K-POP: BTS - Dynamite",
        "K-POP: SEVENTEEN - Very Nice", "POP: Justin Timberlake - Can’t Stop The Feeling"
    ],
    "😢 슬플 때": [
        "K-POP: AKMU - 어떻게 이별까지 사랑하겠어", "K-POP: 태연 - Fine", "K-POP: 백현 - UN Village",
        "POP: Adele - Someone Like You", "POP: Lewis Capaldi - Someone You Loved", 
        "POP: Sam Smith - Too Good At Goodbyes", "K-POP: IU - 밤편지",
        "K-POP: 폴킴 - 모든 날, 모든 순간", "POP: Coldplay - Fix You"
    ],
    "💓 설렐 때": [
        "K-POP: TWICE - What is Love?", "K-POP: Red Velvet - Ice Cream Cake", "K-POP: 아이유 - 금요일에 만나요",
        "POP: Taylor Swift - Lover", "POP: Carly Rae Jepsen - Call Me Maybe", 
        "POP: Bruno Mars - Just The Way You Are", "K-POP: 오마이걸 - Dun Dun Dance",
        "K-POP: 세븐틴 - Pretty U", "POP: Shawn Mendes - Senorita"
    ],
    "😡 화날 때": [
        "K-POP: CL - The Baddest Female", "K-POP: BLACKPINK - Kill This Love", "K-POP: BTS - MIC Drop",
        "POP: Billie Eilish - Bad Guy", "POP: Eminem - Lose Yourself", 
        "POP: Linkin Park - Numb", "K-POP: ITZY - WANNABE",
        "K-POP: Jessi - NUNU NANA", "POP: Rage Against The Machine - Killing In The Name"
    ],
    "🍵 차분할 때": [
        "K-POP: 백예린 - 그건 아마 우리의 잘못은 아닐 거야", "K-POP: 헤이즈 - 비도 오고 그래서", "K-POP: 아이유 - 무릎",
        "POP: Billie Eilish - Ocean Eyes", "POP: Ed Sheeran - Perfect", 
        "POP: Norah Jones - Don’t Know Why", "K-POP: 정승환 - 이 바보야",
        "K-POP: 10cm - 사랑은 은하수 다방에서", "POP: John Mayer - Gravity"
    ]
}

if st.button("🎧 노래 추천받기"):
    st.subheader(f"{selected_mood} 들으면 좋은 노래 💿")
    recommended = random.sample(songs[selected_mood], 5)  # 랜덤 5곡
    for idx, song in enumerate(recommended, 1):
        st.write(f"{idx}. {song}")
