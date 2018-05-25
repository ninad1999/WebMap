import folium
import pandas

data = pandas.read_csv("volcanoes.txt")

latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation = list(data["ELEV"])

map = folium.Map(location=[38, -99], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for lat, lon, elev  in zip(latitude, longitude, elevation) :  
	if (1000 < elev < 2000) :
		colour = "#336600"
	elif (2000 < elev < 3000) :
		colour = "#0066ff"
	else:
		colour = "red"
	fgv.add_child(folium.CircleMarker(location=[lat, lon], popup="{} m".format(elev), fill=True, fill_color=colour, fill_opacity=0.7, color=None, radius=8)) 

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), style_function= lambda x: {"fillColor":"green"
if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())
map.save("Map1.html")


