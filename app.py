import streamlit as st
import random
import time

st.title("⏱️ 스피드 퀴즈 게임 (정답 제출 후 2초 자동 이동)")

# 10문제 예시
quiz_data = [
    {"question": "Python에서 리스트를 만드는 기호는?", "options": ["[]", "{}", "()"], "answer": "[]"},
    {"question": "Python에서 문자열 합치는 연산자는?", "options": ["+", "*", "-"], "answer": "+"},
    {"question": "Python에서 'Hello' 출력하려면?", "options": ["print('Hello')", "echo 'Hello'", "console.log('Hello')"], "answer": "print('Hello')"},
    {"question": "2 + 3 * 4는?", "options": ["20", "14", "24"], "answer": "14"},
    {"question": "파이썬에서 나누기 연산자는?", "options": ["/", "//", "%"], "answer": "/"},
    {"question": "Python 변수 이름으로 사용할 수 없는 것은?", "options": ["my_var", "2var", "var2"], "answer": "2var"},
    {"question": "Python에서 반복문을 만드는 키워드는?", "options": ["for", "repeat", "loop"], "answer": "for"},
    {"question": "Python 리스트에서 마지막 요소를 가져오는 방법?", "options": ["list[-1]", "list[0]", "list[last]"], "answer": "list[-1]"},
    {"question": "Python에서 주석을 만드는 기호는?", "options": ["#", "//", "/* */"], "answer": "#"},
    {"question": "Python 함수 정의 키워드는?", "options": ["def", "func", "function"], "answer": "def"}
]

# 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "index" not in st.session_state:
    st.session_state.index = 0
if "selected_quiz" not in st.session_state:
    st.session_state.selected_quiz = random.sample(quiz_data, 5)
if "answered" not in st.session_state:
    st.session_state.answered = False

# 현재 문제
if st.session_state.index < len(st.session_state.selected_quiz):
    current = st.session_state.selected_quiz[st.session_state.index]
    st.subheader(f"문제 {st.session_state.index + 1}: {current['question']}")
    choice = st.radio("정답 선택:", current["options"], key=st.session_state.index)

    if st.button("제출", key=f"btn{st.session_state.index}") and not st.session_state.answered:
        st.session_state.answered = True
        if choice == current["answer"]:
            st.success("정답! 🎉")
            st.session_state.score += 1
        else:
            st.error(f"틀렸습니다! 정답: {current['answer']}")
        
        # 2초 후 다음 문제
        time.sleep(2)
        st.session_state.index += 1
        st.session_state.answered = False
        st.experimental_rerun()

else:
    st.subheader("🏁 퀴즈 종료!")
    st.write(f"최종 점수: {st.session_state.score} / 5")
    if st.button("다시 시작"):
        st.session_state.score = 0
        st.session_state.index = 0
        st.session_state.selected_quiz = random.sample(quiz_data, 5)
        st.experimental_rerun()
