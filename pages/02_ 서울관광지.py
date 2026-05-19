import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(
    page_title="서울 인기 관광지 TOP 10",
    page_icon="🇰🇷",
    layout="wide"
)

# 제목 및 설명
st.title("🏯 외국인이 선호하는 서울 주요 관광지 TOP 10")
st.markdown("""
스트림릿 클라우드에서 실행되는 인터랙티브 지도입니다. 
외국인 관광객들에게 인기 있는 서울의 명소들을 확인해보세요!
""")

# 1. 데이터 준비 (장소명, 위도, 경도, 설명)
tourist_spots = [
    {"name": "경복궁", "lat": 37.5796, "lon": 126.9770, "desc": "조선 왕조의 법궁, 한복 체험의 성지"},
    {"name": "N서울타워", "lat": 37.5511, "lon": 126.9882, "desc": "남산 정상에서 보는 서울의 야경"},
    {"name": "명동 거리", "lat": 37.5599, "lon": 126.9858, "desc": "쇼핑과 길거리 음식의 천국"},
    {"name": "북촌 한옥마을", "lat": 37.5826, "lon": 126.9832, "desc": "전통 한옥이 보존된 아름다운 마을"},
    {"name": "동대문 디자인 플라자 (DDP)", "lat": 37.5665, "lon": 127.0092, "desc": "미래 지향적 건축물과 야경명소"},
    {"name": "인사동", "lat": 37.5724, "lon": 126.9856, "desc": "한국의 전통 기념품과 갤러리"},
    {"name": "롯데월드타워 (서울스카이)", "lat": 37.5126, "lon": 127.1025, "desc": "세계에서 5번째로 높은 빌딩"},
    {"name": "광장시장", "lat": 37.5702, "lon": 127.0004, "desc": "빈대떡과 육회 등 K-푸드의 성지"},
    {"name": "홍대 거리", "lat": 37.5567, "lon": 126.9235, "desc": "젊음과 예술, 버스킹의 중심지"},
    {"name": "청계천", "lat": 37.5691, "lon": 126.9787, "desc": "도심 속 시민들의 휴식처"}
]

# 레이아웃 구성
col1, col2 = st.columns([1, 3])

with col1:
    st.subheader("📍 관광지 목록")
    for spot in tourist_spots:
        with st.expander(spot['name']):
            st.write(spot['desc'])

with col2:
    # 2. 폴리움(Folium) 지도 초기화 (서울 중심부)
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

    # 3. 지도에 마커 추가
    for spot in tourist_spots:
        folium.Marker(
            location=[spot['lat'], spot['lon']],
            popup=spot['name'],
            tooltip=f"<b>{spot['name']}</b>",
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)

    # 4. 스트림릿에 지도 표시
    st_folium(m, width=800, height=500)

st.info("💡 각 마커를 클릭하면 장소 이름을 확인할 수 있습니다.")00
