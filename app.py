import streamlit as st
import random

st.title("🗡️ 장비 강화 게임")

# 상태값 초기화
if "level" not in st.session_state:
    st.session_state.level = 0
if "gold" not in st.session_state:
    st.session_state.gold = 1000

st.write(f"현재 장비 강화 단계: **+{st.session_state.level}**")
st.write(f"보유 골드: **{st.session_state.gold}G**")

st.write("---")

# 강화 비용과 확률
upgrade_cost = 100 + st.session_state.level * 50
success_rate = max(10, 100 - st.session_state.level * 10)
destroy_chance = max(0, st.session_state.level * 2 - 10)

st.write(f"강화 비용: {upgrade_cost}G")
st.write(f"성공 확률: {success_rate}%")
st.write(f"파괴 확률: {destroy_chance}%")

# 강화 버튼
if st.button("강화하기"):
    if st.session_state.gold < upgrade_cost:
        st.error("❌ 골드가 부족합니다!")
    else:
        st.session_state.gold -= upgrade_cost
        roll = random.randint(1, 100)

        if roll <= success_rate:
            st.session_state.level += 1
            st.success(f"🎉 강화 성공! → +{st.session_state.level}")
        elif roll <= success_rate + destroy_chance:
            st.session_state.level = 0
            st.error("💥 장비 파괴! +0 으로 초기화됨")
        else:
            st.warning("⚠️ 강화 실패! 단계 유지")

st.write("---")

# ★★ 판매 기능 추가 ★★
sell_price = 200 + st.session_state.level * 150  # 단계 × 가격 증가

st.write(f"판매 가격: **{sell_price}G**")

if st.button("장비 판매하기"):
    st.session_state.gold += sell_price
