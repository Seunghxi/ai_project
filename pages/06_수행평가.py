import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="인천광역시 온실가스 배출량 분석",
    layout="wide"
)

st.title("인천광역시 온실가스 배출량 분석")

uploaded_file = st.file_uploader(
    "CSV 파일을 업로드하세요",
    type=["csv"]
)

if uploaded_file is not None:

    # 인코딩 자동 처리
    try:
        df = pd.read_csv(uploaded_file, encoding="cp949")
    except:
        uploaded_file.seek(0)
        df = pd.read_csv(uploaded_file, encoding="utf-8")

    st.subheader("원본 데이터")
    st.dataframe(df)

    try:
        total = df[df["구분"] == "(직접)총배출량"].iloc[0]

        year_2010 = float(total["2010"])
        year_2023 = float(total["2023"])

        change = year_2023 - year_2010
        change_rate = (change / year_2010) * 100

        st.subheader("과거와 현재 비교")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("2010년", f"{year_2010:,.0f}")

        with col2:
            st.metric("2023년", f"{year_2023:,.0f}")

        st.metric(
            "변화율",
            f"{change_rate:.2f}%"
        )

        graph_df = pd.DataFrame({
            "연도": ["2010", "2023"],
            "배출량": [year_2010, year_2023]
        })

        fig, ax = plt.subplots(figsize=(8, 5))

        ax.bar(
            graph_df["연도"],
            graph_df["배출량"],
            color="blue"
        )

        ax.set_title("인천광역시 온실가스 배출량 비교")
        ax.set_xlabel("연도")
        ax.set_ylabel("배출량 (천 tCO₂eq)")

        st.pyplot(fig)

        st.subheader("문제점")

        st.markdown("""
        ① 여전히 온실가스 배출량이 매우 높음

        ② 에너지 산업의 배출 비중이 큼

        ③ 탄소중립 목표 달성이 쉽지 않음

        ④ 산업·교통 부문의 배출이 지속됨
        """)

    except Exception as e:
        st.error("데이터 형식이 예상과 다릅니다.")
        st.write(e)
