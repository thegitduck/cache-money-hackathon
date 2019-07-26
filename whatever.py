import folium
import requests

#coordinates=["shit", 38.3050, -85.7500]

def getCoord():
    return requests.get('http://localhost:5000/locations').json()['results']


def addMarkers(m):
    coordinates = getCoord()
    for coord in coordinates:
        print(coord)
        folium.Marker(location=[coord[1], coord[2]], icon=folium.Icon()).add_to(m)


m = folium.Map(location=[38.2527,-85.7585], zoom_start=16)

addMarkers(m)
m.save("map.html")



    
 