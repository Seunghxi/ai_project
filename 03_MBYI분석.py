import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# 페이지 설정
# -----------------------------------
st.set_page_config(
    page_title="MBTI 국가 분석",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 MBTI 국가 분석기")

# -----------------------------------
# 데이터 불러오기
# -----------------------------------
df = pd.read_csv("countriesMBTI_16types.csv")

# MBTI 컬럼 추출
mbti_cols = [col for col in df.columns if col != "Country"]

# -----------------------------------
# 탭 생성
# -----------------------------------
tab1, tab2 = st.tabs([
    "🌎 국가별 MBTI 분석",
    "🏆 MBTI별 국가 TOP10"
])

# =====================================================
# TAB 1 : 국가 선택 → MBTI 비율 보기
# =====================================================
with tab1:

    st.header("국가별 MBTI 비율")

    # 국가 선택
    country = st.selectbox(
        "국가 선택",
        sorted(df["Country"].unique())
    )

    # 선택한 국가 데이터
    selected = df[df["Country"] == country].iloc[0]

    # MBTI 높은 순 정렬
    mbti_data = selected[mbti_cols].sort_values(
        ascending=False
    )

    # -----------------------------------
    # 색상 설정
    # 1등 = 노란색
    # 나머지 = 초록 그라데이션
    # -----------------------------------
    colors = []

    for i in range(len(mbti_data)):

        if i == 0:
            colors.append("#FFD700")

        else:
            alpha = 1 - (i / len(mbti_data)) * 0.8

            colors.append(
                (0.2, 0.7, 0.3, alpha)
            )

    # -----------------------------------
    # 그래프 생성
    # -----------------------------------
    fig, ax = plt.subplots(figsize=(12, 6))

    bars = ax.bar(
        mbti_data.index,
        mbti_data.values,
        color=colors
    )

    # 값 표시
    for bar in bars:

        height = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:.1%}",
            ha="center",
            va="bottom",
            fontsize=9
        )

    ax.set_title(
        f"{country} MBTI 비율",
        fontsize=18,
        fontweight="bold"
    )

    ax.set_xlabel("MBTI 유형")
    ax.set_ylabel("비율")

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)

    # 가장 높은 MBTI
    top_mbti = mbti_data.idxmax()
    top_value = mbti_data.max()

    st.success(
        f"🏆 {country}에서 가장 높은 MBTI는 "
        f"{top_mbti} ({top_value:.1%}) 입니다!"
    )

# =====================================================
# TAB 2 : MBTI 선택 → 국가 TOP10
# =====================================================
with tab2:

    st.header("MBTI별 국가 TOP10")

    # MBTI 선택
    selected_mbti = st.selectbox(
        "MBTI 선택",
        mbti_cols
    )

    # 높은 순 정렬 후 TOP10
    top10 = df[
        ["Country", selected_mbti]
    ].sort_values(
        by=selected_mbti,
        ascending=False
    ).head(10)

    # -----------------------------------
    # 색상 설정
    # -----------------------------------
    colors = []

    for i in range(len(top10)):

        if i == 0:
            colors.append("#FFD700")

        else:
            alpha = 1 - (i / len(top10)) * 0.8

            colors.append(
                (0.2, 0.7, 0.3, alpha)
            )

    # -----------------------------------
    # 그래프 생성
    # -----------------------------------
    fig2, ax2 = plt.subplots(figsize=(12, 6))

    bars2 = ax2.bar(
        top10["Country"],
        top10[selected_mbti],
        color=colors
    )

    # 값 표시
    for bar in bars2:

        height = bar.get_height()

        ax2.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:.1%}",
            ha="center",
            va="bottom",
            fontsize=9
        )

    ax2.set_title(
        f"{selected_mbti} 비율이 높은 국가 TOP10",
        fontsize=18,
        fontweight="bold"
    )

    ax2.set_xlabel("국가")
    ax2.set_ylabel("비율")

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig2)

    # 1등 국가 표시
    first_country = top10.iloc[0]["Country"]
    first_value = top10.iloc[0][selected_mbti]

    st.success(
        f"🥇 {selected_mbti} 비율 1위 국가는 "
        f"{first_country} ({first_value:.1%}) 입니다!"
    )
