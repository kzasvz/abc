import streamlit as st
import random

st.title("🗡️ 장비 강화 게임 (판매 1회 제한)")

# 상태 초기화
if "level" not in st.session_state:
    st.session_state.level = 0
if "gold" not in st.session_state:
    st.session_state.gold = 1000
if "can_sell" not in st.session_state:
    st.session_state.can_sell = True  # 현재 장비 판매 가능 여부

st.write(f"현재 장비 강화 단계: **+{st.session_state.level}**")
st.write(f"보유 골드: **{st.session_state.gold}G**")
st.write(f"판매 가능 여부: {'✅ 판매 가능' if st.session_state.can_sell else '❌ 판매 불가'}")

st.write("---")

# 강화 비용 & 확률
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
            st.session_state.can_sell = True  # 강화 성공하면 판매 가능
            st.success(f"🎉 강화 성공! → +{st.session_state.level}")
        elif roll <= success_rate + destroy_chance:
            st.session_state.level = 0
            st.session_state.can_sell = False  # 파괴되면 판매 불가
            st.error("💥 장비 파괴! +0으로 초기화")
        else:
            st.warning("⚠️ 강화 실패! 단
