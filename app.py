import streamlit as st
import time
import random

st.title("⚡ 반응 속도 테스트 게임")

# 상태 초기화
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "best_time" not in st.session_state:
    st.session_state.best_time = None

st.write("버튼이 나타나면 최대한 빨리 클릭하세요!")

# 버튼 랜덤 등장
if "button_ready" not in st.session_state:
    st.session_state.button_ready = False

if not st.session_state.button_ready:
    wait_time = random.uniform(1, 5)  # 1~5초 랜덤
    st.write("준비 중...")
    time.sleep(wait_time)
    st.session_state.button_ready = True
    st.session_state.start_time = time.time()

if st.session_state.button_ready:
    if st.button("지금 클릭!"):
        reaction_time = (time.time() - st.session_state.start_time) * 1000  # ms
        st.success(f"반응 속도: {reaction_time:.0f} ms")

        # 최고 기록 갱신
        if (st.session_state.best_time is None) or (reaction_time < st.session_state.best_time):
            st.session_state.best_time = reaction_time
            st.balloons()
            st.write("🏆 최고 기록 갱신!")

        st.write(f"최고 기록: {st.session_state.best_time:.0f} ms")

        # 다음 게임 준비
        st.session_state.button_ready = False
