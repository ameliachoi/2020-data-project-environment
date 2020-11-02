import folium
import pandas as pd

df = pd.read_csv('전국_재활용센터_map.csv', encoding='utf-8')
geo_data = 'skorea_provinces_geo_simple.json'

# 서울시 중심부의 위도, 경도 입니다.
center = [37, 127]

# 맵이 center 에 위치하고, zoom 레벨은 11로 시작하는 맵 m을 만듭니다.
m = folium.Map(location=center, zoom_start=6)


# Choropleth 레이어를 만들고, 맵 m에 추가합니다.
folium.Choropleth(geo_data=geo_data,
                  data=df,
                  columns=('index', '제공기관명'),
                  key_on='feature.properties.name',
                  fill_color='BuPu',
                  legend_name='count',
                  fill_opacity=1,
                  line_opacity=1,
                  smooth_factor=0).add_to(m)

m.save('전국_재활용센터_분포.html')

