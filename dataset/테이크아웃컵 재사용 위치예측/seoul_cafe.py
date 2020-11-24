import folium
import pandas as pd
import json

geo_path = 'skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))

# 위도 경도 자료만 따로 모으기
df = pd.read_csv('서울특별시_중구_카페_정보.csv', encoding='utf-8')

lat = df['위도']
lng = df['경도']

map = folium.Map(location=[37.5502, 126.982], zoom_start=11)

for n in df.index:
    folium.CircleMarker([lat[n], lng[n]],
                        color='#B45F04',
                        fill_color='#B45F04',
                        radius=10).add_to(map)

map.save('seoul_cafe.html')

