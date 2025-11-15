import streamlit as st

st.title("Hello Streamlit!")
st.write("이것은 가장 기본적인 스트림릿 예제입니다 :)")

name = st.text_input("이름을 입력하세요")
if st.button("확인"):
    st.write(f"안녕하세요, {name}님!")
