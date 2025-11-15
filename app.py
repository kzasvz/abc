import streamlit as st

st.title("📝 퀴즈 게임")

# 퀴즈 문제 리스트
quiz_data = [
    {
        "question": "Python에서 리스트를 생성하는 방법은?",
        "options": ["[]", "{}", "()"],
        "answer": "[]"
    },
    {
        "question": "파이썬에서 문자열을 합치기 위해 사용하는 연산자는?",
        "options": ["+", "*", "-"],
        "answer": "+"
    },
    {
        "question": "파이썬에서 '가' 문자를 출력하려면?",
        "options": ["print('가')", "echo '가'", "console.log('가')"],
        "answer": "print('가')"
    },
]

# 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "index" not in st.session_state:
    st.session_state.index = 0

# 현재 문제
if st.session_state.index < len(quiz_data):
    current = quiz_data[st.session_state.index]
    st.subheader(current["question"])
    choice = st.radio("정답을 선택하세요:", current["options"])

    if st.button("제출"):
        if choice == current["answer"]:
            st.success("정답! 🎉")
            st.session_state.score += 1
        else:
            st.error(f"틀렸습니다! 정답은 {current['answer']} 입니다.")
        st.session_state.index += 1
        st.experimental_rerun()
else:
    st.subheader("🏁 퀴즈 종료!")
    st.write(f"최종 점수: {st.session_state.score} / {len(quiz_data)}")
    if st.button("다시 시작"):
        st.session_state.score = 0
        st.session_state.index = 0
        st.experimental_rerun()
