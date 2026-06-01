import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# 페이지 설정
# ---------------------------
st.set_page_config(
    page_title="서울 기온 분석",
    layout="wide"
)

st.title("🌡️ 서울 기온 분석")

# ---------------------------
# 한글 폰트 설정
# ---------------------------
plt.rcParams["font.family"] = ["Malgun Gothic", "NanumGothic", "AppleGothic"]
plt.rcParams["axes.unicode_minus"] = False

# ---------------------------
# 데이터 불러오기
# ---------------------------
@st.cache_data
def load_data():

    df = pd.read_csv("seoul.csv", encoding="cp949")

    # 날짜 변환 (오류 발생 시 제거)
    df["날짜"] = pd.to_datetime(
        df["날짜"],
        errors="coerce"
    )

    df = df.dropna(subset=["날짜"])

    # 연도, 월, 일 추출
    df["연도"] = df["날짜"].dt.year
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day

    return df

df = load_data()

# ---------------------------
# 월/일 선택
# ---------------------------
col1, col2 = st.columns(2)

with col1:
    selected_month = st.selectbox(
        "월 선택",
        range(1, 13)
    )

with col2:
    selected_day = st.selectbox(
        "일 선택",
        range(1, 32)
    )

# ---------------------------
# 데이터 필터링
# ---------------------------
filtered = df[
    (df["월"] == selected_month) &
    (df["일"] == selected_day)
].copy()

filtered = filtered.sort_values("연도")

# ---------------------------
# 그래프
# ---------------------------
if len(filtered) > 0:

    fig, ax = plt.subplots(figsize=(14, 6))

    # 최고기온 (빨간색)
    ax.plot(
        filtered["연도"],
        filtered["최고기온(℃)"],
        color="red",
        marker="o",
        linewidth=2,
        label="최고기온"
    )

    # 최저기온 (연한 파란색)
    ax.plot(
        filtered["연도"],
        filtered["최저기온(℃)"],
        color="lightskyblue",
        marker="o",
        linewidth=2,
        label="최저기온"
    )

    ax.set_title(
        f"{selected_month}월 {selected_day}일 연도별 최고·최저기온",
        fontsize=16
    )

    ax.set_xlabel("연도")
    ax.set_ylabel("기온(℃)")

    ax.grid(
        True,
        linestyle="--",
        alpha=0.5
    )

    ax.legend()

    st.pyplot(fig)

    # 데이터 표
    st.subheader("📋 데이터")

    st.dataframe(
        filtered[
            ["연도", "최고기온(℃)", "최저기온(℃)"]
        ],
        use_container_width=True
    )

else:
    st.warning("해당 날짜의 데이터가 없습니다.")
