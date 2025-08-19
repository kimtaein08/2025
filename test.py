import streamlit as st
import random

st.set_page_config(page_title="영화 캐릭터 심리테스트", page_icon="🎬", layout="centered")

st.title("🎬 영화 캐릭터 심리테스트")
st.write("당신은 어떤 영화 캐릭터 유형일까요? 질문에 답하고 결과를 확인해보세요!")

# 결과 유형 정의 (이유 포함)
results = {
    "히어로형": "💪 정의롭고 희생정신이 강한 리더 타입!\n- 위기 상황에서 앞장서며 모두를 지키려는 성향이 나타났습니다.",
    "악당형": "😈 매혹적이고 강렬한 카리스마를 가진 타입!\n- 예상치 못한 반전과 독창적인 선택이 나타났습니다.",
    "코믹형": "😂 분위기 메이커, 웃음으로 모두를 즐겁게 하는 타입!\n- 뜻밖의 아이디어로 문제를 해결하는 모습이 나타났습니다.",
    "전략가형": "🧐 똑똑하고 치밀한 두뇌파 타입!\n- 계획적이고 분석적인 선택이 두드러졌습니다.",
    "로맨틱형": "💕 사랑과 감성을 중시하는 따뜻한 타입!\n- 감정을 솔직하게 드러내고 타인을 배려하는 선택이 많았습니다.",
    "미스터리형": "🌌 비밀스럽고 신비로운 매력을 가진 타입!\n- 신비롭고 침착한 성향이 선택에서 나타났습니다.",
    "순수형": "🐣 천진난만하고 착한 순수 타입!\n- 순수하고 따뜻한 마음이 선택에서 드러났습니다.",
    "예술가형": "🎭 창의적이고 감각적인 예술가 타입!\n- 독창적이고 예술적인 선택이 많았습니다."
}

# 질문 & 선택지
questions = [
    ("Q1. 영화 속 위기 상황에서 나는?", {
        "모두를 위해 나선다": "히어로형",
        "계획을 세워 신중하게 움직인다": "전략가형",
        "뜻밖의 기지로 상황을 헤쳐 나간다": "코믹형",
        "상황을 이용해 기회를 노린다": "악당형",
        "사랑하는 사람을 먼저 지킨다": "로맨틱형"
    }),
    ("Q2. 친구들이 날 볼 때 가장 잘 어울리는 말은?", {
        "믿음직한 리더": "히어로형",
        "똑똑하고 계산적": "전략가형",
        "유쾌하고 장난기 많음": "코믹형",
        "카리스마 있고 강렬함": "악당형",
        "따뜻하고 감성적임": "로맨틱형"
    }),
    ("Q3. 영화에서 내가 잘 어울리는 장르는?", {
        "액션/히어로물": "히어로형",
        "스릴러/첩보물": "전략가형",
        "코미디 영화": "코믹형",
        "범죄/빌런 영화": "악당형",
        "로맨스 영화": "로맨틱형"
    }),
    ("Q4. 영화 속 배경이나 장면을 선택할 수 있다면, 당신은 어떤 곳을 좋아할까?", {
        "모두가 힘든 상황에서도 용기를 내야 하는 곳": "히어로형",
        "치밀하게 계획을 세우며 행동할 수 있는 곳": "전략가형",
        "뜻밖의 일이 벌어져 재미있는 사건이 일어나는 곳": "코믹형",
        "예측할 수 없는 반전과 긴장이 있는 곳": "악당형",
        "감정이 풍부하고 따뜻한 분위기의 장소": "로맨틱형"
    }),
    ("Q5. 내가 주인공이라면 영화 속 역할은?", {
        "모두가 위험에 처했을 때 앞장선다": "히어로형",
        "상황을 분석하고 완벽하게 계획한다": "전략가형",
        "뜻밖의 아이디어로 위기를 모면한다": "코믹형",
        "다른 사람들을 놀라게 할 반전을 준비한다": "악당형",
        "감정을 솔직하게 드러내며 다른 사람을 위로한다": "로맨틱형"
    })
]

# 세션 상태 초기화
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'answers' not in st.session_state:
    st.session_state.answers = [None] * len(questions)

q_idx = st.session_state.question_index
question, options = questions[q_idx]

# 질문 출력
st.subheader(question)
choice = st.radio("선택하세요:", list(options.keys()), key=q_idx)
if choice:
    st.session_state.answers[q_idx] = choice

# 이전/다음 버튼
col1, col2 = st.columns(2)
with col1:
    if st.button("이전") and q_idx > 0:
        st.session_state.question_index -= 1
with col2:
    if st.button("다음") and q_idx < len(questions) - 1:
        st.session_state.question_index += 1

# 마지막 질문에서 결과 버튼
if q_idx == len(questions) - 1:
    if st.button("결과 보기"):
        # 점수 계산
        scores = {k:0 for k in results.keys()}
        for i, ans in enumerate(st.session_state.answers):
            if ans:
                scores[options[ans]] += 1 if ans in options else 0
        max_score = max(scores.values())
        top_types = [t for t, s in scores.items() if s == max_score]
        final_type = random.choice(top_types)

        st.subheader("✨ 당신의 영화 캐릭터 유형은?")
        st.success(results[final_type])

        # 선택한 답변 표시
        st.subheader("📝 당신이 선택한 답변")
        for i, ans in enumerate(st.session_state.answers):
            st.write(f"Q{i+1}. {ans}")
