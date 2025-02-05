import streamlit as st
import random
import time

# 로또 번호 생성 함수
def when_start():
    로또번호 = []
    인덱스 = 1
    while len(로또번호) < 6:
        뽑은숫자 = random.randint(1, 45)
        if 뽑은숫자 not in 로또번호:
            로또번호.append(뽑은숫자)
        인덱스 += 1
    return 로또번호

# Streamlit 애플리케이션 UI
st.title("🎰 로또 번호 추첨기 🎰")
st.write("버튼을 클릭하여 로또 번호를 추첨하세요!")

# 추첨을 시작할 버튼
if st.button("로또 번호 추첨 시작!"):
    # 버튼을 클릭하면 번호를 추첨하면서 출력
    with st.empty():
        for _ in range(10):  # 번호 추첨을 애니메이션처럼 반복
            로또번호 = when_start()
            st.write(f"현재 추첨 중... {로또번호}")
            time.sleep(0.5)  # 추첨 중 딜레이
    
    # 최종 번호 출력
    로또번호 = when_start()
    st.write(f"🎉 추첨된 로또 번호는: {로또번호} 🎉")
