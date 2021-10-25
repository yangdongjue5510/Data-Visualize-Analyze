import pandas as pd

data = pd.read_csv("MyData.csv")
df = data.sort_values(by = ["User_ID","Date"], ascending=[False,True])

step_arr = df["step"].tolist()
venue_arr = df["Venue category name (raw_POIs.txt)"].tolist()
lat_arr = df["Latitude (raw_POIs.txt)"].tolist()
lon_arr = df["Longitude (raw_POIs.txt)"].tolist()

Formal_Venue = []
Formal_Lat = []
Formal_Lon = []
for i in range(0,len(step_arr)):
    if(step_arr[i] == 1):
        Formal_Venue.append("NULL")
        Formal_Lat.append("NULL")
        Formal_Lon.append("NULL")
    else:
        Formal_Venue.append(venue_arr[i-1])
        Formal_Lat.append(lat_arr[i-1])
        Formal_Lon.append(lon_arr[i-1])
df["Formal_Venue"] = Formal_Venue
df["Formal_Lat"] = Formal_Lat
df["Formal_Lon"] = Formal_Lon

df.to_csv("MyData.csv")