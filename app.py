import streamlit as st
import random

# 게임 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "tries" not in st.session_state:
    st.session_state.tries = 0

# 타이틀
st.title("⚽️ 축구 패널티 슈팅 게임")

# 게임 설명
st.write("패널티 슈팅을 하세요! 골대에 공을 넣으면 점수를 얻습니다.")

# 방향 선택
direction = st.radio("어디로 슈팅할까요?", ["왼쪽", "가운데", "오른쪽"])

# 골키퍼가 어느 방향으로 막을지 랜덤 설정
goalkeeper_direction = random.choice(["왼쪽", "가운데", "오른쪽"])

# 슈팅 버튼
if st.button("슈팅!"):
    st.session_state.tries += 1
    
    # 슈팅 성공 여부
    if direction == goalkeeper_direction:
        st.write(f"골키퍼는 {goalkeeper_direction}로 막았습니다. 실축!")
    else:
        st.write(f"골키퍼는 {goalkeeper_direction}로 갔고, 당신은 {direction}으로 슈팅! 골인!")
        st.session_state.score += 1
    
    # 시도 횟수 표시
    st.write(f"시도 횟수: {st.session_state.tries}")
    st.write(f"현재 점수: {st.session_state.score}")

    # 게임 종료 조건
    if st.session_state.tries >= 5:
        st.write(f"게임 종료! 총 점수는 {st.session_state.score}점 입니다.")
        if st.button("다시 시작"):
            st.session_state.score = 0
            st.session_state.tries = 0

