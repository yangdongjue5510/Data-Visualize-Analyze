import pandas as pd

data = pd.read_csv("MyData.csv")

df = data.sort_values(by = ["User_ID","Date"], ascending=[False,True])
sorted_user = df[["User_ID"]]
user_arr = sorted_user.values

step = []
j = 1
for i in range(0, len(user_arr)):
    if i == 0:
        step.append(j)
    else:
        user = user_arr[i]
        if user == user_arr[i-1]:
            j +=1
            step. append(j)
        else:
            j = 1
            step.append(j)
df["step"] = step

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

df2 = df[["Formal_Venue","Venue category name (raw_POIs.txt)"]]
loc_arr = []
for i in range(0,len(df2)):
    loc_arr.append(str(df2.iloc[i][0])+"-"+str(df2.iloc[i][1]))
df["Loc_Plus"] = loc_arr

sorted_df = df.sort_values(by = ["Loc_Plus"], ascending=[True])
shape_arr = sorted_df[["Loc_Plus"]].values.tolist()
input_arr = ["1shape"]
a = 1
for i in range(1,len(shape_arr)):
    if (shape_arr[i] == shape_arr[i-1]):
        input_arr.append(str(a)+"shape")
    else:
        a+=1
        input_arr.append(str(a)+"shape")
sorted_df["shape"] = input_arr
data = sorted_df
df2 = data[["shape","Post_Venue"]]
next_loc = []
for i in range(0,len(df2)):
    next_loc.append(str(df2.iloc[i][0])+"-"+str(df2.iloc[i][1]))
data["next_venue"] = next_loc

data = data.sort_values(by = ["User_ID","Date"], ascending=[False,True])

a = input("이전 Veune입력: ")
b = input("이후 Venue입력: ")
c = a+"-"+b
d = ''
df = data[["Loc_Plus","shape"]]
for i in range(0,len(df)):
    if (c==df.iloc[i,0]):
        d = df.iloc[i,1]
        break
my_frame = pd.DataFrame({"shape_count":data["shape"].value_counts()})
df3 = data[["shape","Post_Venue","next_venue"]]
df4 = df3[df3['shape'] ==d]
print(d)
shape_count = my_frame.loc[d]
print(shape_count)
print(df4["next_venue"].value_counts(normalize=True)*100)