iimport streamlit as st
import random

st.title("⚾ 홈런 더비 게임!")

# 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "tries" not in st.session_state:
    st.session_state.tries = 0

st.write("배트 스윙 타이밍을 맞추어 홈런을 날려보세요!")

# 타이밍 조절 슬라이더
swing_timing = st.slider("스윙 타이밍 (0~100)", 0, 100, 50)

# 실제 공의 타이밍 (랜덤)
pitch_timing = random.randint(30, 70)  # 공이 오는 타이밍은 30~70 사이

if st.button("스윙!"):
    st.session_state.tries += 1
    
    # 타이밍 차 계산
    diff = abs(swing_timing - pitch_timing)

    # 판정
    if diff <= 5:
        st.success("🎉 완벽한 타이밍! 홈런!!")
        st.session_state.score += 1
    elif diff <= 15:
        st.warning("✨ 안타! 잘 맞았지만 아쉽게도 홈런은 아님")
    else:
        st.error("💨 헛스윙! 타이밍이 많이 틀림")

    # 정보 출력
    st.write(f"공 타이밍: {pitch_timing}")
    st.write(f"현재 점수(홈런): {st.session_state.score}")
    st.write(f"시도 횟수: {st.session_state.tries} / 10")

    # 게임 종료
    if st.session_state.tries >= 10:
        st.write("---")
        st.subheader("🏁 게임 종료!")
        st.write(f"최종 홈런 수: {st.session_state.score}개")

        if st.button("다시 시작"):
            st.session_state.score = 0
            st.session_state.tries = 0
