import pandas as pd

data = pd.read_csv("MyData.csv")
df = data.sort_values(by = ["User_ID","Date"], ascending=[False,True])

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

sorted_df.to_csv("MyData.csv")