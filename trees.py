# %%
import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster
import geopandas as gpd
import math
# %%
m1=folium.Map(location=[48.445804976771385, -123.36025493901205],tiles='openstreetmap',zoom_start=12)
m1
# %%
oak=gpd.read_file(r"C:\MyGISstuff\funGIS\Trees\GaryOak_XYTableToPoint.shp")
# %%
oak.head()
# %%
m_2 = folium.Map(location=[48.445804976771385, -123.36025493901205], tiles='cartodbpositron', zoom_start=13)
for idx, row in oak.iterrows():
    Marker([row['lat'], row['lon']]).add_to(m_2)
m_2
# %%
m_3 = folium.Map(location=[48.445804976771385, -123.36025493901205], tiles='cartodbpositron', zoom_start=13)
mc=MarkerCluster()
for idx, row in oak.iterrows():
    if not math.isnan(row['lon']) and not math.isnan(row['lat']):
        mc.add_child(Marker([row['lat'],row['lon']]))
m_3.add_child(mc)
m_3
# %%
m_4 = folium.Map(location=[48.445804976771385, -123.36025493901205], tiles='cartodbpositron', zoom_start=13)
for i in range(0,len(oak)):
    Circle(location=[oak.iloc[i]['lat'],oak.iloc[i]['lon']], radius=20, color='forestgreen').add_to(m_4)
m_4
# %%
m_5 = folium.Map(location=[48.445804976771385, -123.36025493901205], tiles='cartodbpositron', zoom_start=13)
HeatMap(data=oak[['lat', 'lon']], radius=10).add_to(m_5)
m_5
# %%
