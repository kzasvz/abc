import streamlit as st
import random

st.title("🎯 숫자 맞추기 게임 (1~100)")

# 상태 초기화
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)  # 맞춰야 할 숫자
if "tries" not in st.session_state:
    st.session_state.tries = 0
if "message" not in st.session_state:
    st.session_state.message = "숫자를 입력하고 '제출'을 눌러보세요!"

st.write(st.session_state.message)

# 숫자 입력
guess = st.number_input("숫자를 입력하세요 (1~100)", min_value=1, max_value=100, step=1)

if st.button("제출"):
    st.session_state.tries += 1
    if guess < st.session_state.number:
        st.session_state.message = "⬆️ 더 큰 숫자입니다!"
    elif guess > st.session_state.number:
        st.session_state.message = "⬇️ 더 작은 숫자입니다!"
    else:
        st.session_state.message = f"🎉 정답! 숫자는 {st.session_state.number}였습니다. 시도 횟수: {st.session_state.tries}"
        st.balloons()

# 초기화 버튼
if st.button("다시 시작"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.message = "숫자를 입력하고 '제출'을 눌러보세요!"
