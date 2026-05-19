import streamlit as st
import folium
from streamlit_folium import st_folium

# 1. Page Configuration
st.set_page_config(
    page_title="Seoul Top 10 Tour Spots",
    page_icon="🇰🇷",
    layout="wide"
)

# 2. Header
st.title("🏯 Seoul Top 10 Tourist Spots for Foreigners")
st.markdown("Interactive map built with Streamlit and Folium. Click markers to check the name.")

st.divider()

# 3. Data Dictionary
tourist_spots = [
    {"name": "Gyeongbokgung Palace (경복궁)", "lat": 37.5796, "lon": 126.9770, "desc": "The main royal palace of the Joseon Dynasty."},
    {"name": "N Seoul Tower (N서울타워)", "lat": 37.5511, "lon": 126.9882, "desc": "Panoramic views of Seoul from Namsan Mountain."},
    {"name": "Myeong-dong (명동)", "lat": 37.5599, "lon": 126.9858, "desc": "A major shopping district and street food heaven."},
    {"name": "Bukchon Hanok Village (북촌한옥마을)", "lat": 37.5826, "lon": 126.9832, "desc": "Traditional Korean village with a rich history."},
    {"name": "DDP (동대문디자인플라자)", "lat": 37.5665, "lon": 127.0092, "desc": "A futuristic landmark with modern architecture."},
    {"name": "Insa-dong (인사동)", "lat": 37.5724, "lon": 126.9856, "desc": "A vibrant street known for traditional goods and tea houses."},
    {"name": "Lotte World Tower (롯데월드타워)", "lat": 37.5126, "lon": 127.1025, "desc": "The 5th tallest building in the world."},
    {"name": "Gwangjang Market (광장시장)", "lat": 37.5702, "lon": 127.0004, "desc": "Famous street food market (K-Food hotspot)."},
    {"name": "Hongdae Street (홍대거리)", "lat": 37.5567, "lon": 126.9235, "desc": "An area known for youthful indie culture and busking."},
    {"name": "Cheonggyecheon Stream (청계천)", "lat": 37.5691, "lon": 126.9787, "desc": "An urban stream oasis in downtown Seoul."}
]

# 4. Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📍 Spot List")
    for spot in tourist_spots:
        with st.expander(spot["name"]):
            st.write(spot["desc"])

with col2:
    st.subheader("🗺️ Map View")
    # Base Map (Center: Seoul)
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

    # Add Markers
    for spot in tourist_spots:
        folium.Marker(
            location=[spot["lat"], spot["lon"]],
            popup=spot["name"],
            tooltip=spot["name"],
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)

    # Render Folium map in Streamlit
    st_folium(m, width=700, height=500)
