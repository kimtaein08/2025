import streamlit as st
import random

st.set_page_config(page_title="노래 추천 앱", layout="wide")

st.title("🌟 기분에 맞는 랜덤 노래 추천기 🎶")
st.write("당신의 기분을 선택하면 K-POP, POP, J-POP에서 랜덤으로 노래 5곡을 추천해드려요! 💖")

# 감정 리스트
moods = ["😊 기분 좋을 때", "😢 슬플 때", "💓 설렐 때", "😡 화날 때", "🍵 차분할 때"]

# 카테고리별 노래 데이터
songs = {
    "K-POP": {
        "😊 기분 좋을 때": [
            ("IVE - I AM", "https://youtu.be/6ZUIwj3FgUY"),
            ("NewJeans - ETA", "https://youtu.be/jOTfBlKSQYY"),
            ("TWICE - What is Love?", "https://youtu.be/i0p1bmr0EmE"),
            ("SEVENTEEN - Super", "https://youtu.be/-GQg25oP0S4"),
            ("Red Velvet - Feel My Rhythm", "https://youtu.be/2tM1LFFxeKg")
        ],
        "😢 슬플 때": [
            ("BIGBANG - Still Life", "https://youtu.be/eN5mG_yMDiM"),
            ("Taeyeon - Fine", "https://youtu.be/iX-QaNzd-0Y"),
            ("AKMU - 어떻게 이별까지 사랑하겠어, 널 사랑하는 거지", "https://youtu.be/1jO2wSpAoxA"),
            ("IU - 밤편지", "https://youtu.be/BzYnNdJhZQw"),
            ("Baekhyun - UN Village", "https://youtu.be/tVV4h38wnMI")
        ],
        "💓 설렐 때": [
            ("STAYC - Teddy Bear", "https://youtu.be/pigQd3cu5TI"),
            ("OH MY GIRL - Dolphin", "https://youtu.be/_cOZq0G0FWY"),
            ("BTS - Butter", "https://youtu.be/WMweEpGlu_U"),
            ("GFRIEND - Me Gustas Tu", "https://youtu.be/YYHyAIFG3iI"),
            ("NewJeans - OMG", "https://youtu.be/sVTy_wmn5SU")
        ],
        "😡 화날 때": [
            ("ITZY - LOCO", "https://youtu.be/MjCZfZfucEc"),
            ("BLACKPINK - Kill This Love", "https://youtu.be/2S24-y0Ij3Y"),
            ("aespa - Savage", "https://youtu.be/WPdWvnAAurg"),
            ("2NE1 - I Am The Best", "https://youtu.be/j7_lSP8Vc3o"),
            ("LE SSERAFIM - ANTIFRAGILE", "https://youtu.be/pyf8cbqyfPs")
        ],
        "🍵 차분할 때": [
            ("IU - Palette", "https://youtu.be/d9IxdwEFk1c"),
            ("Heize - And July", "https://youtu.be/rMg2zz3Wgro"),
            ("Crush - 가끔", "https://youtu.be/2tTm_kW4V0I"),
            ("Paul Kim - 모든 날, 모든 순간", "https://youtu.be/cfwoQ1x2fYI"),
            ("AKMU - 작은 별", "https://youtu.be/0P4tYwtgZnM")
        ]
    },
    "POP": {
        "😊 기분 좋을 때": [
            ("Pharrell Williams - Happy", "https://youtu.be/ZbZSe6N_BXs"),
            ("Katy Perry - Firework", "https://youtu.be/QGJuMBdaqIw"),
            ("Justin Timberlake - CAN'T STOP THE FEELING!", "https://youtu.be/ru0K8uYEZWw"),
            ("Dua Lipa - Levitating", "https://youtu.be/TUVcZfQe-Kw"),
            ("Bruno Mars - Treasure", "https://youtu.be/nPvuNsRccVw")
        ],
        "😢 슬플 때": [
            ("Adele - Someone Like You", "https://youtu.be/hLQl3WQQoQ0"),
            ("Lewis Capaldi - Someone You Loved", "https://youtu.be/zABLecsR5UE"),
            ("Sam Smith - Stay With Me", "https://youtu.be/pB-5XG-DbAA"),
            ("Billie Eilish - when the party's over", "https://youtu.be/pbMwTqkKSps"),
            ("Coldplay - Fix You", "https://youtu.be/k4V3Mo61fJM")
        ],
        "💓 설렐 때": [
            ("Taylor Swift - Love Story", "https://youtu.be/8xg3vE8Ie_E"),
            ("Ed Sheeran - Perfect", "https://youtu.be/2Vv-BfVoq4g"),
            ("Shawn Mendes - There's Nothing Holdin' Me Back", "https://youtu.be/dT2owtxkU8k"),
            ("One Direction - What Makes You Beautiful", "https://youtu.be/QJO3ROT-A4E"),
            ("Carly Rae Jepsen - Call Me Maybe", "https://youtu.be/fWNaR-rxAic")
        ],
        "😡 화날 때": [
            ("Billie Eilish - bad guy", "https://youtu.be/DyDfgMOUjCI"),
            ("Linkin Park - Numb", "https://youtu.be/kXYiU_JCYtU"),
            ("Eminem - Lose Yourself", "https://youtu.be/_Yhyp-_hX2s"),
            ("Rihanna - Bitch Better Have My Money", "https://youtu.be/cggNqDAtJYU"),
            ("Demi Lovato - Sorry Not Sorry", "https://youtu.be/-MsvER1dpjM")
        ],
        "🍵 차분할 때": [
            ("Lauv - I Like Me Better", "https://youtu.be/BcqxLCWn-CE"),
            ("John Legend - All of Me", "https://youtu.be/450p7goxZqg"),
            ("Norah Jones - Don't Know Why", "https://youtu.be/tO4dxvguQDk"),
            ("Alicia Keys - If I Ain't Got You", "https://youtu.be/Ju8Hr50Ckwk"),
            ("Bruno Mars - Just The Way You Are", "https://youtu.be/LjhCEhWiKXk")
        ]
    },
    "J-POP": {
        "😊 기분 좋을 때": [
            ("Official HIGE DANDism - Pretender", "https://youtu.be/TQ8WlA2GXbk"),
            ("YOASOBI - アイドル", "https://youtu.be/z2XqK8wTg5c"),
            ("LiSA - Rising Hope", "https://youtu.be/fmI_Ndrxy14"),
            ("Perfume - FLASH", "https://youtu.be/q6T0wOMsNrI"),
            ("Aimer - Brave Shine", "https://youtu.be/JzOIo4UUl0w")
        ],
        "😢 슬플 때": [
            ("Aimer - Kataomoi", "https://youtu.be/d4Kp9-9N2VQ"),
            ("YOASOBI - もう少しだけ", "https://youtu.be/zfFQn06F1Sg"),
            ("RADWIMPS - 前前前世", "https://youtu.be/PDSkFeMVNFs"),
            ("YUI - Good-bye days", "https://youtu.be/T7YXpU2oqJg"),
            ("Ikimono Gakari - Blue Bird", "https://youtu.be/Tp0qhQja1HU")
        ],
        "💓 설렐 때": [
            ("YOASOBI - 夜に駆ける", "https://youtu.be/x8VYWazR5mE"),
            ("King & Prince - Cinderella Girl", "https://youtu.be/fFbkZpUEVtQ"),
            ("Aimyon - Marigold", "https://youtu.be/0xSiBpUdW4E"),
            ("Daichi Miura - EXCITE", "https://youtu.be/5sGOwFVUU0I"),
            ("Nogizaka46 - Influencer", "https://youtu.be/0I647GU3Jsc")
        ],
        "😡 화날 때": [
            ("LiSA - Gurenge", "https://youtu.be/CwkzK-F0Y00"),
            ("Eve - 廻廻奇譚", "https://youtu.be/1tk1pqwrOys"),
            ("UVERworld - Core Pride", "https://youtu.be/2-owvMPltiE"),
            ("Aimer - Zankyou Sanka", "https://youtu.be/Kl4Jd5qYoQo"),
            ("Ling Tosite Sigure - unravel", "https://youtu.be/7aMOurgDB-o")
        ],
        "🍵 차분할 때": [
            ("Spitz - 空も飛べるはず", "https://youtu.be/DnGdoEa1tPg"),
            ("Radwimps - Sparkle", "https://youtu.be/tQ9I5zvVQfM"),
            ("YOASOBI - Ano Yume o Nazotte", "https://youtu.be/sAuEeM_6zpk"),
            ("Aimer - Ref:rain", "https://youtu.be/Sw6Ck9xgY4s"),
            ("Ikimono Gakari - Sakura", "https://youtu.be/0Uhh62MUEic")
        ]
    }
}

# 기분 선택
mood = st.selectbox("✨ 지금 당신의 기분은 어떤가요?", moods)

# 추천 버튼
if st.button("🌈 노래 추천 받기 🎧"):
    cols = st.columns(5)
    all_categories = list(songs.keys())

    for i in range(5):
        with cols[i]:
            category = random.choice(all_categories)
            song = random.choice(songs[category][mood])
            st.markdown(
                f"""
                <div style="background-color:#fff0f5;padding:12px;border-radius:15px;
                box-shadow:2px 2px 8px rgba(0,0,0,0.1);text-align:center;">
                    <h4>🎵 {song[0]}</h4>
                    <p>({category})</p>
                    <a href="{song[1]}" target="_blank">👉 유튜브에서 듣기</a>
                </div>
                """,
                unsafe_allow_html=True
            )
