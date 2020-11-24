import folium
import pandas as pd
import json

geo_path = 'skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))

# 위도 경도 자료만 따로 모으기
df = pd.read_csv('서울특별시_중구_카페_정보.csv', encoding='utf-8')
latlon = df.loc[:, ['위도', '경도']]

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=7,
                init='k-means++',
                max_iter=300,
                random_state=0)
kmeans.fit(latlon)
df['cluster'] = kmeans.labels_

map = folium.Map(location=[37.5502, 126.982], zoom_start=13)

for n in df.index:
    if df['cluster'][n] == 0:
        icon_color = 'red'
    elif df['cluster'][n] == 1:
        icon_color = 'orange'
    elif df['cluster'][n] == 2:
        icon_color = 'darkred'
    elif df['cluster'][n] == 3:
        icon_color = 'green'
    elif df['cluster'][n] == 4:
        icon_color = 'gray'
    elif df['cluster'][n] == 5:
        icon_color = 'darkblue'
    else:
        icon_color = 'purple'

    folium.CircleMarker(location=[df['위도'][n], df['경도'][n]],
                        radius=10,
                        color=icon_color,
                        fill=True,
                        fill_color=icon_color).add_to(map)

list = kmeans.cluster_centers_
for n in range(7):
    folium.Marker(location=list[n],
                  icon=folium.Icon(icon='cloud')).add_to(map)

map.save('seoul_cafe_kmeans.html')

print(kmeans.cluster_centers_)