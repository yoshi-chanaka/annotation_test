import streamlit as st

st.title("ミニテスト")

score = 0

# Q1
q1 = st.radio("1. Pythonの作者は？", ["グイド・ヴァンロッサム", "ビル・ゲイツ", "イーロン・マスク"])
if q1 == "グイド・ヴァンロッサム":
    score += 1

# Q2
q2 = st.checkbox("2. Pythonはオープンソースである")
if q2:
    score += 1

# 提出
if st.button("採点する"):
    st.write(f"あなたの得点: {score}/2")

    if score == 2:
        st.success("満点！おめでとうございます🎉パスワードはabcです")
    elif score == 1:
        st.info("もう一歩！復習してみましょう。")
    else:
        st.error("残念！頑張って勉強してください💪")
