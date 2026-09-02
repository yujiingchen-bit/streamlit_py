import streamlit as st

st.title("專案展示作品集")
st.divider()
st.logo("./image/logo.png", size="small")

with st.sidebar:
    with st.container():
        st.header("選單標題1")
        st.write("選單內容1")
        st.button("按鈕A1")
        st.button("按鈕K1")
    st.divider()
    with st.container():
        st.header("選單標題2")
        st.write("選單內容2")
        st.button("按鈕B")
        st.button("按鈕L")



tab1, tab2, tab3, tab4 = st.tabs(["專案介紹", "專案內容", "專案成果", "操作影片"])

with tab1:
    st.subheader("專案介紹")
    c1, c2 = st.columns(2)
    with c1:
        st.text_input("請輸入您的姓名", key="name")
    with c2:
        st.text_input("請輸入您的電子郵件", key="email")

with tab2:
    st.subheader("專案內容")
    c3=st.container()
    with c3:
        st.write("**早期篩檢與公費政策公費LDCT篩檢：** 台灣國民健康署針對高風險族群提供公費低劑量電腦斷層篩檢，包含具肺癌家族史（具肺癌家族史之50至74歲男性或45至74歲女性）以及重度吸菸史（50至74歲且吸菸史達30包-年以上）的民眾 [0.12]。檢查優勢：LDCT不需禁食、不打顯影劑、過程僅需約5分鐘，能有效揪出小於1公分的微小病灶，大幅提升早期發現率與治癒率。")
        st.write("**日常預防要點戒菸拒菸：** 吸菸是引發肺癌最大的危險因子，並應徹底杜絕二手菸及三手菸。減少油煙：烹調時建議使用抽油煙機，避免吸入過多高溫油煙。防範空污：空氣品質不佳或紫爆時減少戶外劇烈運動，外出配戴口罩。環境防護：工作環境若接觸石綿、砷、氡氣或化學物質，務必落實安全防護。")   

with tab3:
    st.subheader("專案成果")
    st.write("專案成果內容說明")
    st.image("./image/images.jpg", caption="肺癌分析說明")

with tab4:
    st.subheader("操作影片")
    st.video("https://youtu.be/1LtzGS1tArE?si=9Ka9ejZd6h5hY0qU", format="video/mp4", start_time=0,end_time=60,mute=True)

with st.bottom:
    st.header("聯絡資訊")
    st.text("Email:aaa@gmail.com")