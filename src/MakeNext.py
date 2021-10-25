import pandas as pd

data = pd.read_csv("MyData.csv")

df2 = data[["shape","Post_Venue"]]
next_loc = []
for i in range(0,len(df2)):
    next_loc.append(str(df2.iloc[i][0])+"-"+str(df2.iloc[i][1]))
data["next_venue"] = next_loc

data = data.sort_values(by = ["User_ID","Date"], ascending=[False,True])