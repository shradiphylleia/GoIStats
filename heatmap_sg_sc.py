import json
import folium
from mpce_social_grp import data_8R
import pandas as pd
from branca.colormap import linear

mpce_sg = pd.DataFrame(data_8R)
mpce_sg["Scheduled_Caste"] = pd.to_numeric(mpce_sg["Scheduled_Caste"], errors="coerce").fillna(0)

mpce_sg_sc_dict = mpce_sg.set_index('name')["Scheduled_Caste"].to_dict()

with open("geoBoundaries-IND-ADM1.geojson", "r", encoding="utf-8") as f:
    geojson_data = json.load(f)

m = folium.Map(location=[20.5937, 78.9629], zoom_start=5, control_scale=True, zoom_control=True, tiles="cartodbpositron")

colormap = linear.YlGn_09.scale(
    min(mpce_sg["Scheduled_Caste"]), max(mpce_sg["Scheduled_Caste"])
)

folium.GeoJson(
    geojson_data,
    name="avg mpce: scheduled caste",
    style_function=lambda feature: {
        "fillColor": colormap(mpce_sg_sc_dict.get(feature["properties"].get("shapeName", ""), 0)),  # Default to 0
        "color": "black",
        "weight": 1,
        "dashArray": "5, 5",
        "fillOpacity": 0.9,
    },
).add_to(m)

colormap.caption = "avg mpce: scheduled caste"
colormap.add_to(m)

m.save("Social_grp_sc.html")
