import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium
import os 

zoom_start =  15
file_path = os.path.join(os.getcwd(), "cities.csv")
file_path_1 = os.path.join(os.getcwd(), "Coordonnées_b.csv")

# file_path = os.path.join(os.getcwd(), "Coordonnées.csv")

df = pd.read_csv(file_path)
df1 = pd.read_csv(file_path_1)


# def data_list():
#    data = []
#    latitudes = [latitude for latitude in df["Latitude"] if latitude != "Latitude"]
#    longitudes = [longitude for longitude in df["Longitude"] if longitude != "Longitude"]
#    for row in range(len(df["Latitude"])):
#         data.append({
#            'latitude': float(latitudes[row]),
#            'longitude': float(longitudes[row])
#         })

#    return data



def data_list():
   data = []

   for row in range(len(df["Latitude"])):
        longitude, latitude = df["Latitude"][row], df["Longitude"][row]
        # longitude, latitude, time = df["Latitude"][row], df["Longitude"][row], df["Time"][row]
        data.append({
          #  'time': time,
           'latitude': float(latitude),
           'longitude': float(longitude)
        })

   return data


latitudes = df["Latitude"]
longitudes = df["Longitude"]

data = data_list()

# Barycentre
st.cache_data
def barycentre(latitudes, longitudes):
 latitude = 0.0
 longitude = 0.0

 for i in range(len(latitudes)-1):
   latitude += latitudes[i] / len(latitudes)
   longitude += longitudes[i] / len(longitudes)

 return [float(latitude), float(longitude)]


# if st.button("Mettre à jour"):
#    data = data_list()

latitudes = latitudes.astype(float).tolist()
longitudes = longitudes.astype(float).tolist()

lat_b = df1["Latitude"].astype(float).tolist()
long_b = df1["Longitude"].astype(float).tolist()
time_b = df1["Time"].astype(str).tolist()

points = []

for i in range(len(longitudes)):
   points.append([longitudes[i], latitudes[i]])


st.title("Map de parcours et de potentiels dangers ")


m = folium.Map(location=barycentre(latitudes, longitudes), zoom_start=zoom_start)


for i in range(len(lat_b)):
      folium.Circle(location=(lat_b[i], long_b[i]),
                    raidus = 5,
                    popup=f"(Potentiellement présent, Décourvert à f{time_b[i]})",
                    color="red",
                    fill=True,
                    fill_color="red").add_to(m)

folium.PolyLine(locations=points, color="blue", dash_array="",opacity=".85").add_to(m)

st_folium(m, width=700, height=500)

  # if st.button("Sauvegarder la Map actuelle"):
  #   m.save("map.html")
