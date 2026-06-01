import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="서울 기온 분석",
    layout="wide"
)

# 한글 깨짐 방지
plt.rcParams["font.family"] = ["Malgun Gothic", "NanumGothic"]
plt.rcParams["axes.unicode_minus"] = False

st.title("🌡️ 서울 기온 분석")

@st.cache_data
def load_data():
    df = pd.read_csv("seoul.csv", encoding="cp949")

    df["날짜"] = pd.to_datetime(df["날짜"])

    df["연도"] = df["날짜"].dt.year
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day

    return df

df = load_data()

# 월 선택
month = st.selectbox(
    "월 선택",
    range(1, 13)
)

# 일 선택
day = st.selectbox(
    "일 선택",
    range(1, 32)
)

# 해당 날짜 필터링
filtered = df[
    (df["월"] == month) &
    (df["일"] == day)
].copy()

filtered = filtered.sort_values("연도")

if len(filtered) > 0:

    fig, ax = plt.subplots(figsize=(14, 6))

    # 최고기온
    ax.plot(
        filtered["연도"],
        filtered["최고기온(℃)"],
        color="red",
        linewidth=2,
        marker="o",
        label="최고기온"
    )

    # 최저기온
    ax.plot(
        filtered["연도"],
        filtered["최저기온(℃)"],
        color="lightskyblue",
        linewidth=2,
        marker="o",
        label="최저기온"
    )

    ax.set_title(
        f"{month}월 {day}일 연도별 최고·최저기온",
        fontsize=16
    )

    ax.set_xlabel("연도")
    ax.set_ylabel("기온(℃)")

    ax.grid(
        True,
        linestyle="--",
        alpha=0.4
    )

    # 범례
    ax.legend()

    st.pyplot(fig)

    st.subheader("데이터")

    st.dataframe(
        filtered[
            ["연도", "최고기온(℃)", "최저기온(℃)"]
        ],
        use_container_width=True
    )

else:
    st.warning("해당 날짜의 데이터가 없습니다.")
