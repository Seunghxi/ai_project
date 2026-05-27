# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib as mpl

# ---------------------------
# 한글 폰트 설정
# ---------------------------
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# ---------------------------
# 데이터 불러오기
# ---------------------------
df = pd.read_excel("인구.xlsx", sheet_name="인구")

# 행정구역 이름 정리
df["지역"] = df["행정구역"].str.split("(").str[0].str.strip()

# 사용할 연령 컬럼
age_columns = [
    "2026년04월_계_0~9세",
    "2026년04월_계_10~19세",
    "2026년04월_계_20~29세",
    "2026년04월_계_30~39세",
    "2026년04월_계_40~49세",
    "2026년04월_계_50~59세",
    "2026년04월_계_60~69세",
    "2026년04월_계_70~79세",
    "2026년04월_계_80~89세",
    "2026년04월_계_90~99세",
    "2026년04월_계_100세 이상"
]

# 숫자형 변환
for col in age_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# ---------------------------
# Streamlit UI
# ---------------------------
st.title("📊 행정구역별 연령 인구 분석")

regions = df["지역"].unique()

selected_region = st.selectbox(
    "행정구역 선택",
    regions
)

# 선택 데이터
row = df[df["지역"] == selected_region].iloc[0]

# x축 / y축 데이터
ages = [
    "0~9",
    "10~19",
    "20~29",
    "30~39",
    "40~49",
    "50~59",
    "60~69",
    "70~79",
    "80~89",
    "90~99",
    "100+"
]

population = [row[col] for col in age_columns]

# ---------------------------
# 그래프 생성
# ---------------------------
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(
    ages,
    population,
    marker="o",
    linewidth=3,
    color="hotpink"
)

# 제목 및 축
ax.set_title(f"{selected_region} 연령별 인구수", fontsize=18)
ax.set_xlabel("나이", fontsize=13)
ax.set_ylabel("인구수", fontsize=13)

# 10살 단위 구분선
ax.grid(
    axis="x",
    linestyle="--",
    alpha=0.6
)

# y축 숫자 쉼표
ax.get_yaxis().set_major_formatter(
    plt.FuncFormatter(lambda x, loc: f"{int(x):,}")
)

st.pyplot(fig)
