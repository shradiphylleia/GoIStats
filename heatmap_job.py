import json
import folium
import pandas as pd
from avg_mpce_household import data
from branca.colormap import linear

mpce_job=pd.DataFrame(data)
mpce_job['Self_Employed_Agriculture']=pd.to_numeric(mpce_job['Self_Employed_Agriculture'],errors='coerce').fillna(0)

mpce_sg_obc_dict=mpce_job.set_index('name')["Self_Employed_Agriculture"].to_dict()

with open("geoBoundaries-IND-ADM1.geojson", "r", encoding="utf-8") as f:
    geojson_data = json.load(f)

m = folium.Map(location=[20.5937, 78.9629], zoom_start=5, control_scale=True, zoom_control=True, tiles="cartodbpositron")

colormap=linear.YlGn_09.scale(
    min(mpce_job["Self_Employed_Agriculture"]), max(mpce_job["Self_Employed_Agriculture"])
)

folium.GeoJson(
    geojson_data,
    name="avg mpce: self employed agriculture",
    style_function=lambda feature: {
        "fillColor": colormap(mpce_sg_obc_dict.get(feature["properties"].get("shapeName", ""), 0)),
        "color": "black",
        "weight": 1,
        "dashArray": "5, 5",
        "fillOpacity": 0.9,
    },
).add_to(m)

colormap.caption = "avg mpce:self emp in agriculture"
colormap.add_to(m)

m.save("job_agri.html")
