import pandas as pd

data = pd.read_csv("MyData.csv")
df = data.sort_values(by = ["User_ID","Date"], ascending=[False,True])

step_arr = df["step"].tolist()
venue_arr = df["Venue category name (raw_POIs.txt)"].tolist()
lat_arr = df["Latitude (raw_POIs.txt)"].tolist()
lon_arr = df["Longitude (raw_POIs.txt)"].tolist()

Post_Venue = []
Post_Lat = []
Post_Lon = []
for i in range(0,len(step_arr)-1):
    if(step_arr[i+1] == step_arr[i]+1):
        Post_Venue.append(venue_arr[i+1])
        Post_Lat.append(lat_arr[i+1])
        Post_Lon.append(lon_arr[i+1])
    else:
        Post_Venue.append("NULL")
        Post_Lat.append("NULL")
        Post_Lon.append("NULL")
Post_Venue.append("NULL")
Post_Lat.append("NULL")
Post_Lon.append("NULL")
df["Post_Venue"] = Post_Venue
df["Post_Lat"] = Post_Lat
df["Post_Lon"] = Post_Lon

df.to_csv("MyData.csv")