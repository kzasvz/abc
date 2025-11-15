import streamlit as st
import random

# 카드 덱 초기화
card_suits = ["♠", "♣", "♦", "♥"]
card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

deck = [f"{value}{suit}" for suit in card_suits for value in card_values]

# 점수 계산 함수
def calculate_card_score(card):
    value = card[:-1]  # 카드에서 숫자나 문자만 추출 (예: 2, 10, J 등)
    if value in ["J", "Q", "K"]:
        return 10
    elif value == "A":
        return 11
    else:
        return int(value)

# 게임 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0

# 타이틀과 카드 뽑기 버튼
st.title("🎴 카드 뽑기 게임")

st.write(f"현재 점수: {st.session_state.score}")

if st.button("카드 뽑기"):
    # 덱에서 랜덤으로 카드 한 장 뽑기
    card = random.choice(deck)
    deck.remove(card)  # 뽑은 카드는 덱에서 제거

    # 점수 계산
    card_score = calculate_card_score(card)
    st.session_state.score += card_score

    # 카드 결과 출력
    st.write(f"뽑은 카드: {card}")
    st.write(f"이 카드의 점수: {card_score}")
    st.write(f"총 점수: {st.session_state.score}")

    # 덱이 비었으면 게임 종료
    if len(deck) == 0:
        st.write("덱이 비었습니다! 게임이 종료되었습니다.")
        if st.button("게임 다시 시작"):
            st.session_state.score = 0
            deck = [f"{value}{suit}" for suit in card_suits for value in card_values]
