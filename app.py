import streamlit as st
import random

st.title("🎮 숫자 맞추기 게임")

# 게임 상태 초기화
if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 100)
if "tries" not in st.session_state:
    st.session_state.tries = 0

st.write("1부터 100 사이의 숫자를 맞춰보세요!")

# 숫자 입력
guess = st.number_input("추측할 숫자를 입력하세요", min_value=1, max_value=100, step=1)

if st.button("확인"):
    st.session_state.tries += 1
    answer = st.session_state.answer

    if guess < answer:
        st.warning("📉 더 큰 숫자!")
    elif guess > answer:
        st.warning("📈 더 작은 숫자!")
    else:
        st.success(f"🎉 정답입니다! 정답: {answer}")
        st.success(f"총 {st.session_state.tries}번 시도했습니다!")
        if st.button("게임 다시 시작"):
            st.session_state.answer = random.randint(1, 100)
            st.session_state.tries = 0
