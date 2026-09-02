import streamlit as st

st.title("專案展示作品集")
st.divider()

st.subheader("專案介紹")


with st.sidebar:
    st.header("選擇專案")
    st.button("專案一")
    st.button("專案二")


c1, c2 = st.columns(2)
with c1:
    st.write("專案一介紹")

with c2:
    st.write("專案二介紹")


with st.bottom:
    st.header("聯絡資訊")
    st.text("Email:aaa@gmail.com")