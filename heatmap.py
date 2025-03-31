import json
import folium
from mpce_social_grp import data_8R
import pandas as pd

mpce_sg=pd.DataFrame(data_8R)
mpce_sg_st=mpce_sg[['name','Scheduled_Tribe']]

mpce_sg_st_dict=mpce_sg_st.set_index('name')['Scheduled_Tribe']

with open("geoBoundaries-IND-ADM1.geojson", "r", encoding="utf-8") as f:
    geojson_data = json.load(f)

m=folium.Map(location=[20.5937, 78.9629], zoom_start=5,control_scale=True,zoom_control=True,tiles='cartodbpositron')


from branca.colormap import linear
colormap=linear.YlGn_09.scale(
    mpce_sg_st.Scheduled_Tribe.min(),mpce_sg_st.Scheduled_Tribe.max()
)


folium.GeoJson(
    geojson_data,
    name="avg mpce: scheduled tribe",
    style_function=lambda feature: {
        "fillColor": colormap(mpce_sg_st_dict.get(feature["properties"].get("shapeName", ""))),
        "color": "black",
        "weight": 1,
        "dashArray": "5, 5",
        "fillOpacity": 0.9,
    },
).add_to(m)

colormap.caption = "avg mpce: scheduled tribe"
colormap.add_to(m)
folium.LayerControl().add_to(m)
m.save('Social_grp_st.html') 

